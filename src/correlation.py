import pandas as pd
from scipy import stats

def compute_daily_correlation(daily_sentiment: pd.DataFrame,
                              returns: pd.DataFrame) -> pd.DataFrame:
    """
    Align daily sentiment with stock returns and compute Pearson correlations.

    Parameters
    ----------
    daily_sentiment : pandas.DataFrame
        DataFrame with an 'avg_sentiment' column indexed by date.
    returns : pandas.DataFrame
        DataFrame with one return column per ticker (e.g. 'AAPL_return').

    Returns
    -------
    corr_df : pandas.DataFrame
        DataFrame with one row per ticker and the corresponding correlation.
    """
    combined = pd.concat([daily_sentiment, returns], axis=1, join="inner").dropna()
    results = {}

    for col in returns.columns:
        if combined[col].count() >= 2:
            corr, _ = stats.pearsonr(combined["avg_sentiment"], combined[col])
            results[col] = corr

    corr_df = pd.DataFrame.from_dict(results, orient="index", columns=["Correlation"])
    return corr_df
