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

    # Text to be converted to speech
    text = _("This is an example of changing voices for text-to-speech conversion.")

    # List available voices
    print(_("Available voices:"))
    voices = voice_selector.list_voices("OpenTTS")
    for voice in voices["OpenTTS"]:
        print(f"- {voice}")

    # Synthesize using different voices
    for voice in voices["OpenTTS"][:2]:  # Use the first two voices as examples
        print(f"\n{_('Synthesizing with voice')} '{voice}':")
        voice_selector.select_voice("OpenTTS", voice)
        result = voice_selector.synthesize(text)
        output_file = f"output_{voice}.wav"
        tts_engine.save_audio(result['audio'], output_file)
        print(_("Audio saved to {}").format(output_file))

    # Get current voice
    current_voice = voice_selector.get_current_voice()
    print(f"\n{_('Current voice')}: {current_voice['engine']} - {current_voice['voice']}")

if __name__ == "__main__":
    main()