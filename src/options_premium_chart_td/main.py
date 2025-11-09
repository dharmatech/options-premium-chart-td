import argparse

from options_premium_chart_td.options_premium_chart import gen_options_premium_chart



def main():
    parser = argparse.ArgumentParser(description='Generate an options premium chart for a given stock symbol.')
    parser.add_argument('symbol', type=str, help='The stock symbol to generate the chart for (e.g., GOOG).')
    parser.add_argument('--premium-threshold', type=int, default=500000,
                        help='The premium threshold to use for the chart (default: 500000).')
    args = parser.parse_args()

    gen_options_premium_chart(args.symbol, premium_threshold=args.premium_threshold)

if __name__ == "__main__":
    main()