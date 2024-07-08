import os
import gettext
from typing import Optional

# Get the project root directory
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
LOCALE_DIR = os.path.join(PROJECT_ROOT, 'locale')

# Global variables to store the current translations and language
_current_translations = None
_current_language = 'en'

def setup_i18n(language: str = 'en') -> None:
    """
    Set up internationalization for the application.
    
    Args:
        language (str): The language code to use (e.g., 'en', 'es', 'fr').
    """
    global _current_translations, _current_language
    try:
        # The translation files should be named like 'es.mo', 'fr.mo', etc.
        _current_translations = gettext.translation('messages', localedir=LOCALE_DIR, languages=[language])
        _current_translations.install()
        _current_language = language
    except FileNotFoundError:
        print(f"Warning: No translation found for language '{language}'. Falling back to English.")
        _current_translations = gettext.NullTranslations()
        _current_language = 'en'

def change_language(language: str) -> None:
    """
    Change the current language.

    Args:
        language (str): The language code to switch to (e.g., 'en', 'es', 'fr').
    """
    setup_i18n(language)

def get_current_language() -> str:
    """
    Get the current language code.

    Returns:
        str: The current language code.
    """
    return _current_language

def _(message: str) -> str:
    """
    Translate a message.

    Args:
        message (str): The message to translate.

    Returns:
        str: The translated message, or the original message if no translation is found.
    """
    if _current_translations is None:
        setup_i18n()
    return _current_translations.gettext(message)

# Initialize with default language (English)
setup_i18n()