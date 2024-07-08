import os
import sys
import time

# Add the project root directory to the Python path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, project_root)

from src.opentts_tensorflow_integration import TTSEngine, VoiceSelector, PerformanceOptimizer
from src.opentts_tensorflow_integration.utils.i18n import setup_i18n, _

def main():
    # Initialize internationalization
    setup_i18n('en')  # Use English for this example

    # Initialize the TTS engine and voice selector
    tts_engine = TTSEngine()
    voice_selector = VoiceSelector()
    voice_selector.add_engine("OpenTTS", tts_engine.opentts_engine)

    # Initialize the performance optimizer
    optimizer = PerformanceOptimizer(cache_size=5)

    # Select a voice
    voice_selector.select_voice("OpenTTS", "default")  # Assume 'default' voice exists

    # Prepare a list of texts to synthesize
    texts = [
        _("This is the first sentence."),
        _("Here's another sentence to synthesize."),
        _("Let's repeat the first sentence."),
        _("This is the first sentence."),
        _("And here's a new, unique sentence."),
    ]

    print(_("Synthesizing without performance optimization:"))
    start_time = time.time()
    for text in texts:
        result = voice_selector.synthesize(text)
        print(f"Synthesized: '{text}'")
    end_time = time.time()
    print(_("Time taken without optimization: {:.2f} seconds").format(end_time - start_time))

    print(_("\nSynthesizing with performance optimization:"))
    start_time = time.time()
    results = optimizer.batch_process(voice_selector.engines["OpenTTS"], texts)
    for text, audio in zip(texts, results):
        print(f"Synthesized: '{text}'")
    end_time = time.time()
    print(_("Time taken with optimization: {:.2f} seconds").format(end_time - start_time))

    # Print cache statistics
    cache_stats = optimizer.get_cache_stats()
    print(_("\nCache statistics:"))
    print(f"Cache size: {cache_stats['cache_size']}")
    print(f"Max cache size: {cache_stats['max_cache_size']}")
    print(f"Cache usage: {cache_stats['cache_usage']}")

if __name__ == "__main__":
    main()