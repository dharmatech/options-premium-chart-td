import pandas as pd

def classify_trades(df: pd.DataFrame) -> pd.DataFrame:

    df['ask'] = pd.to_numeric(df['ask'])
    df['bid'] = pd.to_numeric(df['bid'])
    df['price'] = pd.to_numeric(df['price'])
    df['size'] = pd.to_numeric(df['size'])
    # ---------------------------------------------------------------
    df['mid'] = (df['bid'] + df['ask']) / 2
    # ---------------------------------------------------------------
    df.loc[df['price'] >  df['mid'], 'side'] = 'BUY'
    df.loc[df['price'] <  df['mid'], 'side'] = 'SELL'
    df.loc[df['price'] == df['mid'], 'side'] = 'MID'
    # ---------------------------------------------------------------
    # df.drop(columns=['size', 'price', 'bid', 'ask', 'ext_condition1', 'ext_condition2', 'ext_condition3', 'ext_condition4', 'quote_timestamp', 'sequence', 'condition',  'exchange',  'bid_size', 'bid_exchange', 'bid_condition', 'ask_size', 'ask_exchange', 'ask_condition', 'outlook'])
    # CALL BUY   bullish
    # CALL SELL  bearish
    # PUT  BUY   bearish
    # PUT  SELL  bullish    
    df.loc[(df['right'] == 'CALL') & (df['side'] == 'BUY' ), 'sentiment'] = 'bullish'
    df.loc[(df['right'] == 'CALL') & (df['side'] == 'SELL'), 'sentiment'] = 'bearish'
    df.loc[(df['right'] == 'PUT' ) & (df['side'] == 'BUY' ), 'sentiment'] = 'bearish'
    df.loc[(df['right'] == 'PUT' ) & (df['side'] == 'SELL'), 'sentiment'] = 'bullish'
    # ---------------------------------------------------------------
    df['premium'] = df['size'] * df['price'] * 100
    # ---------------------------------------------------------------
    # df = df_all
    df['dte'] = (pd.to_datetime(df['expiration']) - pd.to_datetime(df['trade_timestamp'])).dt.days

    return df

