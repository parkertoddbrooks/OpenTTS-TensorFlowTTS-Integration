(opentts+tensorflowtts-venv) parker@PxB-MBP-16 OpenTTS_TensorFlow_Integration % export PYTHONPATH="/Users/parker/Documents/dev/claude-engineer/_Projects/OpenTTS_TensorFlow_Integration:$PYTHONPATH"
(opentts+tensorflowtts-venv) parker@PxB-MBP-16 OpenTTS_TensorFlow_Integration % pytest tests/
=================================================== test session starts ===================================================
platform darwin -- Python 3.12.4, pytest-8.2.2, pluggy-1.5.0
rootdir: /Users/parker/Documents/dev/claude-engineer/_Projects/OpenTTS_TensorFlow_Integration
collected 39 items                                                                                                        

tests/test_base_tts.py .......                                                                                      [ 17%]
tests/test_opentts_wrapper.py .EE......                                                                             [ 41%]
tests/test_performance_optimizer.py ......                                                                          [ 56%]
tests/test_tensorflow_tts_wrapper.py .EFF.....                                                                      [ 79%]
tests/test_voice_selector.py ......FF                                                                               [100%]

========================================================= ERRORS ==========================================================
____________________________________________ ERROR at setup of test_load_model ____________________________________________

    @pytest.fixture
    def mock_opentts():
>       with patch('src.opentts_tensorflow_integration.opentts.opentts_wrapper.opentts') as mock:

tests/test_opentts_wrapper.py:9: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
/usr/local/Cellar/python@3.12/3.12.4/Frameworks/Python.framework/Versions/3.12/lib/python3.12/unittest/mock.py:1458: in __enter__
    original, local = self.get_original()
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

self = <unittest.mock._patch object at 0x133f58560>

    def get_original(self):
        target = self.getter()
        name = self.attribute
    
        original = DEFAULT
        local = False
    
        try:
            original = target.__dict__[name]
        except (AttributeError, KeyError):
            original = getattr(target, name, DEFAULT)
        else:
            local = True
    
        if name in _builtins and isinstance(target, ModuleType):
            self.create = True
    
        if not self.create and original is DEFAULT:
>           raise AttributeError(
                "%s does not have the attribute %r" % (target, name)
            )
E           AttributeError: <module 'src.opentts_tensorflow_integration.opentts.opentts_wrapper' from '/Users/parker/Documents/dev/claude-engineer/_Projects/OpenTTS_TensorFlow_Integration/src/opentts_tensorflow_integration/opentts/opentts_wrapper.py'> does not have the attribute 'opentts'

/usr/local/Cellar/python@3.12/3.12.4/Frameworks/Python.framework/Versions/3.12/lib/python3.12/unittest/mock.py:1431: AttributeError
_________________________________________ ERROR at setup of test_load_model_error _________________________________________

    @pytest.fixture
    def mock_opentts():
>       with patch('src.opentts_tensorflow_integration.opentts.opentts_wrapper.opentts') as mock:

tests/test_opentts_wrapper.py:9: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
/usr/local/Cellar/python@3.12/3.12.4/Frameworks/Python.framework/Versions/3.12/lib/python3.12/unittest/mock.py:1458: in __enter__
    original, local = self.get_original()
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

self = <unittest.mock._patch object at 0x1317bed20>

    def get_original(self):
        target = self.getter()
        name = self.attribute
    
        original = DEFAULT
        local = False
    
        try:
            original = target.__dict__[name]
        except (AttributeError, KeyError):
            original = getattr(target, name, DEFAULT)
        else:
            local = True
    
        if name in _builtins and isinstance(target, ModuleType):
            self.create = True
    
        if not self.create and original is DEFAULT:
>           raise AttributeError(
                "%s does not have the attribute %r" % (target, name)
            )
E           AttributeError: <module 'src.opentts_tensorflow_integration.opentts.opentts_wrapper' from '/Users/parker/Documents/dev/claude-engineer/_Projects/OpenTTS_TensorFlow_Integration/src/opentts_tensorflow_integration/opentts/opentts_wrapper.py'> does not have the attribute 'opentts'

/usr/local/Cellar/python@3.12/3.12.4/Frameworks/Python.framework/Versions/3.12/lib/python3.12/unittest/mock.py:1431: AttributeError
____________________________________________ ERROR at setup of test_load_model ____________________________________________

    @pytest.fixture
    def mock_tensorflow_tts():
>       with patch('src.opentts_tensorflow_integration.tensorflow_tts.tensorflow_tts_wrapper.tensorflow_tts') as mock:

tests/test_tensorflow_tts_wrapper.py:10: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
/usr/local/Cellar/python@3.12/3.12.4/Frameworks/Python.framework/Versions/3.12/lib/python3.12/unittest/mock.py:1458: in __enter__
    original, local = self.get_original()
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

self = <unittest.mock._patch object at 0x133f87f50>

    def get_original(self):
        target = self.getter()
        name = self.attribute
    
        original = DEFAULT
        local = False
    
        try:
            original = target.__dict__[name]
        except (AttributeError, KeyError):
            original = getattr(target, name, DEFAULT)
        else:
            local = True
    
        if name in _builtins and isinstance(target, ModuleType):
            self.create = True
    
        if not self.create and original is DEFAULT:
