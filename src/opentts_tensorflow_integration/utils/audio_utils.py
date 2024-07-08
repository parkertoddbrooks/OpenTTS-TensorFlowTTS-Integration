import numpy as np
from typing import Tuple

class AudioUtils:
    """
    Utility class for audio processing and format conversion.
    """

    @staticmethod
    def convert_to_wav(audio: np.ndarray, sample_rate: int) -> bytes:
        """
        Convert numpy array audio data to WAV format.

        Args:
            audio (np.ndarray): Audio data as a numpy array.
            sample_rate (int): The sample rate of the audio.

        Returns:
            bytes: WAV file content as bytes.
        """
        try:
            import io
            import wave
            import struct

            # Ensure audio data is in the correct format (16-bit PCM)
            audio_int16 = (audio * 32767).astype(np.int16)

            buffer = io.BytesIO()
            with wave.open(buffer, 'wb') as wav_file:
                wav_file.setnchannels(1)  # mono
                wav_file.setsampwidth(2)  # 16-bit
                wav_file.setframerate(sample_rate)
                wav_file.writeframes(audio_int16.tobytes())

            return buffer.getvalue()
        except ImportError:
            raise ImportError("wave module is required for WAV conversion.")

    @staticmethod
    def convert_to_mp3(audio: np.ndarray, sample_rate: int) -> bytes:
        """
        Convert numpy array audio data to MP3 format.

        Args:
            audio (np.ndarray): Audio data as a numpy array.
            sample_rate (int): The sample rate of the audio.

        Returns:
            bytes: MP3 file content as bytes.
        """
        try:
            import io
            import pydub

            # Convert to WAV first
            wav_data = AudioUtils.convert_to_wav(audio, sample_rate)

            # Use pydub to convert WAV to MP3
            audio_segment = pydub.AudioSegment.from_wav(io.BytesIO(wav_data))
            buffer = io.BytesIO()
            audio_segment.export(buffer, format="mp3")

            return buffer.getvalue()
        except ImportError:
            raise ImportError("pydub is required for MP3 conversion. Install it with 'pip install pydub'.")

    @staticmethod
    def convert_to_ogg(audio: np.ndarray, sample_rate: int) -> bytes:
        """
        Convert numpy array audio data to OGG format.

        Args:
            audio (np.ndarray): Audio data as a numpy array.
            sample_rate (int): The sample rate of the audio.

        Returns:
            bytes: OGG file content as bytes.
        """
        try:
            import io
            import pydub

            # Convert to WAV first
            wav_data = AudioUtils.convert_to_wav(audio, sample_rate)

            # Use pydub to convert WAV to OGG
            audio_segment = pydub.AudioSegment.from_wav(io.BytesIO(wav_data))
            buffer = io.BytesIO()
            audio_segment.export(buffer, format="ogg")

            return buffer.getvalue()
        except ImportError:
            raise ImportError("pydub is required for OGG conversion. Install it with 'pip install pydub'.")

    @staticmethod
    def save_audio(audio: np.ndarray, file_path: str, sample_rate: int, format: str = 'wav'):
        """
        Save audio data to a file in the specified format.

        Args:
            audio (np.ndarray): Audio data as a numpy array.
            file_path (str): Path to save the audio file.
            sample_rate (int): The sample rate of the audio.
            format (str): The desired output format ('wav', 'mp3', or 'ogg').
        """
        if format == 'wav':
            audio_data = AudioUtils.convert_to_wav(audio, sample_rate)
        elif format == 'mp3':
            audio_data = AudioUtils.convert_to_mp3(audio, sample_rate)
        elif format == 'ogg':
            audio_data = AudioUtils.convert_to_ogg(audio, sample_rate)
        else:
            raise ValueError(f"Unsupported audio format: {format}")

        with open(file_path, 'wb') as f:
            f.write(audio_data)

    @staticmethod
    def resample(audio: np.ndarray, original_sr: int, target_sr: int) -> Tuple[np.ndarray, int]:
        """
        Resample audio data to a different sample rate.

        Args:
            audio (np.ndarray): Audio data as a numpy array.
            original_sr (int): The original sample rate of the audio.
            target_sr (int): The target sample rate.

        Returns:
            Tuple[np.ndarray, int]: Resampled audio data and the new sample rate.
        """
        try:
            import librosa
            resampled_audio = librosa.resample(audio, orig_sr=original_sr, target_sr=target_sr)
            return resampled_audio, target_sr
        except ImportError:
            raise ImportError("librosa is required for resampling. Install it with 'pip install librosa'.")