import os
import sys

# Add the project root directory to the Python path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, project_root)

from src.opentts_tensorflow_integration import TTSEngine
from src.opentts_tensorflow_integration.utils.i18n import setup_i18n, _

def main():
    # Initialize internationalization
    setup_i18n('en')  # Use English for this example

    # Initialize the TTS engine
    tts_engine = TTSEngine()

    # Text to be converted to speech
    text = _("Hello, world! This is a basic text-to-speech conversion example.")

    print(_("Converting text to speech..."))
    
    # Generate speech
    audio = tts_engine.synthesize(text)

    # Save the audio to a file
    output_file = "output.wav"
    tts_engine.save_audio(audio, output_file)

    print(_("Speech generated and saved to {}").format(output_file))

if __name__ == "__main__":
    main()