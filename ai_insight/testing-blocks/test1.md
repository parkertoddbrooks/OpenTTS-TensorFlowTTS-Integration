(opentts+tensorflowtts-venv) parker@PxB-MBP-16 OpenTTS_TensorFlow_Integration % cat locale/messages.pot
# SOME DESCRIPTIVE TITLE.
# Copyright (C) YEAR THE PACKAGE'S COPYRIGHT HOLDER
# This file is distributed under the same license as the PACKAGE package.
# FIRST AUTHOR <EMAIL@ADDRESS>, YEAR.
#
#, fuzzy
msgid ""
msgstr ""
"Project-Id-Version: PACKAGE VERSION\n"
"Report-Msgid-Bugs-To: \n"
"POT-Creation-Date: 2024-07-07 14:19-0700\n"
"PO-Revision-Date: YEAR-MO-DA HO:MI+ZONE\n"
"Last-Translator: FULL NAME <EMAIL@ADDRESS>\n"
"Language-Team: LANGUAGE <LL@li.org>\n"
"Language: \n"
"MIME-Version: 1.0\n"
"Content-Type: text/plain; charset=CHARSET\n"
"Content-Transfer-Encoding: 8bit\n"

#: src/opentts_tensorflow_integration/core/base_tts.py:21
msgid "Initialized {} with sample rate {}"
msgstr ""

#: src/opentts_tensorflow_integration/core/base_tts.py:48
msgid "Normalized text: '{}' to '{}'"
msgstr ""

#: src/opentts_tensorflow_integration/core/base_tts.py:51
msgid "Error normalizing text: {}"
msgstr ""

#: src/opentts_tensorflow_integration/core/base_tts.py:52
msgid "Failed to normalize text: {}"
msgstr ""

#: src/opentts_tensorflow_integration/core/base_tts.py:65
msgid "Saved audio to {}"
msgstr ""

#: src/opentts_tensorflow_integration/core/base_tts.py:67
msgid "soundfile is required to save audio but not installed"
msgstr ""

#: src/opentts_tensorflow_integration/core/base_tts.py:68
msgid ""
"soundfile is required to save audio. Please install it with 'pip install "
"soundfile'."
msgstr ""

#: src/opentts_tensorflow_integration/core/base_tts.py:70
msgid "Error saving audio: {}"
msgstr ""

#: src/opentts_tensorflow_integration/core/base_tts.py:71
msgid "Failed to save audio: {}"
msgstr ""

#: src/opentts_tensorflow_integration/core/performance_optimizer.py:109
msgid "{:.2f}%"
msgstr ""

#: src/opentts_tensorflow_integration/core/voice_selector.py:46
#: src/opentts_tensorflow_integration/core/voice_selector.py:60
msgid "Engine '{}' not found."
msgstr ""

#: src/opentts_tensorflow_integration/core/voice_selector.py:64
msgid "Voice '{}' not found in engine '{}'."
msgstr ""

#: src/opentts_tensorflow_integration/core/voice_selector.py:93
msgid "No voice selected. Please select a voice first."
msgstr ""

#: src/opentts_tensorflow_integration/opentts/opentts_wrapper.py:20
msgid "Initialized OpenTTSWrapper"
msgstr ""

#: src/opentts_tensorflow_integration/opentts/opentts_wrapper.py:32
msgid "Loaded OpenTTS model from {}"
msgstr ""

#: src/opentts_tensorflow_integration/opentts/opentts_wrapper.py:34
msgid "OpenTTS is not installed"
msgstr ""

#: src/opentts_tensorflow_integration/opentts/opentts_wrapper.py:35
msgid "OpenTTS is not installed. Please install it with 'pip install opentts'."
msgstr ""

#: src/opentts_tensorflow_integration/opentts/opentts_wrapper.py:37
#: src/opentts_tensorflow_integration/opentts/opentts_wrapper.py:38
msgid "Failed to load OpenTTS model: {}"
msgstr ""

#: src/opentts_tensorflow_integration/opentts/opentts_wrapper.py:51
#: src/opentts_tensorflow_integration/opentts/opentts_wrapper.py:72
#: src/opentts_tensorflow_integration/opentts/opentts_wrapper.py:91
msgid "OpenTTS engine is not initialized"
msgstr ""

#: src/opentts_tensorflow_integration/opentts/opentts_wrapper.py:52
#: src/opentts_tensorflow_integration/opentts/opentts_wrapper.py:73
#: src/opentts_tensorflow_integration/opentts/opentts_wrapper.py:92
msgid "OpenTTS engine is not initialized. Please call load_model() first."
msgstr ""

