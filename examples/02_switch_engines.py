import os
import sys

# Add the project root directory to the Python path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, project_root)

from src.opentts_tensorflow_integration import TTSEngine, VoiceSelector
from src.opentts_tensorflow_integration.utils.i18n import setup_i18n, _

def main():
    # Initialize internationalization
    setup_i18n('en')  # Use English for this example

    # Initialize the TTS engine
    tts_engine = TTSEngine()

    # Create a voice selector and add engines
    voice_selector = VoiceSelector()
    voice_selector.add_engine("OpenTTS", tts_engine.opentts_engine)
    voice_selector.add_engine("TensorFlowTTS", tts_engine.tensorflow_tts_engine)

    # Text to be converted to speech
    text = _("This is an example of switching between different TTS engines.")

    # List available engines
    print(_("Available engines:"))
    for engine in voice_selector.list_engines():
        print(f"- {engine}")

    # Synthesize using OpenTTS
    print(_("\nSynthesizing with OpenTTS:"))
    voice_selector.select_voice("OpenTTS", "default")  # Assume 'default' voice exists
    result = voice_selector.synthesize(text)
    tts_engine.save_audio(result['audio'], "output_opentts.wav")
    print(_("Audio saved to output_opentts.wav"))

    # Synthesize using TensorFlow TTS
    print(_("\nSynthesizing with TensorFlow TTS:"))
    voice_selector.select_voice("TensorFlowTTS", "default")  # Assume 'default' voice exists
    result = voice_selector.synthesize(text)
    tts_engine.save_audio(result['audio'], "output_tensorflow.wav")
    print(_("Audio saved to output_tensorflow.wav"))

if __name__ == "__main__":
    main()