import pandas as pd

def transform(data : list):
    df = pd.json_normalize(data)

    # Filter only needed column
    df = df[["full_name", "language", "stargazers_count", "created_at", "updated_at"]]
    
    # Filter rows with no langauage or with less than 5 stars
    df = df[(df.language.notna())]

    # Convert timestamps
    df["created_at"] = pd.to_datetime(df["created_at"])
    df["updated_at"] = pd.to_datetime(df["updated_at"])

    # Further derived columns
    df["is_active"] = df["updated_at"] > (pd.Timestamp.now(tz="UTC") - pd.Timedelta(days=365))
    df["popularity_score"] = ((df["stargazers_count"] / 1000) + (df["is_active"].astype(int) * 10))
    df["is_popular"] = df["popularity_score"] >= 10

    # Sort by popularity score
    df = df.sort_values(by="popularity_score", ascending=False)
    
    return df