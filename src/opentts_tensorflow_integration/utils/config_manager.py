import json
import os
from typing import Dict, Any

class ConfigManager:
    """
    A class to manage configuration settings for the TTS integration.
    """

    def __init__(self, config_file: str = "config.json"):
        """
        Initialize the ConfigManager.

        Args:
            config_file (str): The name of the configuration file. Defaults to "config.json".
        """
        self.config_file = config_file
        self.config: Dict[str, Any] = {}
        self.load_config()

    def load_config(self):
        """
        Load the configuration from the file. If the file doesn't exist, create a default configuration.
        """
        if os.path.exists(self.config_file):
            with open(self.config_file, 'r') as f:
                self.config = json.load(f)
        else:
            self.config = self.get_default_config()
            self.save_config()

    def save_config(self):
        """
        Save the current configuration to the file.
        """
        with open(self.config_file, 'w') as f:
            json.dump(self.config, f, indent=4)

    def get_default_config(self) -> Dict[str, Any]:
        """
        Get the default configuration settings.

        Returns:
            Dict[str, Any]: A dictionary containing default configuration settings.
        """
        return {
            "openTTS": {
                "model_path": "",
                "default_voice": ""
            },
            "tensorflowTTS": {
                "model_path": "",
                "default_voice": ""
            },
            "default_engine": "openTTS",
            "output_format": "wav",
            "sample_rate": 22050
        }

    def get(self, key: str, default: Any = None) -> Any:
        """
        Get a configuration value.

        Args:
            key (str): The configuration key.
            default (Any, optional): The default value to return if the key is not found.

        Returns:
            Any: The configuration value, or the default if not found.
        """
        return self.config.get(key, default)

    def set(self, key: str, value: Any):
        """
        Set a configuration value.

        Args:
            key (str): The configuration key.
            value (Any): The value to set.
        """
        self.config[key] = value
        self.save_config()

    def update(self, new_config: Dict[str, Any]):
        """
        Update multiple configuration values at once.

        Args:
            new_config (Dict[str, Any]): A dictionary of configuration keys and values to update.
        """
        self.config.update(new_config)
        self.save_config()

    def reset_to_default(self):
        """
        Reset the configuration to default values.
        """
        self.config = self.get_default_config()
        self.save_config()