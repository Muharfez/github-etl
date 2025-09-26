import os
import yaml
from dotenv import load_dotenv

def load_config():
    load_dotenv()

    path="config/config.yaml"
    with open(path) as f:
        config = yaml.safe_load(f)

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