import pytest
import numpy as np
from unittest.mock import MagicMock, patch
from src.opentts_tensorflow_integration.opentts import OpenTTSWrapper
from src.opentts_tensorflow_integration.utils import TTSError, ModelNotFoundError, VoiceNotFoundError

@pytest.fixture
def mock_opentts():
    mock = MagicMock()
    mock.TTS = MagicMock()
    return mock

def test_opentts_wrapper_initialization():
    wrapper = OpenTTSWrapper()
    assert wrapper.opentts_engine is None
    assert wrapper.current_voice is None

def test_load_model(mock_opentts):
    with patch('builtins.__import__', return_value=mock_opentts):
        wrapper = OpenTTSWrapper()
        wrapper.load_model("path/to/model")
    mock_opentts.TTS.assert_called_once_with("path/to/model")
    assert wrapper.opentts_engine is not None

def test_load_model_error(mock_opentts):
    mock_opentts.TTS.side_effect = Exception("Model loading error")
    with patch('builtins.__import__', return_value=mock_opentts):
        wrapper = OpenTTSWrapper()
        with pytest.raises(ModelNotFoundError):
            wrapper.load_model("path/to/model")

def test_load_model_import_error():
    with patch('builtins.__import__', side_effect=ImportError("No module named 'opentts'")):
        wrapper = OpenTTSWrapper()
        with pytest.raises(ImportError):
            wrapper.load_model("path/to/model")

def test_synthesize():
    wrapper = OpenTTSWrapper()
    wrapper.opentts_engine = MagicMock()
    wrapper.opentts_engine.synthesize.return_value = [0.1, 0.2, 0.3]
    
    result = wrapper.synthesize("Hello, world!")
    assert isinstance(result, np.ndarray)
    np.testing.assert_array_almost_equal(result, np.array([0.1, 0.2, 0.3]), decimal=6)

def test_synthesize_error():
    wrapper = OpenTTSWrapper()
    with pytest.raises(TTSError):
        wrapper.synthesize("Hello, world!")

def test_available_voices():
    wrapper = OpenTTSWrapper()
    wrapper.opentts_engine = MagicMock()
    wrapper.opentts_engine.list_voices.return_value = ["voice1", "voice2"]
    
    voices = wrapper.available_voices
    assert voices == ["voice1", "voice2"]

def test_available_voices_error():
    wrapper = OpenTTSWrapper()
    with pytest.raises(TTSError):
        _ = wrapper.available_voices

def test_set_voice():
    wrapper = OpenTTSWrapper()
    wrapper.opentts_engine = MagicMock()
    wrapper.opentts_engine.list_voices.return_value = ["voice1", "voice2"]
    
    wrapper.set_voice("voice1")
    assert wrapper.current_voice == "voice1"
    wrapper.opentts_engine.set_voice.assert_called_once_with("voice1")

def test_set_voice_error():
    wrapper = OpenTTSWrapper()
    wrapper.opentts_engine = MagicMock()
    wrapper.opentts_engine.list_voices.return_value = ["voice1", "voice2"]
    
    with pytest.raises(VoiceNotFoundError):
        wrapper.set_voice("voice3")

# Add more tests as needed        wrapper.set_voice("voice3")

# Add more tests as needed