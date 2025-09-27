# ARC Challange - ETL Pipeline - GitHub Repositories

This project is a simple ETL pipeline that extracts GitHub repository data, transforms it, and loads it into JSON files on S3. The pipeline demonstrates clean code, logging, error handling, and basic unit testing.

## Project Setup

Clone the repository:

```bash
git clone https://github.com/Muharfez/github-etl.git
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

This project uses **two configuration files**:

- **`.env`** → contains **secrets and credentials** (never commit this to GitHub)  
- **`config/config.yaml`** → contains **pipeline parameters** (safe to commit)  

This separation is intentional:  
- `.env` is machine-specific and holds sensitive values like API keys.  
- `config.yaml` is project-wide and defines how the pipeline should behave.  

---

### 1. `config/config.yaml`

This file contains **pipeline settings** that control the ETL behavior:

```yaml
query: "Data Engineering"   # Search term for GitHub repositories
page_size: 50               # Number of repos per page (GitHub API max is 100)
s3:
  bucket: "your-bucket-name" # Target S3 bucket name
```

### 2. `.env`

This file contains **pipeline settings** that control the ETL behavior:

```env
GITHUB_TOKEN=your_github_token
AWS_ACCESS_KEY_ID=your_aws_access_key
AWS_SECRET_ACCESS_KEY=your_aws_secret_key
AWS_DEFAULT_REGION=your_aws_region

