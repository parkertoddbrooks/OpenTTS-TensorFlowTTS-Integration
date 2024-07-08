from typing import Dict, List
from .base_tts import BaseTTS
from ..utils.i18n import _

class VoiceSelector:
    """
    A class to manage voice selection across different TTS engines.
    """

    def __init__(self):
        self.engines: Dict[str, BaseTTS] = {}
        self.current_engine: str = None
        self.current_voice: str = None

    def add_engine(self, name: str, engine: BaseTTS):
        """
        Add a TTS engine to the voice selector.

        Args:
            name (str): The name of the engine (e.g., 'OpenTTS', 'TensorFlowTTS').
            engine (BaseTTS): An instance of a TTS engine.
        """
        self.engines[name] = engine

    def list_engines(self) -> List[str]:
        """
        List all available TTS engines.

        Returns:
            List[str]: A list of engine names.
        """
        return list(self.engines.keys())

    def list_voices(self, engine_name: str = None) -> Dict[str, List[str]]:
        """
        List all available voices, optionally for a specific engine.

        Args:
            engine_name (str, optional): The name of the engine to list voices for.

        Returns:
            Dict[str, List[str]]: A dictionary mapping engine names to lists of voice names.
        """
        if engine_name:
            if engine_name not in self.engines:
                raise ValueError(_("Engine '{}' not found.").format(engine_name))
            return {engine_name: self.engines[engine_name].available_voices}
        
        return {name: engine.available_voices for name, engine in self.engines.items()}

    def select_voice(self, engine_name: str, voice_name: str):
        """
        Select a voice from a specific engine.

        Args:
            engine_name (str): The name of the engine to select the voice from.
            voice_name (str): The name of the voice to select.
        """
        if engine_name not in self.engines:
            raise ValueError(_("Engine '{}' not found.").format(engine_name))
        
        engine = self.engines[engine_name]
        if voice_name not in engine.available_voices:
            raise ValueError(_("Voice '{}' not found in engine '{}'.").format(voice_name, engine_name))
        
        engine.set_voice(voice_name)
        self.current_engine = engine_name
        self.current_voice = voice_name

    def get_current_voice(self) -> Dict[str, str]:
        """
        Get the currently selected voice and engine.

        Returns:
            Dict[str, str]: A dictionary with keys 'engine' and 'voice'.
        """
        return {
            'engine': self.current_engine,
            'voice': self.current_voice
        }

    def synthesize(self, text: str) -> Dict[str, any]:
        """
        Synthesize speech using the currently selected engine and voice.

        Args:
            text (str): The text to synthesize.

        Returns:
            Dict[str, any]: A dictionary containing the audio data and metadata.
        """
        if not self.current_engine or not self.current_voice:
            raise RuntimeError(_("No voice selected. Please select a voice first."))
        
        engine = self.engines[self.current_engine]
        audio = engine.synthesize(text)
        
        return {
            'audio': audio,
            'engine': self.current_engine,
            'voice': self.current_voice,
            'sample_rate': engine.sample_rate
        }