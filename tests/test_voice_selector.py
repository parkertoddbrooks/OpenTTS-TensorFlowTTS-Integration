import pytest
from unittest.mock import MagicMock
from src.opentts_tensorflow_integration.core import VoiceSelector
from src.opentts_tensorflow_integration.utils import TTSError

class MockTTSEngine:
    def __init__(self, available_voices):
        self.available_voices = available_voices
        self.current_voice = None
        self.sample_rate = 22050  # Add sample_rate attribute

    def set_voice(self, voice_name):
        if voice_name not in self.available_voices:
            raise ValueError(f"Voice '{voice_name}' not found.")
        self.current_voice = voice_name

    def synthesize(self, text):
        return f"Synthesized '{text}' with {self.current_voice}"

@pytest.fixture
def voice_selector():
    return VoiceSelector()

def test_add_engine(voice_selector):
    engine = MockTTSEngine(["voice1", "voice2"])
    voice_selector.add_engine("mock_engine", engine)
    assert "mock_engine" in voice_selector.engines

def test_list_engines(voice_selector):
    engine1 = MockTTSEngine(["voice1", "voice2"])
    engine2 = MockTTSEngine(["voice3", "voice4"])
    voice_selector.add_engine("engine1", engine1)
    voice_selector.add_engine("engine2", engine2)
    assert voice_selector.list_engines() == ["engine1", "engine2"]

def test_list_voices(voice_selector):
    engine1 = MockTTSEngine(["voice1", "voice2"])
    engine2 = MockTTSEngine(["voice3", "voice4"])
    voice_selector.add_engine("engine1", engine1)
    voice_selector.add_engine("engine2", engine2)
    
    voices = voice_selector.list_voices()
    assert voices == {"engine1": ["voice1", "voice2"], "engine2": ["voice3", "voice4"]}

    voices_engine1 = voice_selector.list_voices("engine1")
    assert voices_engine1 == {"engine1": ["voice1", "voice2"]}

def test_select_voice(voice_selector):
    engine = MockTTSEngine(["voice1", "voice2"])
    voice_selector.add_engine("mock_engine", engine)
    voice_selector.select_voice("mock_engine", "voice1")
    assert voice_selector.current_engine == "mock_engine"
    assert voice_selector.current_voice == "voice1"

def test_select_voice_error(voice_selector):
    engine = MockTTSEngine(["voice1", "voice2"])
    voice_selector.add_engine("mock_engine", engine)
    with pytest.raises(ValueError):
        voice_selector.select_voice("mock_engine", "non_existent_voice")

def test_get_current_voice(voice_selector):
    engine = MockTTSEngine(["voice1", "voice2"])
    voice_selector.add_engine("mock_engine", engine)
    voice_selector.select_voice("mock_engine", "voice1")
    current_voice = voice_selector.get_current_voice()
    assert current_voice == {"engine": "mock_engine", "voice": "voice1"}

def test_synthesize(voice_selector):
    engine = MockTTSEngine(["voice1", "voice2"])
    voice_selector.add_engine("mock_engine", engine)
    voice_selector.select_voice("mock_engine", "voice1")
    result = voice_selector.synthesize("Hello, world!")
    assert result["audio"] == "Synthesized 'Hello, world!' with voice1"
    assert result["engine"] == "mock_engine"
    assert result["voice"] == "voice1"
    assert result["sample_rate"] == 22050  # Check for sample_rate in the result

def test_synthesize_error(voice_selector):
    with pytest.raises(RuntimeError):  # Change from TTSError to RuntimeError
        voice_selector.synthesize("Hello, world!")

# Add more tests as needed
# Add more tests as needed        voice_selector.synthesize("Hello, world!")

# Add more tests as needed