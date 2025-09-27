# ARC Challange - ETL Pipeline - GitHub Repositories

This project is a simple ETL pipeline that extracts GitHub repository data, transforms it, and loads it into JSON files on S3.

## Project Setup

Clone the repository:

```bash
git clone https://github.com/Muharfez/github-etl.git
cd github-etl
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
---

## Configuration

This project uses **two configuration files**:

- **`.env`** → contains **secrets and credentials**  
- **`config/config.yaml`** → contains **pipeline parameters**  

This separation is intentional:  
- `.env` holds sensitive values like API keys.  
- `config.yaml` defines how the pipeline should behave.  

### 1. `config/config.yaml`

This file contains **pipeline settings** that control the ETL behavior:

```yaml
query: "Data Engineering"   # Search term for GitHub repositories- For info on how to construct a search query: 
page_size: 50               # Number of repos per page
s3:
  bucket: "your-bucket-name" # Target S3 bucket name
```

### 2. `.env`

This file contains **sensitive credentials** needed for authentication:

```env
GITHUB_TOKEN=your_github_token
AWS_ACCESS_KEY_ID=your_aws_access_key
AWS_SECRET_ACCESS_KEY=your_aws_secret_key
AWS_DEFAULT_REGION=your_aws_region
``` 

Create these 2 files in your project and configure them with your pipeline settings/credentials.

---

### Running the script
Run the main script:
```bash
python main.py
```
Logs are stored in application.log and also printed to the console.

---

### Running Unit Tests
Unit tests are stored in the tests/ directory. To run all tests:
```bash
python -m unittest discover tests
```
Or run a specific test file:
```bash
python -m unittest tests/test_transformer.py
```

---

### Notes
- Ensure your .env and config/config.yaml are correctly set up before running the pipeline.
- The pipeline will stop gracefully if required configurations or credentials are missing.
- The GITHUB_TOKEN is optional, but without it, the GitHub API is subject to strict rate limits for unauthenticated requests. For more information on rate limits and guidance on constructing search queries, refer to the GitHub API documentation
