(opentts+tensorflowtts-venv) parker@PxB-MBP-16 OpenTTS_TensorFlow_Integration % pytest tests/
=================================================== test session starts ===================================================
platform darwin -- Python 3.12.4, pytest-8.2.2, pluggy-1.5.0
rootdir: /Users/parker/Documents/dev/claude-engineer/_Projects/OpenTTS_TensorFlow_Integration
collected 0 items / 5 errors                                                                                              

========================================================= ERRORS ==========================================================
_________________________________________ ERROR collecting tests/test_base_tts.py _________________________________________
ImportError while importing test module '/Users/parker/Documents/dev/claude-engineer/_Projects/OpenTTS_TensorFlow_Integration/tests/test_base_tts.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/usr/local/Cellar/python@3.12/3.12.4/Frameworks/Python.framework/Versions/3.12/lib/python3.12/importlib/__init__.py:90: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
tests/test_base_tts.py:3: in <module>
    from src.opentts_tensorflow_integration.core import BaseTTS
E   ModuleNotFoundError: No module named 'src'
_____________________________________ ERROR collecting tests/test_opentts_wrapper.py ______________________________________
ImportError while importing test module '/Users/parker/Documents/dev/claude-engineer/_Projects/OpenTTS_TensorFlow_Integration/tests/test_opentts_wrapper.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/usr/local/Cellar/python@3.12/3.12.4/Frameworks/Python.framework/Versions/3.12/lib/python3.12/importlib/__init__.py:90: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
tests/test_opentts_wrapper.py:4: in <module>
    from src.opentts_tensorflow_integration.opentts import OpenTTSWrapper
E   ModuleNotFoundError: No module named 'src'
__________________________________ ERROR collecting tests/test_performance_optimizer.py ___________________________________
ImportError while importing test module '/Users/parker/Documents/dev/claude-engineer/_Projects/OpenTTS_TensorFlow_Integration/tests/test_performance_optimizer.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/usr/local/Cellar/python@3.12/3.12.4/Frameworks/Python.framework/Versions/3.12/lib/python3.12/importlib/__init__.py:90: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
tests/test_performance_optimizer.py:4: in <module>
    from src.opentts_tensorflow_integration.core import PerformanceOptimizer, BaseTTS
E   ModuleNotFoundError: No module named 'src'
__________________________________ ERROR collecting tests/test_tensorflow_tts_wrapper.py __________________________________
ImportError while importing test module '/Users/parker/Documents/dev/claude-engineer/_Projects/OpenTTS_TensorFlow_Integration/tests/test_tensorflow_tts_wrapper.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/usr/local/Cellar/python@3.12/3.12.4/Frameworks/Python.framework/Versions/3.12/lib/python3.12/importlib/__init__.py:90: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
tests/test_tensorflow_tts_wrapper.py:5: in <module>
    from src.opentts_tensorflow_integration.tensorflow_tts import TensorFlowTTSWrapper
E   ModuleNotFoundError: No module named 'src'
----------------------------------------------------- Captured stderr -----------------------------------------------------
2024-07-07 16:55:31.542970: I tensorflow/core/platform/cpu_feature_guard.cc:210] This TensorFlow binary is optimized to use available CPU instructions in performance-critical operations.
To enable the following instructions: AVX2 FMA, in other operations, rebuild TensorFlow with the appropriate compiler flags.
______________________________________ ERROR collecting tests/test_voice_selector.py ______________________________________
ImportError while importing test module '/Users/parker/Documents/dev/claude-engineer/_Projects/OpenTTS_TensorFlow_Integration/tests/test_voice_selector.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/usr/local/Cellar/python@3.12/3.12.4/Frameworks/Python.framework/Versions/3.12/lib/python3.12/importlib/__init__.py:90: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
tests/test_voice_selector.py:3: in <module>
    from src.opentts_tensorflow_integration.core import VoiceSelector
E   ModuleNotFoundError: No module named 'src'
==================================================== warnings summary =====================================================
<frozen importlib._bootstrap>:488
  <frozen importlib._bootstrap>:488: DeprecationWarning: Type google._upb._message.MessageMapContainer uses PyType_Spec with a metaclass that has custom tp_new. This is deprecated and will no longer be allowed in Python 3.14.

<frozen importlib._bootstrap>:488
  <frozen importlib._bootstrap>:488: DeprecationWarning: Type google._upb._message.ScalarMapContainer uses PyType_Spec with a metaclass that has custom tp_new. This is deprecated and will no longer be allowed in Python 3.14.

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
================================================= short test summary info =================================================
ERROR tests/test_base_tts.py
ERROR tests/test_opentts_wrapper.py
ERROR tests/test_performance_optimizer.py
ERROR tests/test_tensorflow_tts_wrapper.py
ERROR tests/test_voice_selector.py
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! Interrupted: 5 errors during collection !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
============================================= 2 warnings, 5 errors in 41.81s ==============================================
(opentts+tensorflowtts-venv) parker@PxB-MBP-16 OpenTTS_TensorFlow_Integration %  

