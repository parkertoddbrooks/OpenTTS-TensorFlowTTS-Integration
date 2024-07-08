import os
import sys

# Add the project root directory to the Python path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, project_root)

from src.opentts_tensorflow_integration import TTSEngine, VoiceSelector
from src.opentts_tensorflow_integration.utils.i18n import setup_i18n, change_language, get_current_language, _

def display_info(tts_engine, voice_selector):
    print(_("Current language: {}").format(get_current_language()))
    print(_("Available engines:"))
    for engine in voice_selector.list_engines():
        print(f"- {engine}")
    print(_("Available voices:"))
    voices = voice_selector.list_voices()
    for engine, voice_list in voices.items():
        print(f"{engine}:")
        for voice in voice_list:
            print(f"  - {voice}")

def main():
    # Initialize the TTS engine and voice selector
    tts_engine = TTSEngine()
    voice_selector = VoiceSelector()
    voice_selector.add_engine("OpenTTS", tts_engine.opentts_engine)
    voice_selector.add_engine("TensorFlowTTS", tts_engine.tensorflow_tts_engine)

    # Example in English
    setup_i18n('en')
    print(_("Example in English:"))
    display_info(tts_engine, voice_selector)
    
    text_en = _("This is an example of changing languages for internationalization.")
    voice_selector.select_voice("OpenTTS", "default")  # Assume 'default' voice exists
    result = voice_selector.synthesize(text_en)
    tts_engine.save_audio(result['audio'], "output_en.wav")
    print(_("English audio saved to output_en.wav"))

    print("\n" + "="*50 + "\n")

    # Example in Spanish
    change_language('es')
    print(_("Example in Spanish:"))
    display_info(tts_engine, voice_selector)
    
    text_es = _("This is an example of changing languages for internationalization.")
    voice_selector.select_voice("OpenTTS", "default")  # Assume 'default' voice exists
    result = voice_selector.synthesize(text_es)
    tts_engine.save_audio(result['audio'], "output_es.wav")
    print(_("Spanish audio saved to output_es.wav"))

if __name__ == "__main__":
    main()