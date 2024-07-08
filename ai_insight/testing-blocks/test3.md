(opentts+tensorflowtts-venv) parker@PxB-MBP-16 OpenTTS_TensorFlow_Integration %    cat /Users/parker/Documents/dev/claude-engineer/_Projects/OpenTTS_TensorFlow_Integration/locale/en/LC_MESSAGES/messages.po
# English translations for PACKAGE package.
# Copyright (C) 2024 THE PACKAGE'S COPYRIGHT HOLDER
# This file is distributed under the same license as the PACKAGE package.
# Parker Todd Brooks <parker@pxb-mbp-16.local>, 2024.
#
msgid ""
msgstr ""
"Project-Id-Version: PACKAGE VERSION\n"
"Report-Msgid-Bugs-To: \n"
"POT-Creation-Date: 2024-07-07 14:19-0700\n"
"PO-Revision-Date: 2024-07-07 14:25-0700\n"
"Last-Translator: Parker Todd Brooks <parker@pxb-mbp-16.local>\n"
"Language-Team: English\n"
"Language: en\n"
"MIME-Version: 1.0\n"
"Content-Type: text/plain; charset=UTF-8\n"
"Content-Transfer-Encoding: 8bit\n"
"Plural-Forms: nplurals=2; plural=(n != 1);\n"

#: src/opentts_tensorflow_integration/core/base_tts.py:21
msgid "Initialized {} with sample rate {}"
msgstr "Initialized {} with sample rate {}"

#: src/opentts_tensorflow_integration/core/base_tts.py:48
msgid "Normalized text: '{}' to '{}'"
msgstr "Normalized text: '{}' to '{}'"

#: src/opentts_tensorflow_integration/core/base_tts.py:51
msgid "Error normalizing text: {}"
msgstr "Error normalizing text: {}"

#: src/opentts_tensorflow_integration/core/base_tts.py:52
msgid "Failed to normalize text: {}"
msgstr "Failed to normalize text: {}"

#: src/opentts_tensorflow_integration/core/base_tts.py:65
msgid "Saved audio to {}"
msgstr "Saved audio to {}"

#: src/opentts_tensorflow_integration/core/base_tts.py:67
msgid "soundfile is required to save audio but not installed"
msgstr "soundfile is required to save audio but not installed"

#: src/opentts_tensorflow_integration/core/base_tts.py:68
msgid ""
"soundfile is required to save audio. Please install it with 'pip install "
"soundfile'."
msgstr ""
"soundfile is required to save audio. Please install it with 'pip install "
"soundfile'."

#: src/opentts_tensorflow_integration/core/base_tts.py:70
msgid "Error saving audio: {}"
msgstr "Error saving audio: {}"

#: src/opentts_tensorflow_integration/core/base_tts.py:71
msgid "Failed to save audio: {}"
msgstr "Failed to save audio: {}"

#: src/opentts_tensorflow_integration/core/performance_optimizer.py:109
msgid "{:.2f}%"
msgstr "{:.2f}%"

#: src/opentts_tensorflow_integration/core/voice_selector.py:46
#: src/opentts_tensorflow_integration/core/voice_selector.py:60
msgid "Engine '{}' not found."
msgstr "Engine '{}' not found."

#: src/opentts_tensorflow_integration/core/voice_selector.py:64
msgid "Voice '{}' not found in engine '{}'."
msgstr "Voice '{}' not found in engine '{}'."

#: src/opentts_tensorflow_integration/core/voice_selector.py:93
msgid "No voice selected. Please select a voice first."
msgstr "No voice selected. Please select a voice first."

#: src/opentts_tensorflow_integration/opentts/opentts_wrapper.py:20
msgid "Initialized OpenTTSWrapper"
msgstr "Initialized OpenTTSWrapper"

#: src/opentts_tensorflow_integration/opentts/opentts_wrapper.py:32
msgid "Loaded OpenTTS model from {}"
msgstr "Loaded OpenTTS model from {}"

#: src/opentts_tensorflow_integration/opentts/opentts_wrapper.py:34
msgid "OpenTTS is not installed"
msgstr "OpenTTS is not installed"

#: src/opentts_tensorflow_integration/opentts/opentts_wrapper.py:35
msgid "OpenTTS is not installed. Please install it with 'pip install opentts'."
msgstr ""
"OpenTTS is not installed. Please install it with 'pip install opentts'."

#: src/opentts_tensorflow_integration/opentts/opentts_wrapper.py:37
#: src/opentts_tensorflow_integration/opentts/opentts_wrapper.py:38
msgid "Failed to load OpenTTS model: {}"
msgstr "Failed to load OpenTTS model: {}"

#: src/opentts_tensorflow_integration/opentts/opentts_wrapper.py:51
#: src/opentts_tensorflow_integration/opentts/opentts_wrapper.py:72
#: src/opentts_tensorflow_integration/opentts/opentts_wrapper.py:91
msgid "OpenTTS engine is not initialized"
msgstr "OpenTTS engine is not initialized"

#: src/opentts_tensorflow_integration/opentts/opentts_wrapper.py:52
#: src/opentts_tensorflow_integration/opentts/opentts_wrapper.py:73
#: src/opentts_tensorflow_integration/opentts/opentts_wrapper.py:92
msgid "OpenTTS engine is not initialized. Please call load_model() first."
msgstr "OpenTTS engine is not initialized. Please call load_model() first."