#: src/opentts_tensorflow_integration/opentts/opentts_wrapper.py:56
#: src/opentts_tensorflow_integration/tensorflow_tts/tensorflow_tts_wrapper.py:61
msgid "Synthesizing text: '{}'"
msgstr ""

#: src/opentts_tensorflow_integration/opentts/opentts_wrapper.py:60
#: src/opentts_tensorflow_integration/tensorflow_tts/tensorflow_tts_wrapper.py:72
msgid "Error during speech synthesis: {}"
msgstr ""

#: src/opentts_tensorflow_integration/opentts/opentts_wrapper.py:61
#: src/opentts_tensorflow_integration/tensorflow_tts/tensorflow_tts_wrapper.py:73
msgid "Failed to synthesize speech: {}"
msgstr ""

#: src/opentts_tensorflow_integration/opentts/opentts_wrapper.py:77
msgid "Available voices: {}"
msgstr ""

#: src/opentts_tensorflow_integration/opentts/opentts_wrapper.py:80
msgid "Error retrieving available voices: {}"
msgstr ""

#: src/opentts_tensorflow_integration/opentts/opentts_wrapper.py:81
msgid "Failed to retrieve available voices: {}"
msgstr ""

#: src/opentts_tensorflow_integration/opentts/opentts_wrapper.py:96
msgid "Voice '{}' is not available in OpenTTS."
msgstr ""

#: src/opentts_tensorflow_integration/opentts/opentts_wrapper.py:100
#: src/opentts_tensorflow_integration/tensorflow_tts/tensorflow_tts_wrapper.py:102
msgid "Set current voice to '{}'"
msgstr ""

#: src/opentts_tensorflow_integration/opentts/opentts_wrapper.py:105
#: src/opentts_tensorflow_integration/tensorflow_tts/tensorflow_tts_wrapper.py:107
msgid "Error setting voice: {}"
msgstr ""

#: src/opentts_tensorflow_integration/opentts/opentts_wrapper.py:106
#: src/opentts_tensorflow_integration/tensorflow_tts/tensorflow_tts_wrapper.py:108
msgid "Failed to set voice: {}"
msgstr ""

#: src/opentts_tensorflow_integration/tensorflow_tts/tensorflow_tts_wrapper.py:23
msgid "Initialized TensorFlowTTSWrapper"
msgstr ""

#: src/opentts_tensorflow_integration/tensorflow_tts/tensorflow_tts_wrapper.py:37
msgid "Loaded TensorFlow TTS model from {}"
msgstr ""

#: src/opentts_tensorflow_integration/tensorflow_tts/tensorflow_tts_wrapper.py:39
msgid "TensorFlow TTS is not installed"
msgstr ""

#: src/opentts_tensorflow_integration/tensorflow_tts/tensorflow_tts_wrapper.py:40
msgid ""
"TensorFlow TTS is not installed. Please install it with 'pip install "
"TensorFlowTTS'."
msgstr ""

#: src/opentts_tensorflow_integration/tensorflow_tts/tensorflow_tts_wrapper.py:42
#: src/opentts_tensorflow_integration/tensorflow_tts/tensorflow_tts_wrapper.py:43
msgid "Failed to load TensorFlow TTS model: {}"
msgstr ""

#: src/opentts_tensorflow_integration/tensorflow_tts/tensorflow_tts_wrapper.py:56
msgid "TensorFlow TTS model is not initialized"
msgstr ""

#: src/opentts_tensorflow_integration/tensorflow_tts/tensorflow_tts_wrapper.py:57
msgid ""
"TensorFlow TTS model is not initialized. Please call load_model() first."
msgstr ""

#: src/opentts_tensorflow_integration/tensorflow_tts/tensorflow_tts_wrapper.py:85
msgid "Retrieving available voices for TensorFlow TTS"
msgstr ""

#: src/opentts_tensorflow_integration/tensorflow_tts/tensorflow_tts_wrapper.py:97
msgid "Voice '{}' is not available in TensorFlow TTS."
msgstr ""

#: src/opentts_tensorflow_integration/tensorflow_tts/tensorflow_tts_wrapper.py:122
msgid "Vocoder not implemented"
msgstr ""

#: src/opentts_tensorflow_integration/tensorflow_tts/tensorflow_tts_wrapper.py:123
msgid ""
"Vocoder not implemented. Please implement this method using your chosen "
"vocoder."
msgstr ""
(opentts+tensorflowtts-venv) parker@PxB-MBP-16 OpenTTS_TensorFlow_Integration % 