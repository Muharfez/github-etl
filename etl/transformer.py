import pandas as pd

from util.logger import Logger

class Transformer:
    def __init__(self):
        self.logger = self.logger = Logger().get_logger()

    def transform(self, data : list):
        try:
            df = pd.json_normalize(data)

            # Filter only needed column
            df = df[["full_name", "language", "stargazers_count", "forks_count", "created_at", "updated_at"]]
            
            # Filter rows with no langauage
            df = df[(df.language.notna())]

            # Filter languages with >=10 repos
            lang_counts = df.groupby("language")["language"].transform("size")
            df = df[lang_counts >= 10]
            
            # Convert timestamps
            df["created_at"] = pd.to_datetime(df["created_at"])
            df["updated_at"] = pd.to_datetime(df["updated_at"])

            # Derived columns
            df["year"] = df["created_at"].dt.year
            df["is_active"] = df["updated_at"] > (pd.Timestamp.now(tz="UTC") - pd.Timedelta(days=180))
            df["is_popular"] = df["stargazers_count"] > 1000

            # Sort by stars
            df = df.sort_values(by=["stargazers_count"], ascending=False)

            return df.reset_index(drop=True)
        
        except Exception as e:
            self.logger.error(f"Error in transformer: {e}")