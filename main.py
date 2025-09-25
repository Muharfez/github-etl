import os
import yaml
from dotenv import load_dotenv

from etl.extract import extract
from etl.transform import transform

# Load env
load_dotenv()

# Load config
with open("config/config.yaml") as f:
    config = yaml.safe_load(f)

token = os.getenv("GITHUB_TOKEN")
query = config["query"]

data = extract(query=query, token=token)
data = transform(data)