# OpenTTS TensorFlow Integration Documentation

## Table of Contents

1. [Introduction](#introduction)
2. [Development Status](#development-status)
3. [Installation & Requirements](#installation--requirements)
4. [Usage](#usage)
5. [API Reference](#api-reference)
6. [Configuration](#configuration)
7. [Internationalization](#internationalization)
8. [Performance Optimization](#performance-optimization)
9. [Testing](#testing)
10. [Troubleshooting](#troubleshooting)
11. [Contributing](#contributing)

## Introduction

OpenTTS TensorFlowTTS Integration is a library that combines the capabilities of OpenTTS and TensorFlow TTS to provide a powerful and flexible text-to-speech solution. This library includes internationalization (i18n) support and performance optimizations through caching and batch processing. It provides a seamless integration between these technologies, offering developers an easy-to-use API for advanced, customizable speech synthesis capabilities.

## Development Status

This project is currently in early development stages and is not yet ready for production use. It is a Development-only GitHub Repository intended for experimentation and collaboration. We are actively working on implementing core functionalities and plan to add a UI in the near future. The API and features are subject to change as the project evolves.

## Installation & Requirements

Ensure you have the following dependencies:
- Python 3.7+
- TensorFlow version: 2.4.0 or higher (but less than 3.0)
- TensorFlowTTS version: 1.8 (or the latest version compatible with our project)
- OpenTTS (currently mocked, not required for installation)

Note: OpenTTS is currently mocked in this project and not directly used. It is listed here as a conceptual dependency, but is not required for installation or development at this stage. Future versions of this project will integrate directly with OpenTTS.

To set up the project:

1. Create and activate a virtual environment
2. Clone the repository and install in editable mode
3. Install TensorFlow and TensorFlowTTS

For detailed installation steps, including GPU support and potential issues, please refer to the [README.md](README.md) file.

## Usage

Here's a basic example of how to use the library, including new features:

```python
from opentts_tensorflow_integration import TTSEngine, VoiceSelector, PerformanceOptimizer

# Initialize the TTS engine with i18n support
tts_engine = TTSEngine(language='en')

# Create a voice selector and add engines
voice_selector = VoiceSelector()
voice_selector.add_engine("openTTS", tts_engine.openTTS_engine)
voice_selector.add_engine("tensorflowTTS", tts_engine.tensorflowTTS_engine)

# Select a voice
voice_selector.select_voice("openTTS", "voice1")

# Create a performance optimizer
optimizer = PerformanceOptimizer(cache_size=1000)

# Generate speech with caching and optimization
text = "Hello, world!"
result = optimizer.synthesize(voice_selector, text)

# Save the audio
tts_engine.save_audio(result['audio'], "output.wav")
```

## API Reference

### TTSEngine

`TTSEngine` is the main class for text-to-speech operations.

Methods:
- `__init__(language: str = 'en')`: Initialize the TTSEngine with a specific language.
- `synthesize(text: str) -> np.ndarray`: Convert text to speech.
- `save_audio(audio: np.ndarray, file_path: str)`: Save the audio waveform to a file.

### VoiceSelector

`VoiceSelector` is a class to manage voice selection across different TTS engines.

Methods:
- `__init__()`: Initialize the VoiceSelector.
- `add_engine(name: str, engine: BaseTTS)`: Add a TTS engine to the voice selector.
- `list_engines() -> List[str]`: List all available TTS engines.
- `list_voices(engine_name: str = None) -> Dict[str, List[str]]`: List all available voices, optionally for a specific engine.
- `select_voice(engine_name: str, voice_name: str)`: Select a voice from a specific engine.
- `get_current_voice() -> Dict[str, str]`: Get the currently selected voice and engine.
- `synthesize(text: str) -> Dict[str, any]`: Synthesize speech using the currently selected engine and voice.

### PerformanceOptimizer

`PerformanceOptimizer` is a class to handle performance optimizations for TTS operations.

Methods:
- `__init__(cache_size: int = 1000)`: Initialize the PerformanceOptimizer with a specific cache size.
- `synthesize(voice_selector: VoiceSelector, text: str) -> Dict[str, any]`: Synthesize speech with caching and optimization.
- `batch_process(voice_selector: VoiceSelector, texts: List[str]) -> List[Dict[str, any]]`: Process multiple TTS requests in batch.
- `clear_cache()`: Clear the entire cache.
- `get_cache_stats() -> Dict[str, Any]`: Get statistics about the current state of the cache.

## Configuration

The library uses a `ConfigManager` class to handle configuration settings. You can access and modify configuration settings as follows:

```python
from opentts_tensorflow_integration.utils import ConfigManager

config = ConfigManager()

# Get a configuration value
model_path = config.get("openTTS.model_path")

# Set a configuration value
config.set("openTTS.model_path", "/path/to/model")

# Update multiple configuration values
config.update({
    "openTTS.model_path": "/path/to/model",
    "default_engine": "openTTS",
    "default_language": "en",
    "cache_size": 1000
})

# Reset to default configuration
config.reset_to_default()
```

## Internationalization

To use the internationalization features:

```python
from opentts_tensorflow_integration import TTSEngine

# Initialize the TTS engine with a specific language
tts_engine = TTSEngine(language='es')

# Synthesize speech in Spanish
text = "Hola, mundo!"
audio = tts_engine.synthesize(text)
```

The library supports multiple languages. To check available languages:

```python
available_languages = tts_engine.get_available_languages()
print(available_languages)
```

## Performance Optimization

The `PerformanceOptimizer` class provides caching and batch processing capabilities:

```python
from opentts_tensorflow_integration import PerformanceOptimizer, VoiceSelector

optimizer = PerformanceOptimizer(cache_size=1000)
voice_selector = VoiceSelector()

# Single synthesis with caching
result = optimizer.synthesize(voice_selector, "Hello, world!")

# Batch processing
texts = ["Hello", "World", "How are you?"]
results = optimizer.batch_process(voice_selector, texts)

# Get cache statistics
stats = optimizer.get_cache_stats()
print(stats)
```

## Testing

We use pytest for unit testing. To run all tests:

```bash
pytest tests/
```

Our current test suite consists of 40 tests, all of which are passing as of the latest run. The test suite typically completes in about 3.39 seconds on our development environment.

To run specific test categories:

```bash
pytest tests/test_tts_engine.py  # Test TTS engine functionality
pytest tests/test_i18n.py        # Test internationalization features
pytest tests/test_performance.py # Test performance optimizations
```

For more verbose output, use the `-v` flag:
```bash
pytest -v
```

### Known Issues

During testing, you may encounter DeprecationWarnings related to Google's protocol buffers library. These warnings are:

1. DeprecationWarning for `google._upb._message.MessageMapContainer`
2. DeprecationWarning for `google._upb._message.ScalarMapContainer`

These warnings are not directly related to our codebase, but rather to a dependency (likely TensorFlow or a related library). They indicate that in Python 3.14, some functionality used by our dependencies might change. While these warnings do not affect the current functionality of the library, they should be monitored for future updates.

## Troubleshooting

Common issues and their solutions:

1. **ImportError: No module named 'opentts'**
   - Make sure you have installed the OpenTTS library. You can install it using `pip install opentts`.

2. **RuntimeError: TensorFlow TTS model is not initialized**
   - Ensure you have called the `load_model()` method before trying to synthesize speech.

3. **VoiceNotFoundError: Voice 'voice_name' is not available**
   - Check the list of available voices using the `available_voices` property of the TTS engine.

4. **LanguageNotSupportedError: Language 'language_code' is not supported**
   - Verify that the language you're trying to use is supported. Use `get_available_languages()` to check supported languages.

5. **PerformanceWarning: Cache hit rate is low**
   - Consider increasing the cache size in the PerformanceOptimizer if you're processing a large amount of unique text.

6. **Compatibility with TensorFlow**: 
   - Ensure that the TensorFlow version is compatible with TensorFlowTTS. If you encounter issues, try installing an earlier version of TensorFlow.

7. **CUDA and cuDNN**: 
   - If you're using GPU acceleration, make sure you have compatible CUDA and cuDNN versions installed.

8. **Dependency Conflicts**: 
   - If you encounter dependency conflicts, you may need to create a separate virtual environment for this project.

9. **Build Errors**: 
   - On some systems, you might need to install additional build tools. On Ubuntu, for example:
     ```bash
     sudo apt-get install build-essential libssl-dev libffi-dev python3-dev
     ```
     
## Contributing

We welcome contributions to the OpenTTS TensorFlow Integration project! Here's how you can contribute:

1. Fork the repository on GitHub.
2. Create a new branch for your feature or bug fix.
3. Write your code and tests.
4. Ensure all tests pass by running `pytest`.
5. Submit a pull request with a clear description of your changes.

Please ensure your code adheres to our coding standards and is covered by appropriate tests. For major changes, please open an issue first to discuss what you would like to change.

---

This documentation is a living document and will be updated as the project evolves. For the latest information, please check the repository or submit an issue if you have any questions or suggestions.
