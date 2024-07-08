(opentts+tensorflowtts-venv) parker@PxB-MBP-16 OpenTTS_TensorFlow_Integration % cat /Users/parker/Documents/dev/claude-engineer/_Projects/OpenTTS_TensorFlow_Integration/src/opentts_tensorflow_integration/utils/i18n.py
import os
import gettext

def setup_i18n(locale_dir, language='en'):
    """
    Set up internationalization for the application.
    
    Args:
        locale_dir (str): Path to the directory containing translation files.
        language (str): The language code to use (e.g., 'en', 'es', 'fr').
    
    Returns:
        gettext.GNUTranslations: A translations object.
    """
    try:
        # The translation files should be named like 'es.mo', 'fr.mo', etc.
        translations = gettext.translation('messages', localedir=locale_dir, languages=[language])
        translations.install()
        return translations
    except FileNotFoundError:
        # If no translation file is found, fall back to the default language (no translation)
        return gettext.NullTranslations()

# Helper function to mark strings for translation
def _(message):
    return message

# Example usage:
# setup_i18n('/path/to/locale/dir', 'es')
# print(_("Hello, World!"))  # This will print the Spanish translation if available%                                 
