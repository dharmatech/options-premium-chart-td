
Generates a chart of options premium using ThetaData.

You'll need a pro level options subscription with [ThetaData](https://www.thetadata.net/).

# Install

To install using `uv` in a test environment:

```
mkdir test-options-premium-chart-app
cd test-options-premium-chart-app
uv venv
.\.venv\Scripts\activate
uv pip install "git+https://github.com/dharmatech/options-premium-chart-td"
```

# Run

To run:

```
python -m options_premium_chart_td.main --premium-threshold 100000 GME
```

The first time you run this script for a given symbol, all the options trades for that symbol will be downloaded and saved in the local cache. This will take a very long time. The next time you run the script for that symbol, it can be expected to take much less time.

# Cache

The options trades data is stored in `~/.thetadata-api-v3-cache`.

# Result

The script will generate an file: `options_premium_chart_GME.html`.

![alt text](image.png)