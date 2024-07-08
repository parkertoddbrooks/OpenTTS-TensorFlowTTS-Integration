(opentts+tensorflowtts-venv) parker@PxB-MBP-16 OpenTTS_TensorFlow_Integration % pytest tests/
======================================================== test session starts =========================================================
platform darwin -- Python 3.12.4, pytest-8.2.2, pluggy-1.5.0
rootdir: /Users/parker/Documents/dev/claude-engineer/_Projects/OpenTTS_TensorFlow_Integration
plugins: mock-3.14.0
collected 40 items                                                                                                                   

tests/test_base_tts.py .......                                                                                                 [ 17%]
tests/test_opentts_wrapper.py ..........                                                                                       [ 42%]
tests/test_performance_optimizer.py ......                                                                                     [ 57%]
tests/test_tensorflow_tts_wrapper.py .F.......                                                                                 [ 80%]
tests/test_voice_selector.py ........                                                                                          [100%]

============================================================== FAILURES ==============================================================
__________________________________________________________ test_load_model ___________________________________________________________

self = <src.opentts_tensorflow_integration.tensorflow_tts.tensorflow_tts_wrapper.TensorFlowTTSWrapper object at 0x12a141340>
model_path = 'path/to/model'

    def load_model(self, model_path: str):
        """
        Load TensorFlow TTS model.
    
        Args:
            model_path (str): Path to the TensorFlow TTS model.
        """
        try:
            import tensorflow_tts
>           self.model = tf.saved_model.load(model_path)

src/opentts_tensorflow_integration/tensorflow_tts/tensorflow_tts_wrapper.py:34: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
../../../venvs/opentts+tensorflowtts-venv/lib/python3.12/site-packages/tensorflow/python/saved_model/load.py:912: in load
    result = load_partial(export_dir, None, tags, options)["root"]
../../../venvs/opentts+tensorflowtts-venv/lib/python3.12/site-packages/tensorflow/python/saved_model/load.py:1016: in load_partial
    loader_impl.parse_saved_model_with_debug_info(export_dir))
../../../venvs/opentts+tensorflowtts-venv/lib/python3.12/site-packages/tensorflow/python/saved_model/loader_impl.py:59: in parse_saved_model_with_debug_info
    saved_model = parse_saved_model(export_dir)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

export_dir = 'path/to/model'

    @tf_export("__internal__.saved_model.parse_saved_model", v1=[])
    def parse_saved_model(export_dir):
      """Reads the savedmodel.pb or savedmodel.pbtxt file containing `SavedModel`.
    
      Args:
        export_dir: String or Pathlike, path to the directory containing the
        SavedModel file.
    
      Returns:
        A `SavedModel` protocol buffer.
    
      Raises:
        IOError: If the file does not exist, or cannot be successfully parsed.
      """
      # Build the path to the SavedModel in pbtxt format.
      path_to_pbtxt = file_io.join(
          compat.as_bytes(compat.path_to_str(export_dir)),
          compat.as_bytes(constants.SAVED_MODEL_FILENAME_PBTXT))
      # Build the path to the SavedModel in pb format.
      path_to_pb = file_io.join(
          compat.as_bytes(compat.path_to_str(export_dir)),
          compat.as_bytes(constants.SAVED_MODEL_FILENAME_PB))
      # Build the path to the SavedModel in cpb format.
      path_to_cpb = file_io.join(
          compat.as_bytes(compat.path_to_str(export_dir)),
          compat.as_bytes(constants.SAVED_MODEL_FILENAME_CPB))
    
      # Parse the SavedModel protocol buffer.
      saved_model = saved_model_pb2.SavedModel()
      if file_io.file_exists(path_to_pb):
        with file_io.FileIO(path_to_pb, "rb") as f:
          file_content = f.read()
        try:
          saved_model.ParseFromString(file_content)
        except message.DecodeError as e:
          raise IOError(f"Cannot parse file {path_to_pb}: {str(e)}.") from e
      elif file_io.file_exists(path_to_pbtxt):
        with file_io.FileIO(path_to_pbtxt, "rb") as f:
          file_content = f.read()
        try:
          text_format.Parse(file_content.decode("utf-8"), saved_model)
        except text_format.ParseError as e:
          raise IOError(f"Cannot parse file {path_to_pbtxt}: {str(e)}.") from e
      else:
