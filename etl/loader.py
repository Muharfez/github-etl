import pandas as pd
import boto3

from io import BytesIO
from util.logger import Logger
class Loader: 
    def __init__(self, config : dict):
        self.logger = Logger().get_logger()
        self.config = config

    def load(self, df: pd.DataFrame):
        try:
            s3 = boto3.client(
                "s3",
                aws_access_key_id = self.config["access_key"],
                aws_secret_access_key = self.config["secret_key"],
                region_name = self.config["region"]
            )
            
            for (lang, year), subset in df.groupby(["language", "year"]):
                buffer = BytesIO()
                subset.to_json(buffer, orient="records", lines=True)

                key = f"repos/language={lang}/year={year}/data.json"
                s3.put_object(Body=buffer.getvalue(), Bucket = self.config["bucket"], Key=key)
                self.logger.info(f'Saved {len(subset)} records to s3://{self.config["bucket"]}/{key}')

        except Exception as e:
            self.logger.error(f"Error in loader: {e}")