(opentts+tensorflowtts-venv) parker@PxB-MBP-16 OpenTTS_TensorFlow_Integration % pytest tests/
======================================================== test session starts =========================================================
platform darwin -- Python 3.12.4, pytest-8.2.2, pluggy-1.5.0
rootdir: /Users/parker/Documents/dev/claude-engineer/_Projects/OpenTTS_TensorFlow_Integration
plugins: mock-3.14.0
collected 39 items                                                                                                                   

tests/test_base_tts.py .......                                                                                                 [ 17%]
tests/test_opentts_wrapper.py .FF......                                                                                        [ 41%]
tests/test_performance_optimizer.py ......                                                                                     [ 56%]
tests/test_tensorflow_tts_wrapper.py .F.......                                                                                 [ 79%]
tests/test_voice_selector.py ........                                                                                          [100%]

============================================================== FAILURES ==============================================================
__________________________________________________________ test_load_model ___________________________________________________________

mocker = <pytest_mock.plugin.MockerFixture object at 0x12df771a0>, mock_opentts = <MagicMock id='5042684368'>

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

self = <unittest.mock._patch object at 0x12c5ce000>

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

mocker = <pytest_mock.plugin.MockerFixture object at 0x12df9e5d0>, mock_opentts = <MagicMock id='5066319792'>

    def test_load_model_error(mocker, mock_opentts):
>       mocker.patch('src.opentts_tensorflow_integration.opentts.opentts_wrapper.opentts', mock_opentts)

tests/test_opentts_wrapper.py:27: 
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

self = <unittest.mock._patch object at 0x12df9e750>

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

mocker = <pytest_mock.plugin.MockerFixture object at 0x12e03bd10>, mock_tensorflow_tts = <MagicMock id='5066964192'>
mock_tf = <MagicMock id='5066321856'>

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

self = <unittest.mock._patch object at 0x12df9ef60>

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
============================================== 3 failed, 36 passed, 2 warnings in 4.51s ==============================================
(opentts+tensorflowtts-venv) parker@PxB-MBP-16 OpenTTS_TensorFlow_Integration % 
