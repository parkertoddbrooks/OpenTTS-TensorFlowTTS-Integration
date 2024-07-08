(opentts+tensorflowtts-venv) parker@PxB-MBP-16 OpenTTS_TensorFlow_Integration % pytest tests/
======================================================== test session starts =========================================================
platform darwin -- Python 3.12.4, pytest-8.2.2, pluggy-1.5.0
rootdir: /Users/parker/Documents/dev/claude-engineer/_Projects/OpenTTS_TensorFlow_Integration
plugins: mock-3.14.0
collected 40 items                                                                                                                   

tests/test_base_tts.py .......                                                                                                 [ 17%]
tests/test_opentts_wrapper.py ..........                                                                                       [ 42%]
tests/test_performance_optimizer.py ......                                                                                     [ 57%]
tests/test_tensorflow_tts_wrapper.py .........                                                                                 [ 80%]
tests/test_voice_selector.py ........                                                                                          [100%]

========================================================== warnings summary ==========================================================
<frozen importlib._bootstrap>:488
  <frozen importlib._bootstrap>:488: DeprecationWarning: Type google._upb._message.MessageMapContainer uses PyType_Spec with a metaclass that has custom tp_new. This is deprecated and will no longer be allowed in Python 3.14.

<frozen importlib._bootstrap>:488
  <frozen importlib._bootstrap>:488: DeprecationWarning: Type google._upb._message.ScalarMapContainer uses PyType_Spec with a metaclass that has custom tp_new. This is deprecated and will no longer be allowed in Python 3.14.

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
=================================================== 40 passed, 2 warnings in 3.54s ===================================================
(opentts+tensorflowtts-venv) parker@PxB-MBP-16 OpenTTS_TensorFlow_Integration % 

