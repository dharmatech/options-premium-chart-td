import yfinance as yf
import pandas as pd

def get_stock_data(trades_df, symbol, interval='1d'):
    """Fetches historical stock data for the date range of the given trades."""
    start_date = trades_df['trade_timestamp'].min().strftime('%Y-%m-%d')
    end_date = trades_df['trade_timestamp'].max()

    # Add one day to end_date to ensure the full last day is included
    end_date = (end_date + pd.Timedelta(days=1)).strftime('%Y-%m-%d')

    stock_data = yf.download(symbol, start=start_date, end=end_date, multi_level_index=False, interval=interval)
    return stock_data
