(opentts+tensorflowtts-venv) parker@PxB-MBP-16 OpenTTS_TensorFlow_Integration % pytest tests/
======================================================== test session starts =========================================================
platform darwin -- Python 3.12.4, pytest-8.2.2, pluggy-1.5.0
rootdir: /Users/parker/Documents/dev/claude-engineer/_Projects/OpenTTS_TensorFlow_Integration
plugins: mock-3.14.0
collected 39 items                                                                                                                   

tests/test_base_tts.py .......                                                                                                 [ 17%]
tests/test_opentts_wrapper.py .FF......                                                                                        [ 41%]
tests/test_performance_optimizer.py ......                                                                                     [ 56%]
tests/test_tensorflow_tts_wrapper.py .FF......                                                                                 [ 79%]
tests/test_voice_selector.py ........                                                                                          [100%]

============================================================== FAILURES ==============================================================
__________________________________________________________ test_load_model ___________________________________________________________

mocker = <pytest_mock.plugin.MockerFixture object at 0x133d08650>, mock_opentts = <MagicMock id='5164281312'>

    def test_load_model(mocker, mock_opentts):
>       mocker.patch('src.opentts_tensorflow_integration.opentts.opentts_wrapper.opentts', mock_opentts)

tests/test_opentts_wrapper.py:19: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
../../../venvs/opentts+tensorflowtts-venv/lib/python3.12/site-packages/pytest_mock/plugin.py:440: in __call__
    return self._start_patch(
../../../venvs/opentts+tensorflowtts-venv/lib/python3.12/site-packages/pytest_mock/plugin.py:258: in _start_patch
    mocked: MockType = p.start()
/usr/local/Cellar/python@3.12/3.12.4/Frameworks/Python.framework/Versions/3.12/lib/python3.12/unittest/mock.py:1606: in start
    result = self.__enter__()
/usr/local/Cellar/python@3.12/3.12.4/Frameworks/Python.framework/Versions/3.12/lib/python3.12/unittest/mock.py:1458: in __enter__
    original, local = self.get_original()
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <unittest.mock._patch object at 0x12ecef8f0>

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
_______________________________________________________ test_load_model_error ________________________________________________________

mocker = <pytest_mock.plugin.MockerFixture object at 0x133d26b70>, mock_opentts = <MagicMock id='5164397728'>

    def test_load_model_error(mocker, mock_opentts):
>       mocker.patch('src.opentts_tensorflow_integration.opentts.opentts_wrapper.opentts', mock_opentts)

tests/test_opentts_wrapper.py:26: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
../../../venvs/opentts+tensorflowtts-venv/lib/python3.12/site-packages/pytest_mock/plugin.py:440: in __call__
    return self._start_patch(
../../../venvs/opentts+tensorflowtts-venv/lib/python3.12/site-packages/pytest_mock/plugin.py:258: in _start_patch
    mocked: MockType = p.start()
/usr/local/Cellar/python@3.12/3.12.4/Frameworks/Python.framework/Versions/3.12/lib/python3.12/unittest/mock.py:1606: in start
    result = self.__enter__()
/usr/local/Cellar/python@3.12/3.12.4/Frameworks/Python.framework/Versions/3.12/lib/python3.12/unittest/mock.py:1458: in __enter__
    original, local = self.get_original()
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <unittest.mock._patch object at 0x133d27440>

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
__________________________________________________________ test_load_model ___________________________________________________________

mocker = <pytest_mock.plugin.MockerFixture object at 0x133e27e90>, mock_tensorflow_tts = <MagicMock id='5165449136'>
mock_tf = <MagicMock id='5165571184'>

    def test_load_model(mocker, mock_tensorflow_tts, mock_tf):
>       mocker.patch('src.opentts_tensorflow_integration.tensorflow_tts.tensorflow_tts_wrapper.tensorflow_tts', mock_tensorflow_tts)

tests/test_tensorflow_tts_wrapper.py:27: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
../../../venvs/opentts+tensorflowtts-venv/lib/python3.12/site-packages/pytest_mock/plugin.py:440: in __call__
    return self._start_patch(
../../../venvs/opentts+tensorflowtts-venv/lib/python3.12/site-packages/pytest_mock/plugin.py:258: in _start_patch
    mocked: MockType = p.start()
/usr/local/Cellar/python@3.12/3.12.4/Frameworks/Python.framework/Versions/3.12/lib/python3.12/unittest/mock.py:1606: in start
    result = self.__enter__()
/usr/local/Cellar/python@3.12/3.12.4/Frameworks/Python.framework/Versions/3.12/lib/python3.12/unittest/mock.py:1458: in __enter__
    original, local = self.get_original()
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <unittest.mock._patch object at 0x133c223f0>

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
_______________________________________________________ test_load_model_error ________________________________________________________

self = <src.opentts_tensorflow_integration.tensorflow_tts.tensorflow_tts_wrapper.TensorFlowTTSWrapper object at 0x12f0a3d40>
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

mocker = <pytest_mock.plugin.MockerFixture object at 0x133e5cda0>, mock_tf = <MagicMock id='5165666128'>

    def test_load_model_error(mocker, mock_tf):
        mocker.patch('src.opentts_tensorflow_integration.tensorflow_tts.tensorflow_tts_wrapper.tf', mock_tf)
        mock_tf.saved_model.load.side_effect = Exception("Model loading error")
        wrapper = TensorFlowTTSWrapper()
        with pytest.raises(ModelNotFoundError):
>           wrapper.load_model("path/to/model")

tests/test_tensorflow_tts_wrapper.py:41: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <src.opentts_tensorflow_integration.tensorflow_tts.tensorflow_tts_wrapper.TensorFlowTTSWrapper object at 0x12f0a3d40>
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
-------------------------------------------------------- Captured stderr call --------------------------------------------------------
2024-07-07 20:38:40,665 - opentts_tensorflow_integration - INFO - Initialized TensorFlowTTSWrapper with sample rate 22050
2024-07-07 20:38:40,665 - opentts_tensorflow_integration - INFO - Initialized TensorFlowTTSWrapper
2024-07-07 20:38:40,666 - opentts_tensorflow_integration - ERROR - str: TensorFlow TTS is not installed
--------------------------------------------------------- Captured log call ----------------------------------------------------------
INFO     opentts_tensorflow_integration:logging_utils.py:78 Initialized TensorFlowTTSWrapper with sample rate 22050
INFO     opentts_tensorflow_integration:logging_utils.py:78 Initialized TensorFlowTTSWrapper
ERROR    opentts_tensorflow_integration:logging_utils.py:60 str: TensorFlow TTS is not installed
========================================================== warnings summary ==========================================================
<frozen importlib._bootstrap>:488
  <frozen importlib._bootstrap>:488: DeprecationWarning: Type google._upb._message.MessageMapContainer uses PyType_Spec with a metaclass that has custom tp_new. This is deprecated and will no longer be allowed in Python 3.14.

<frozen importlib._bootstrap>:488
  <frozen importlib._bootstrap>:488: DeprecationWarning: Type google._upb._message.ScalarMapContainer uses PyType_Spec with a metaclass that has custom tp_new. This is deprecated and will no longer be allowed in Python 3.14.

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
====================================================== short test summary info =======================================================
FAILED tests/test_opentts_wrapper.py::test_load_model - AttributeError: <module 'src.opentts_tensorflow_integration.opentts.opentts_wrapper' from '/Users/parker/Documents/dev/claude-eng...
FAILED tests/test_opentts_wrapper.py::test_load_model_error - AttributeError: <module 'src.opentts_tensorflow_integration.opentts.opentts_wrapper' from '/Users/parker/Documents/dev/claude-eng...
FAILED tests/test_tensorflow_tts_wrapper.py::test_load_model - AttributeError: <module 'src.opentts_tensorflow_integration.tensorflow_tts.tensorflow_tts_wrapper' from '/Users/parker/Documents/...
FAILED tests/test_tensorflow_tts_wrapper.py::test_load_model_error - ImportError: TensorFlow TTS is not installed. Please install it with 'pip install TensorFlowTTS'.
============================================== 4 failed, 35 passed, 2 warnings in 4.33s ==============================================
(opentts+tensorflowtts-venv) parker@PxB-MBP-16 OpenTTS_TensorFlow_Integration % 
