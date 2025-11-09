import pandas as pd
import plotly.graph_objects as go

# df_all.drop(columns=['ext_condition1', 'ext_condition2', 'ext_condition3', 'ext_condition4', 'quote_timestamp', 'sequence', 'condition',  'exchange',  'bid_size', 'bid_exchange', 'bid_condition', 'ask_size', 'ask_exchange', 'ask_condition'])

# def make_options_premium_chart(df_all, stock_data, symbol, expiration):
def make_options_premium_chart(df_all, stock_data, symbol):

    df_all['strike'] = pd.to_numeric(df_all['strike'])

    # Create the bubble chart
    fig = go.Figure()

    # Add stock price trace
    fig.add_trace(go.Scatter(
        x=stock_data.index,
        y=stock_data['Close'],
        mode='lines',
        name='Stock Price',
        line=dict(color='black', width=2)
    ))

    # Define mappings for shapes and colors
    shape_map = {'CALL': 'diamond-open', 'PUT': 'circle-open'}
    color_map = {'bullish': 'green', 'bearish': 'red'}

    for right_type in ['CALL', 'PUT']:
        for sentiment_type in ['bullish', 'bearish']:
            df_subset = df_all[(df_all['right'] == right_type) & (df_all['sentiment'] == sentiment_type)]
            if not df_subset.empty:
                fig.add_trace(go.Scatter(
                    x=df_subset['trade_timestamp'],
                    y=df_subset['strike'],
                    mode='markers',
                    marker=dict(
                        symbol=shape_map[right_type],
                        color=color_map[sentiment_type],
                        size=df_subset['premium'],
                        sizemode='area',
                        sizeref=2.*max(df_all['premium'])/(40.**2),
                        sizemin=4
                    ),
                    name=f'{sentiment_type.capitalize()} {right_type}',
                    hoverinfo='text',
                    # text=df_subset.apply(lambda row: f"Strike: {row['strike']}<br>Premium: {row['premium']:,.2f}<br>Side: {row['side']}", axis=1)
                    text=df_subset.apply(lambda row: f"Strike: {row['strike']}<br>Premium: {row['premium']:,.2f}<br>Side: {row['side']}<br>Expiration: {row['expiration']}<br>DTE: {row['dte']}", axis=1)
                ))

    # Determine y-axis range
    min_y = min(df_all['strike'].min(), stock_data['Close'].min())
    max_y = max(df_all['strike'].max(), stock_data['Close'].max())

    # Add a 5% buffer to the y-axis range
    min_y *= 0.95
    max_y *= 1.05

    fig.update_layout(
        title=f'Options Premium for {symbol}. {len(df_all):,} trades with premium over ${df_all["premium"].min():,.0f}',
        xaxis_title='Trade Time',
        yaxis_title='Price',
        legend_title='Sentiment',
        yaxis=dict(range=[min_y, max_y])
    )

    # fig.write_html(f"options_premium_chart_{symbol}_{expiration}.html")
    fig.write_html(f"options_premium_chart_{symbol}.html")

    # print(f"Chart saved to options_premium_chart_{symbol}_{expiration}.html")
    print(f"Chart saved to options_premium_chart_{symbol}.html")
