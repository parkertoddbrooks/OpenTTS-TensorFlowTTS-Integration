import logging
from typing import Optional

class TTSError(Exception):
    """Base class for exceptions in this module."""
    pass

class ModelNotFoundError(TTSError):
    """Exception raised when a TTS model is not found."""
    pass

class VoiceNotFoundError(TTSError):
    """Exception raised when a requested voice is not found."""
    pass

class AudioConversionError(TTSError):
    """Exception raised when there's an error in audio conversion."""
    pass

def setup_logger(name: str, log_file: Optional[str] = None, level: int = logging.INFO) -> logging.Logger:
    """
    Set up a logger with a specified name and optional file output.

    Args:
        name (str): Name of the logger.
        log_file (str, optional): Path to the log file. If None, logs will only be printed to console.
        level (int, optional): Logging level. Defaults to logging.INFO.

    Returns:
        logging.Logger: Configured logger object.
    """
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Create console handler
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    # Create file handler if log_file is specified
    if log_file:
        file_handler = logging.FileHandler(log_file)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    return logger

# Create a default logger for the module
logger = setup_logger('opentts_tensorflow_integration')

def log_error(error: Exception):
    """
    Log an error with its type and message.

    Args:
        error (Exception): The error to log.
    """
    logger.error(f"{type(error).__name__}: {str(error)}")

def log_warning(message: str):
    """
    Log a warning message.

    Args:
        message (str): The warning message to log.
    """
    logger.warning(message)

def log_info(message: str):
    """
    Log an info message.

    Args:
        message (str): The info message to log.
    """
    logger.info(message)