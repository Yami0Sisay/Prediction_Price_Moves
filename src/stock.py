import pandas as pd
import yfinance as yf

def load_stock_data(tickers, start, end) -> pd.DataFrame:
    """
    Download OHLCV stock data for a list of tickers using yfinance.

    Parameters
    ----------
    tickers : list of str
        List of ticker symbols.
    start : str or datetime
        Start date for historical data.
    end : str or datetime
        End date for historical data.

    Returns
    -------
    df : pandas.DataFrame
        DataFrame with OHLCV data, flattened column names if needed.
    """
    df = yf.download(tickers, start=start, end=end, progress=False)

    if isinstance(df.columns, pd.MultiIndex):
        df.columns = [f"{c[0]}_{c[1]}" for c in df.columns]

    df = df.dropna()
    return df
