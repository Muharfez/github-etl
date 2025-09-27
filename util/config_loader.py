import os
import yaml
from dotenv import load_dotenv

class ConfigError(Exception):
    pass

class ConfigLoader():
    def load_config():
        load_dotenv()
        path="config/config.yaml"

        # Check existence of the config.yaml file
        if not os.path.exists(path):
            raise ConfigError(f"Config file not found at path: {path}")

        # Check for invalid content in the config.yaml file
        try:
            with open(path) as f:
                config = yaml.safe_load(f)
        except yaml.YAMLError as e:
            raise ConfigError(f"Invalid YAML in config file: {e}")

        # Validate all required keys in the config.yaml file
        required_keys = ["query", "page_size", "s3"]
        for key in required_keys:
            if key not in config:
                raise ConfigError(f"Missing required config key: '{key}'")
            if key == "s3" & "bucket" not in config["s3"]:
                raise ConfigError("Missing required key: 's3.bucket' in config.yaml")

        # Validate required environment variables 
        env_vars = ["AWS_ACCESS_KEY_ID", "AWS_SECRET_ACCESS_KEY", "AWS_DEFAULT_REGION"]
        missing_env = [var for var in env_vars if not os.getenv(var)]
        if missing_env:
            raise ConfigError(f"Missing required environment variables: {', '.join(missing_env)}")

        # Return config dict
        return {
            "extract" : {
                "query": config["query"],
                "page_size": config["page_size"],
                "github_token": os.getenv("GITHUB_TOKEN"),
            },
            "load": {
                "bucket": config["s3"]["bucket"],
                "access_key": os.getenv("AWS_ACCESS_KEY_ID"),
                "secret_key": os.getenv("AWS_SECRET_ACCESS_KEY"),
                "region": os.getenv("AWS_DEFAULT_REGION"),
            },
        }