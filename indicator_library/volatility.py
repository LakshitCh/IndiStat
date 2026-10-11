import pandas as pd


def bollinger_bands(
    data: pd.DataFrame, period: int = 20, multiplier: float = 2.0
) -> pd.DataFrame:
    """Calculates Bollinger Bands (Middle, Upper, and Lower bands).

    Bollinger Bands consist of a Simple Moving Average (SMA) and upper/lower bands
    that are standard deviations away from the SMA.

    Args:
        data (pd.DataFrame): A pandas DataFrame containing at least a 'Close' column.
        period (int, optional): The lookback period for the SMA and standard deviation. Defaults to 20.
        multiplier (float, optional): The number of standard deviations for the upper/lower bands. Defaults to 2.0.

    Returns:
        pd.DataFrame: A new DataFrame with 'BB_Middle', 'BB_Upper', and 'BB_Lower' columns appended.
    """
    result = data.copy()

    result["BB_Middle"] = (
        result["Close"].rolling(window=period, min_periods=period).mean()
    )

    rolling_std = (
        result["Close"].rolling(window=period, min_periods=period).std()
    )

    result["BB_Upper"] = result["BB_Middle"] + (multiplier * rolling_std)
    result["BB_Lower"] = result["BB_Middle"] - (multiplier * rolling_std)

    return result