>           raise AttributeError(
                "%s does not have the attribute %r" % (target, name)
            )
E           AttributeError: <module 'src.opentts_tensorflow_integration.tensorflow_tts.tensorflow_tts_wrapper' from '/Users/parker/Documents/dev/claude-engineer/_Projects/OpenTTS_TensorFlow_Integration/src/opentts_tensorflow_integration/tensorflow_tts/tensorflow_tts_wrapper.py'> does not have the attribute 'tensorflow_tts'

/usr/local/Cellar/python@3.12/3.12.4/Frameworks/Python.framework/Versions/3.12/lib/python3.12/unittest/mock.py:1431: AttributeError
======================================================== FAILURES =========================================================
__________________________________________________ test_load_model_error __________________________________________________

self = <src.opentts_tensorflow_integration.tensorflow_tts.tensorflow_tts_wrapper.TensorFlowTTSWrapper object at 0x133f84260>
model_path = 'path/to/model'

    def load_model(self, model_path: str):
        """
        Load TensorFlow TTS model.
    
        Args:
            model_path (str): Path to the TensorFlow TTS model.
        """
        try:
>           import tensorflow_tts
E           ModuleNotFoundError: No module named 'tensorflow_tts'

src/opentts_tensorflow_integration/tensorflow_tts/tensorflow_tts_wrapper.py:33: ModuleNotFoundError

During handling of the above exception, another exception occurred:

mock_tf = <MagicMock name='tf' id='5166888192'>

    def test_load_model_error(mock_tf):
        mock_tf.saved_model.load.side_effect = Exception("Model loading error")
        wrapper = TensorFlowTTSWrapper()
        with pytest.raises(ModelNotFoundError):
>           wrapper.load_model("path/to/model")

tests/test_tensorflow_tts_wrapper.py:36: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

self = <src.opentts_tensorflow_integration.tensorflow_tts.tensorflow_tts_wrapper.TensorFlowTTSWrapper object at 0x133f84260>
model_path = 'path/to/model'

    def load_model(self, model_path: str):
        """
        Load TensorFlow TTS model.
    
        Args:
            model_path (str): Path to the TensorFlow TTS model.
        """
        try:
            import tensorflow_tts
            self.model = tf.saved_model.load(model_path)
            # Assuming the processor is saved alongside the model
            self.processor = tensorflow_tts.processor.load(f"{model_path}_processor")
            log_info(_("Loaded TensorFlow TTS model from {}").format(model_path))
        except ImportError:
            log_error(_("TensorFlow TTS is not installed"))
>           raise ImportError(_("TensorFlow TTS is not installed. Please install it with 'pip install TensorFlowTTS'."))
E           ImportError: TensorFlow TTS is not installed. Please install it with 'pip install TensorFlowTTS'.

src/opentts_tensorflow_integration/tensorflow_tts/tensorflow_tts_wrapper.py:40: ImportError
-------------------------------------------------- Captured stderr call ---------------------------------------------------
2024-07-07 17:01:36,168 - opentts_tensorflow_integration - INFO - Initialized TensorFlowTTSWrapper with sample rate 22050
2024-07-07 17:01:36,169 - opentts_tensorflow_integration - INFO - Initialized TensorFlowTTSWrapper
2024-07-07 17:01:36,169 - opentts_tensorflow_integration - ERROR - str: TensorFlow TTS is not installed
---------------------------------------------------- Captured log call ----------------------------------------------------
INFO     opentts_tensorflow_integration:logging_utils.py:78 Initialized TensorFlowTTSWrapper with sample rate 22050
INFO     opentts_tensorflow_integration:logging_utils.py:78 Initialized TensorFlowTTSWrapper
ERROR    opentts_tensorflow_integration:logging_utils.py:60 str: TensorFlow TTS is not installed
_____________________________________________________ test_synthesize _____________________________________________________

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
>       np.testing.assert_array_equal(result, np.array([0.1, 0.2, 0.3]))

tests/test_tensorflow_tts_wrapper.py:50: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

args = (<built-in function eq>, array([0.1, 0.2, 0.3], dtype=float32), array([0.1, 0.2, 0.3]))
kwds = {'err_msg': '', 'header': 'Arrays are not equal', 'strict': False, 'verbose': True}

    @wraps(func)
    def inner(*args, **kwds):
        with self._recreate_cm():
>           return func(*args, **kwds)
E           AssertionError: 
E           Arrays are not equal
E           
E           Mismatched elements: 3 / 3 (100%)
E           Max absolute difference: 1.1920929e-08
E           Max relative difference: 3.97364299e-08
E            x: array([0.1, 0.2, 0.3], dtype=float32)
E            y: array([0.1, 0.2, 0.3])

