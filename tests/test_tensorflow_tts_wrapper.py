import pytest
import numpy as np
import tensorflow as tf
from unittest.mock import MagicMock, patch
from src.opentts_tensorflow_integration.tensorflow_tts import TensorFlowTTSWrapper
from src.opentts_tensorflow_integration.utils import TTSError, ModelNotFoundError, VoiceNotFoundError

@pytest.fixture
def mock_tensorflow_tts():
    mock = MagicMock()
    mock.processor.load.return_value = MagicMock()
    return mock

@pytest.fixture
def mock_tf():
    mock = MagicMock()
    mock.saved_model.load.return_value = MagicMock()
    return mock

def test_tensorflow_tts_wrapper_initialization():
    wrapper = TensorFlowTTSWrapper()
    assert wrapper.model is None
    assert wrapper.processor is None
    assert wrapper.current_voice is None

def test_load_model(mock_tensorflow_tts, mock_tf):
    with patch('tensorflow.saved_model.load', return_value=MagicMock()) as mock_load, \
         patch('builtins.__import__', side_effect=[mock_tensorflow_tts, mock_tf]):
        wrapper = TensorFlowTTSWrapper()
        wrapper.load_model("path/to/model")
    
    mock_load.assert_called_once_with("path/to/model")
    mock_tensorflow_tts.processor.load.assert_called_once_with("path/to/model_processor")
    assert wrapper.model is not None
    assert wrapper.processor is not None

def test_load_model_error(mock_tf):
    with patch('tensorflow.saved_model.load', side_effect=Exception("Model loading error")), \
         patch('builtins.__import__', side_effect=[ImportError("No module named 'tensorflow_tts'"), mock_tf]):
        wrapper = TensorFlowTTSWrapper()
        with pytest.raises(ImportError):
            wrapper.load_model("path/to/model")

def test_synthesize():
    wrapper = TensorFlowTTSWrapper()
    wrapper.model = MagicMock()
    wrapper.processor = MagicMock()
    wrapper.vocoder = MagicMock()
    
    wrapper.processor.text_to_sequence.return_value = [1, 2, 3]
    wrapper.model.generate_mel.return_value = np.array([[0.1, 0.2], [0.3, 0.4]])
    wrapper.vocoder.return_value = tf.constant([0.1, 0.2, 0.3])
    
    result = wrapper.synthesize("Hello, world!")
    assert isinstance(result, np.ndarray)
    np.testing.assert_array_almost_equal(result, np.array([0.1, 0.2, 0.3]), decimal=6)

def test_synthesize_error():
    wrapper = TensorFlowTTSWrapper()
    with pytest.raises(TTSError):
        wrapper.synthesize("Hello, world!")

def test_available_voices():
    wrapper = TensorFlowTTSWrapper()
    voices = wrapper.available_voices
    assert voices == ["default_voice"]

def test_set_voice():
    wrapper = TensorFlowTTSWrapper()
    wrapper.set_voice("default_voice")
    assert wrapper.current_voice == "default_voice"

def test_set_voice_error():
    wrapper = TensorFlowTTSWrapper()
    with pytest.raises(VoiceNotFoundError):
        wrapper.set_voice("non_existent_voice")

def test_vocoder_not_implemented():
    wrapper = TensorFlowTTSWrapper()
    with pytest.raises(NotImplementedError):
        wrapper.vocoder(np.array([[0.1, 0.2], [0.3, 0.4]]))

# Add more tests as needed# Add more tests as needed# Add more tests as neededdef test_vocoder_not_implemented():
    wrapper = TensorFlowTTSWrapper()
    with pytest.raises(NotImplementedError):
        wrapper.vocoder(np.array([[0.1, 0.2], [0.3, 0.4]]))

# Add more tests as needed