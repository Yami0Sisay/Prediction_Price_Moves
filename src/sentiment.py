from textblob import TextBlob
import pandas as pd

def add_sentiment(df: pd.DataFrame, text_col: str = "headline") -> pd.DataFrame:
    """
    Compute TextBlob polarity scores and sentiment categories
    for a given text column and add them to the DataFrame.

    Parameters
    ----------
    df : pandas.DataFrame
        Input DataFrame containing a text column.
    text_col : str
        Name of the column with headline text.

    Returns
    -------
    df : pandas.DataFrame
        Same DataFrame with 'sentiment_score' and 'sentiment_category' columns.
    """
    def get_polarity(text):
        return TextBlob(str(text)).sentiment.polarity

    def sentiment_category(score):
        if score >= 0.05:
            return "Positive"
        elif score <= -0.05:
            return "Negative"
        else:
            return "Neutral"

    df["sentiment_score"] = df[text_col].apply(get_polarity)
    df["sentiment_category"] = df["sentiment_score"].apply(sentiment_category)
    return df
