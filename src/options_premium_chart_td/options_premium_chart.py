
import pandas as pd

from thetadata_utils.get_all_options_trades_cached import get_all_options_trades_cached

from options_premium_chart_td.classify_trades            import classify_trades
from options_premium_chart_td.make_options_premium_chart import make_options_premium_chart
from options_premium_chart_td.get_stock_data             import get_stock_data

def gen_options_premium_chart(symbol: str, premium_threshold: float = 100000):

    pd.set_option('display.float_format', '{:,.2f}'.format)

    df_all = get_all_options_trades_cached(symbol)

    df_all = classify_trades(df_all)

    print(f"Total trades for {symbol}: {len(df_all):,}")

    tmp = df_all[df_all['premium'] > premium_threshold].copy()

    print(f"Trades for {symbol} with premium over {premium_threshold:,}: {len(tmp)}")

    stock_data = get_stock_data(tmp, symbol)

    make_options_premium_chart(tmp, stock_data, symbol)
