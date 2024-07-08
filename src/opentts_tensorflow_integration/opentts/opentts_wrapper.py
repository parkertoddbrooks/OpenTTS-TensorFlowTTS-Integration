import numpy as np
from ..core import BaseTTS
from ..utils import (
    log_error,
    log_info,
    TTSError,
    ModelNotFoundError,
    VoiceNotFoundError
)
from ..utils.i18n import _

class OpenTTSWrapper(BaseTTS):
    """
    Wrapper class for OpenTTS integration.
    """

    def __init__(self):
        super().__init__()
        self.opentts_engine = None
        log_info(_("Initialized OpenTTSWrapper"))

    def load_model(self, model_path: str):
        """
        Load OpenTTS model.

        Args:
            model_path (str): Path to the OpenTTS model.
        """
        try:
            import opentts
            self.opentts_engine = opentts.TTS(model_path)
            log_info(_("Loaded OpenTTS model from {}").format(model_path))
        except ImportError:
            log_error(_("OpenTTS is not installed"))
            raise ImportError(_("OpenTTS is not installed. Please install it with 'pip install opentts'."))
        except Exception as e:
            log_error(_("Failed to load OpenTTS model: {}").format(str(e)))
            raise ModelNotFoundError(_("Failed to load OpenTTS model: {}").format(str(e)))

    def synthesize(self, text: str) -> np.ndarray:
        """
        Convert text to speech using OpenTTS.

        Args:
            text (str): The input text to be converted to speech.

        Returns:
            np.ndarray: The audio waveform as a numpy array.
        """
        if self.opentts_engine is None:
            log_error(_("OpenTTS engine is not initialized"))
            raise TTSError(_("OpenTTS engine is not initialized. Please call load_model() first."))

        try:
            normalized_text = self.normalize_text(text)
            log_info(_("Synthesizing text: '{}'").format(normalized_text))
            audio = self.opentts_engine.synthesize(normalized_text)
            return np.array(audio)
        except Exception as e:
            log_error(_("Error during speech synthesis: {}").format(str(e)))
            raise TTSError(_("Failed to synthesize speech: {}").format(str(e)))

    @property
    def available_voices(self) -> list:
        """
        Get the list of available voices in OpenTTS.

        Returns:
            list: A list of available voice names.
        """
        if self.opentts_engine is None:
            log_error(_("OpenTTS engine is not initialized"))
            raise TTSError(_("OpenTTS engine is not initialized. Please call load_model() first."))

        try:
            voices = self.opentts_engine.list_voices()
            log_info(_("Available voices: {}").format(voices))
            return voices
        except Exception as e:
            log_error(_("Error retrieving available voices: {}").format(str(e)))
            raise TTSError(_("Failed to retrieve available voices: {}").format(str(e)))

    def set_voice(self, voice_name: str):
        """
        Set the current voice for speech synthesis in OpenTTS.

        Args:
            voice_name (str): The name of the voice to use.
        """
        if self.opentts_engine is None:
            log_error(_("OpenTTS engine is not initialized"))
            raise TTSError(_("OpenTTS engine is not initialized. Please call load_model() first."))

        try:
            if voice_name not in self.available_voices:
                raise VoiceNotFoundError(_("Voice '{}' is not available in OpenTTS.").format(voice_name))

            self.opentts_engine.set_voice(voice_name)
            self.current_voice = voice_name
            log_info(_("Set current voice to '{}'").format(voice_name))
        except VoiceNotFoundError as e:
            log_error(str(e))
            raise
        except Exception as e:
            log_error(_("Error setting voice: {}").format(str(e)))
            raise TTSError(_("Failed to set voice: {}").format(str(e)))