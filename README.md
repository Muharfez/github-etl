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
The config.yaml contains pipeline-specific settings

.env

The .env file stores sensitive credentials for the github-api and the s3-bucket