#: src/opentts_tensorflow_integration/opentts/opentts_wrapper.py:56
#: src/opentts_tensorflow_integration/tensorflow_tts/tensorflow_tts_wrapper.py:61
msgid "Synthesizing text: '{}'"
msgstr "Synthesizing text: '{}'"

#: src/opentts_tensorflow_integration/opentts/opentts_wrapper.py:60
#: src/opentts_tensorflow_integration/tensorflow_tts/tensorflow_tts_wrapper.py:72
msgid "Error during speech synthesis: {}"
msgstr "Error during speech synthesis: {}"

#: src/opentts_tensorflow_integration/opentts/opentts_wrapper.py:61
#: src/opentts_tensorflow_integration/tensorflow_tts/tensorflow_tts_wrapper.py:73
msgid "Failed to synthesize speech: {}"
msgstr "Failed to synthesize speech: {}"

#: src/opentts_tensorflow_integration/opentts/opentts_wrapper.py:77
msgid "Available voices: {}"
msgstr "Available voices: {}"

#: src/opentts_tensorflow_integration/opentts/opentts_wrapper.py:80
msgid "Error retrieving available voices: {}"
msgstr "Error retrieving available voices: {}"

#: src/opentts_tensorflow_integration/opentts/opentts_wrapper.py:81
msgid "Failed to retrieve available voices: {}"
msgstr "Failed to retrieve available voices: {}"

#: src/opentts_tensorflow_integration/opentts/opentts_wrapper.py:96
msgid "Voice '{}' is not available in OpenTTS."
msgstr "Voice '{}' is not available in OpenTTS."

#: src/opentts_tensorflow_integration/opentts/opentts_wrapper.py:100
#: src/opentts_tensorflow_integration/tensorflow_tts/tensorflow_tts_wrapper.py:102
msgid "Set current voice to '{}'"
msgstr "Set current voice to '{}'"

#: src/opentts_tensorflow_integration/opentts/opentts_wrapper.py:105
#: src/opentts_tensorflow_integration/tensorflow_tts/tensorflow_tts_wrapper.py:107
msgid "Error setting voice: {}"
msgstr "Error setting voice: {}"

#: src/opentts_tensorflow_integration/opentts/opentts_wrapper.py:106
#: src/opentts_tensorflow_integration/tensorflow_tts/tensorflow_tts_wrapper.py:108
msgid "Failed to set voice: {}"
msgstr "Failed to set voice: {}"

#: src/opentts_tensorflow_integration/tensorflow_tts/tensorflow_tts_wrapper.py:23
msgid "Initialized TensorFlowTTSWrapper"
msgstr "Initialized TensorFlowTTSWrapper"

#: src/opentts_tensorflow_integration/tensorflow_tts/tensorflow_tts_wrapper.py:37
msgid "Loaded TensorFlow TTS model from {}"
msgstr "Loaded TensorFlow TTS model from {}"

#: src/opentts_tensorflow_integration/tensorflow_tts/tensorflow_tts_wrapper.py:39
msgid "TensorFlow TTS is not installed"
msgstr "TensorFlow TTS is not installed"

#: src/opentts_tensorflow_integration/tensorflow_tts/tensorflow_tts_wrapper.py:40
msgid ""
"TensorFlow TTS is not installed. Please install it with 'pip install "
"TensorFlowTTS'."
msgstr ""
"TensorFlow TTS is not installed. Please install it with 'pip install "
"TensorFlowTTS'."

#: src/opentts_tensorflow_integration/tensorflow_tts/tensorflow_tts_wrapper.py:42
#: src/opentts_tensorflow_integration/tensorflow_tts/tensorflow_tts_wrapper.py:43
msgid "Failed to load TensorFlow TTS model: {}"
msgstr "Failed to load TensorFlow TTS model: {}"

#: src/opentts_tensorflow_integration/tensorflow_tts/tensorflow_tts_wrapper.py:56
msgid "TensorFlow TTS model is not initialized"
msgstr "TensorFlow TTS model is not initialized"

#: src/opentts_tensorflow_integration/tensorflow_tts/tensorflow_tts_wrapper.py:57
msgid ""
"TensorFlow TTS model is not initialized. Please call load_model() first."
msgstr ""
"TensorFlow TTS model is not initialized. Please call load_model() first."

#: src/opentts_tensorflow_integration/tensorflow_tts/tensorflow_tts_wrapper.py:85
msgid "Retrieving available voices for TensorFlow TTS"
msgstr "Retrieving available voices for TensorFlow TTS"

#: src/opentts_tensorflow_integration/tensorflow_tts/tensorflow_tts_wrapper.py:97
msgid "Voice '{}' is not available in TensorFlow TTS."
msgstr "Voice '{}' is not available in TensorFlow TTS."

#: src/opentts_tensorflow_integration/tensorflow_tts/tensorflow_tts_wrapper.py:122
msgid "Vocoder not implemented"
msgstr "Vocoder not implemented"

#: src/opentts_tensorflow_integration/tensorflow_tts/tensorflow_tts_wrapper.py:123
msgid ""
"Vocoder not implemented. Please implement this method using your chosen "
"vocoder."
msgstr ""
"Vocoder not implemented. Please implement this method using your chosen "
"vocoder."
(opentts+tensorflowtts-venv) parker@PxB-MBP-16 OpenTTS_TensorFlow_Integration % 
