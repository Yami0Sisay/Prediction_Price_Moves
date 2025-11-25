import pandas as pd

def load_news(path: str) -> pd.DataFrame:
    """
    Load and clean the news dataset.

    - Reads the CSV file from the given path.
    - Drops rows with missing headlines.
    - Converts the date column to datetime.
    - Sorts by date.

    Returns
    -------
    df : pandas.DataFrame
        Cleaned news DataFrame ready for EDA and sentiment analysis.
    """
    df = pd.read_csv(path, index_col=0)
    df = df.dropna(subset=["headline"])
    df["date"] = pd.to_datetime(df["date"], errors="coerce")
    df = df.sort_values("date")
    return df