/usr/local/Cellar/python@3.12/3.12.4/Frameworks/Python.framework/Versions/3.12/lib/python3.12/contextlib.py:81: AssertionError
-------------------------------------------------- Captured stderr call ---------------------------------------------------
2024-07-07 17:01:36,177 - opentts_tensorflow_integration - INFO - Initialized TensorFlowTTSWrapper with sample rate 22050
2024-07-07 17:01:36,177 - opentts_tensorflow_integration - INFO - Initialized TensorFlowTTSWrapper
2024-07-07 17:01:36,192 - opentts_tensorflow_integration - INFO - Normalized text: 'Hello, world!' to 'hello, world!'
2024-07-07 17:01:36,193 - opentts_tensorflow_integration - INFO - Synthesizing text: 'hello, world!'
---------------------------------------------------- Captured log call ----------------------------------------------------
INFO     opentts_tensorflow_integration:logging_utils.py:78 Initialized TensorFlowTTSWrapper with sample rate 22050
INFO     opentts_tensorflow_integration:logging_utils.py:78 Initialized TensorFlowTTSWrapper
INFO     opentts_tensorflow_integration:logging_utils.py:78 Normalized text: 'Hello, world!' to 'hello, world!'
INFO     opentts_tensorflow_integration:logging_utils.py:78 Synthesizing text: 'hello, world!'
_____________________________________________________ test_synthesize _____________________________________________________

voice_selector = <src.opentts_tensorflow_integration.core.voice_selector.VoiceSelector object at 0x134794230>

    def test_synthesize(voice_selector):
        engine = MockTTSEngine(["voice1", "voice2"])
        voice_selector.add_engine("mock_engine", engine)
        voice_selector.select_voice("mock_engine", "voice1")
>       result = voice_selector.synthesize("Hello, world!")

tests/test_voice_selector.py:71: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

self = <src.opentts_tensorflow_integration.core.voice_selector.VoiceSelector object at 0x134794230>, text = 'Hello, world!'

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
>           'sample_rate': engine.sample_rate
        }
E       AttributeError: 'MockTTSEngine' object has no attribute 'sample_rate'

src/opentts_tensorflow_integration/core/voice_selector.py:102: AttributeError
__________________________________________________ test_synthesize_error __________________________________________________

voice_selector = <src.opentts_tensorflow_integration.core.voice_selector.VoiceSelector object at 0x13407a3f0>

    def test_synthesize_error(voice_selector):
        with pytest.raises(TTSError):
>           voice_selector.synthesize("Hello, world!")

tests/test_voice_selector.py:78: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

self = <src.opentts_tensorflow_integration.core.voice_selector.VoiceSelector object at 0x13407a3f0>, text = 'Hello, world!'

    def synthesize(self, text: str) -> Dict[str, any]:
        """
        Synthesize speech using the currently selected engine and voice.
    
        Args:
            text (str): The text to synthesize.
    
        Returns:
            Dict[str, any]: A dictionary containing the audio data and metadata.
        """
        if not self.current_engine or not self.current_voice:
>           raise RuntimeError(_("No voice selected. Please select a voice first."))
E           RuntimeError: No voice selected. Please select a voice first.

src/opentts_tensorflow_integration/core/voice_selector.py:93: RuntimeError
==================================================== warnings summary =====================================================
<frozen importlib._bootstrap>:488
  <frozen importlib._bootstrap>:488: DeprecationWarning: Type google._upb._message.MessageMapContainer uses PyType_Spec with a metaclass that has custom tp_new. This is deprecated and will no longer be allowed in Python 3.14.

<frozen importlib._bootstrap>:488
  <frozen importlib._bootstrap>:488: DeprecationWarning: Type google._upb._message.ScalarMapContainer uses PyType_Spec with a metaclass that has custom tp_new. This is deprecated and will no longer be allowed in Python 3.14.

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
================================================= short test summary info =================================================
FAILED tests/test_tensorflow_tts_wrapper.py::test_load_model_error - ImportError: TensorFlow TTS is not installed. Please install it with 'pip install TensorFlowTTS'.
FAILED tests/test_tensorflow_tts_wrapper.py::test_synthesize - AssertionError: 
FAILED tests/test_voice_selector.py::test_synthesize - AttributeError: 'MockTTSEngine' object has no attribute 'sample_rate'
FAILED tests/test_voice_selector.py::test_synthesize_error - RuntimeError: No voice selected. Please select a voice first.
ERROR tests/test_opentts_wrapper.py::test_load_model - AttributeError: <module 'src.opentts_tensorflow_integration.opentts.opentts_wrapper' from '/Users/parker/Documents/dev...
ERROR tests/test_opentts_wrapper.py::test_load_model_error - AttributeError: <module 'src.opentts_tensorflow_integration.opentts.opentts_wrapper' from '/Users/parker/Documents/dev...
ERROR tests/test_tensorflow_tts_wrapper.py::test_load_model - AttributeError: <module 'src.opentts_tensorflow_integration.tensorflow_tts.tensorflow_tts_wrapper' from '/Users/parker...
=================================== 4 failed, 32 passed, 2 warnings, 3 errors in 15.01s ===================================
(opentts+tensorflowtts-venv) parker@PxB-MBP-16 OpenTTS_TensorFlow_Integration % 
