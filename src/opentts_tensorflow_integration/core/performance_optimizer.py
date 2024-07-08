import hashlib
from typing import List, Dict, Any
import numpy as np
from .base_tts import BaseTTS
from ..utils.i18n import _

class PerformanceOptimizer:
    """
    A class to handle performance optimizations for TTS operations.
    """

    def __init__(self, cache_size: int = 100):
        """
        Initialize the PerformanceOptimizer.

        Args:
            cache_size (int): Maximum number of items to keep in the cache. Defaults to 100.
        """
        self.cache: Dict[str, np.ndarray] = {}
        self.cache_size = cache_size

    def _generate_cache_key(self, text: str, engine: str, voice: str) -> str:
        """
        Generate a unique cache key for a given text, engine, and voice.

        Args:
            text (str): The input text.
            engine (str): The name of the TTS engine.
            voice (str): The name of the voice.

        Returns:
            str: A unique cache key.
        """
        key = f"{text}|{engine}|{voice}"
        return hashlib.md5(key.encode()).hexdigest()

    def get_cached_audio(self, text: str, engine: str, voice: str) -> np.ndarray:
        """
        Retrieve cached audio for a given text, engine, and voice.

        Args:
            text (str): The input text.
            engine (str): The name of the TTS engine.
            voice (str): The name of the voice.

        Returns:
            np.ndarray: The cached audio data, or None if not found in cache.
        """
        cache_key = self._generate_cache_key(text, engine, voice)
        return self.cache.get(cache_key)

    def cache_audio(self, text: str, engine: str, voice: str, audio: np.ndarray):
        """
        Cache the generated audio for a given text, engine, and voice.

        Args:
            text (str): The input text.
            engine (str): The name of the TTS engine.
            voice (str): The name of the voice.
            audio (np.ndarray): The generated audio data.
        """
        cache_key = self._generate_cache_key(text, engine, voice)
        if len(self.cache) >= self.cache_size:
            # Remove the oldest item if cache is full
            oldest_key = next(iter(self.cache))
            del self.cache[oldest_key]
        self.cache[cache_key] = audio

    def batch_process(self, tts_engine: BaseTTS, texts: List[str]) -> List[np.ndarray]:
        """
        Process multiple TTS requests in batch.

        Args:
            tts_engine (BaseTTS): The TTS engine to use for synthesis.
            texts (List[str]): A list of texts to synthesize.

        Returns:
            List[np.ndarray]: A list of audio arrays corresponding to the input texts.
        """
        results = []
        for text in texts:
            # Check cache first
            cached_audio = self.get_cached_audio(text, tts_engine.__class__.__name__, tts_engine.current_voice)
            if cached_audio is not None:
                results.append(cached_audio)
            else:
                # Generate audio if not in cache
                audio = tts_engine.synthesize(text)
                self.cache_audio(text, tts_engine.__class__.__name__, tts_engine.current_voice, audio)
                results.append(audio)
        return results

    def clear_cache(self):
        """
        Clear the entire cache.
        """
        self.cache.clear()

    def get_cache_stats(self) -> Dict[str, Any]:
        """
        Get statistics about the current state of the cache.

        Returns:
            Dict[str, Any]: A dictionary containing cache statistics.
        """
        return {
            "cache_size": len(self.cache),
            "max_cache_size": self.cache_size,
            "cache_usage": _("{:.2f}%").format(len(self.cache) / self.cache_size * 100)
        }