>       raise IOError(
            f"SavedModel file does not exist at: {export_dir}{os.path.sep}"
            f"{{{constants.SAVED_MODEL_FILENAME_PBTXT}|"
            f"{constants.SAVED_MODEL_FILENAME_PB}}}")
E       OSError: SavedModel file does not exist at: path/to/model/{saved_model.pbtxt|saved_model.pb}

../../../venvs/opentts+tensorflowtts-venv/lib/python3.12/site-packages/tensorflow/python/saved_model/loader_impl.py:119: OSError

During handling of the above exception, another exception occurred:

mock_tensorflow_tts = <MagicMock id='5000815168'>, mock_tf = <MagicMock id='5000874512'>

    def test_load_model(mock_tensorflow_tts, mock_tf):
        with patch('builtins.__import__', side_effect=[mock_tensorflow_tts, mock_tf]):
            wrapper = TensorFlowTTSWrapper()
>           wrapper.load_model("path/to/model")

tests/test_tensorflow_tts_wrapper.py:29: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <src.opentts_tensorflow_integration.tensorflow_tts.tensorflow_tts_wrapper.TensorFlowTTSWrapper object at 0x12a141340>
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
            raise ImportError(_("TensorFlow TTS is not installed. Please install it with 'pip install TensorFlowTTS'."))
        except Exception as e:
            log_error(_("Failed to load TensorFlow TTS model: {}").format(str(e)))
>           raise ModelNotFoundError(_("Failed to load TensorFlow TTS model: {}").format(str(e)))
E           src.opentts_tensorflow_integration.utils.logging_utils.ModelNotFoundError: Failed to load TensorFlow TTS model: SavedModel file does not exist at: path/to/model/{saved_model.pbtxt|saved_model.pb}

src/opentts_tensorflow_integration/tensorflow_tts/tensorflow_tts_wrapper.py:43: ModelNotFoundError
-------------------------------------------------------- Captured stderr call --------------------------------------------------------
2024-07-07 21:32:24,706 - opentts_tensorflow_integration - INFO - Initialized TensorFlowTTSWrapper with sample rate 22050
2024-07-07 21:32:24,706 - opentts_tensorflow_integration - INFO - Initialized TensorFlowTTSWrapper
2024-07-07 21:32:24,706 - opentts_tensorflow_integration - ERROR - str: Failed to load TensorFlow TTS model: SavedModel file does not exist at: path/to/model/{saved_model.pbtxt|saved_model.pb}
--------------------------------------------------------- Captured log call ----------------------------------------------------------
INFO     opentts_tensorflow_integration:logging_utils.py:78 Initialized TensorFlowTTSWrapper with sample rate 22050
INFO     opentts_tensorflow_integration:logging_utils.py:78 Initialized TensorFlowTTSWrapper
ERROR    opentts_tensorflow_integration:logging_utils.py:60 str: Failed to load TensorFlow TTS model: SavedModel file does not exist at: path/to/model/{saved_model.pbtxt|saved_model.pb}
========================================================== warnings summary ==========================================================
<frozen importlib._bootstrap>:488
  <frozen importlib._bootstrap>:488: DeprecationWarning: Type google._upb._message.MessageMapContainer uses PyType_Spec with a metaclass that has custom tp_new. This is deprecated and will no longer be allowed in Python 3.14.

<frozen importlib._bootstrap>:488
  <frozen importlib._bootstrap>:488: DeprecationWarning: Type google._upb._message.ScalarMapContainer uses PyType_Spec with a metaclass that has custom tp_new. This is deprecated and will no longer be allowed in Python 3.14.

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
====================================================== short test summary info =======================================================
FAILED tests/test_tensorflow_tts_wrapper.py::test_load_model - src.opentts_tensorflow_integration.utils.logging_utils.ModelNotFoundError: Failed to load TensorFlow TTS model: SavedModel file d...
============================================== 1 failed, 39 passed, 2 warnings in 3.77s ==============================================
(opentts+tensorflowtts-venv) parker@PxB-MBP-16 OpenTTS_TensorFlow_Integration % 

