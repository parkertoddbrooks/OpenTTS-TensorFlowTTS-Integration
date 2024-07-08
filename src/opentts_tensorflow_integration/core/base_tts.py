from abc import ABC, abstractmethod
import numpy as np
from ..utils import (
    log_error,
    log_info,
    TTSError,
    ModelNotFoundError,
    VoiceNotFoundError,
    AudioConversionError
)
from ..utils.i18n import _

class BaseTTS(ABC):
    """
    Abstract base class for Text-to-Speech engines.
    """

    def __init__(self):
        self.sample_rate = 22050  # Default sample rate, can be overridden in subclasses
        self.current_voice = None
        log_info(_("Initialized {} with sample rate {}").format(self.__class__.__name__, self.sample_rate))

    @abstractmethod
    def synthesize(self, text: str) -> np.ndarray:
        """
        Convert text to speech.

        Args:
            text (str): The input text to be converted to speech.

        Returns:
            np.ndarray: The audio waveform as a numpy array.
        """
        pass

    def normalize_text(self, text: str) -> str:
        """
        Normalize input text for speech synthesis.

        Args:
            text (str): The input text to be normalized.

        Returns:
            str: The normalized text.
        """
        try:
            normalized = text.lower().strip()
            log_info(_("Normalized text: '{}' to '{}'").format(text, normalized))
            return normalized
        except Exception as e:
            log_error(_("Error normalizing text: {}").format(str(e)))
            raise TTSError(_("Failed to normalize text: {}").format(str(e)))

    def save_audio(self, audio: np.ndarray, file_path: str):
        """
        Save the audio waveform to a file.

        Args:
            audio (np.ndarray): The audio waveform as a numpy array.
            file_path (str): The path where the audio file will be saved.
        """
        try:
            import soundfile as sf
            sf.write(file_path, audio, self.sample_rate)
            log_info(_("Saved audio to {}").format(file_path))
        except ImportError:
            log_error(_("soundfile is required to save audio but not installed"))
            raise ImportError(_("soundfile is required to save audio. Please install it with 'pip install soundfile'."))
        except Exception as e:
            log_error(_("Error saving audio: {}").format(str(e)))
            raise AudioConversionError(_("Failed to save audio: {}").format(str(e)))

    @abstractmethod
    def load_model(self, model_path: str):
        """
        Load a TTS model from a file.

        Args:
            model_path (str): The path to the model file.
        """
        pass

    @property
    @abstractmethod
    def available_voices(self) -> list:
        """
        Get the list of available voices.

        Returns:
            list: A list of available voice names.
        """
        pass

    @abstractmethod
    def set_voice(self, voice_name: str):
        """
        Set the current voice for speech synthesis.

        Args:
            voice_name (str): The name of the voice to use.
        """
        pass