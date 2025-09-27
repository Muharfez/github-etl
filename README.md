# Lightweight ETL Pipeline - GitHub Repositories

This project is a simple ETL pipeline that extracts GitHub repository data, transforms it, and loads it into JSON files on S3. The pipeline demonstrates clean code, logging, error handling, and basic unit testing.

## Project Setup

Clone the repository:

```bash
git clone https://github.com/yourusername/etl-github.git
cd etl-github
```
It is recommended to use a virtual environment:
```bash
python -m venv venv
source venv/bin/activate      # Linux/macOS
venv\Scripts\activate         # Windows
```

## Installation

Install required Python libraries:
```bash
pip install -r requirements.txt
```

## Configuration

config/config.yaml
The config.yaml contains pipeline-specific settings:

query → search term for GitHub repositories
page_size → number of repositories per page
s3.bucket → target S3 bucket name

Create the config.yaml file under the config folder in the root directory of the project. Use the config.example.yaml file there as a templete for your actual config.yaml file.
Important: Do not commit config.yaml to GitHub. Add it to .gitignore.

.env

The .env file stores sensitive credentials for the github-api and the s3-bucket:
GITHUB_TOKEN=your_github_token
AWS_ACCESS_KEY_ID=your_aws_access_key
AWS_SECRET_ACCESS_KEY=your_aws_secret_key
AWS_DEFAULT_REGION=your_aws_region

Note: Create the .env file under directly in the root directory of the project. Use the .env.example file there as a templete for your actual .env
Important: Do not commit .env to GitHub. Add it to .gitignore.