# Stock Screener

A Python script that screens and sorts the top 50 stocks in the S&P 500 by various criteria such as price, percentage change, volume, or market capitalization. The script aims to provide a quick and efficient way to analyze market data.

## Features

- **Sorting Options**: Sort stocks by:
  - Price
  - Percentage Change
  - Volume
  - Market Cap
- **Real-Time Data**: Uses up-to-date market data for analysis.
- **Customizable**: Easily adaptable for different sorting criteria or additional stock filters.

## Requirements

- Python 3.7+
- Required Python libraries:
  - `pandas`
  - `yfinance`
  - `sys`

Install the dependencies:
```bash
pip install pandas yfinance sys
```

## Usage

1. Run the script:
   ```bash
   python screener.py
   ```

2. Follow the prompts to choose the sorting criteria (e.g., price, percentage change, volume, or market cap).

3. The script will fetch the top 50 stocks from the S&P 500, sort them based on the chosen criteria, and display the results.

## Example

```bash
python screener.py marketcap
```
Output:
```
Top 50 S&P 500 Stocks Sorted by Market Cap:
1. AAPL - $2.87T
2. MSFT - $2.42T
...
```

## Next Steps

1. **Add Color**:
   - Use terminal color libraries (e.g., `colorama`) to highlight specific values (e.g., green for positive percentage changes and red for negative).
3. **Optimize Speed**:
   - Download and cache ticker data to reduce API call overhead and improve performance.
