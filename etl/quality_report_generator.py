from datetime import datetime, timezone
import pandas as pd
import numpy as np
from util.logger import Logger

class QualityReportGenerator:
    def __init__(self):
        self.logger = Logger().get_logger()
        
    def generate_report(self, df: pd.DataFrame):
        report = {
            "generated_at": datetime.now(timezone.utc).isoformat(),
            "row_count": len(df),
            "popularity_percentage" : np.round((df["is_popular"].sum() / df["is_popular"].count()) * 100, 2).item(),
            "unique_langauges" : df["language"].nunique()
        }

        repos_per_language = (
            df.groupby(["language"])
            .size()
            .reset_index(name="repos")
            .to_dict(orient="records")
        )

        report["repos_per_language"] = repos_per_language

        return report