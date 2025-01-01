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

1. Run the script with the following arguments:
   ```bash
   python screener.py <command>
   ```

   - `<command>`: Specifies the sorting criteria. Options include:
     - `price`: Sorts stocks by price from highest to lowest.
     - `-price`: Sorts stocks by price from lowest to highest.
     - `change`: Sorts stocks by percentage change from highest to lowest.
     - `-change`: Sorts stocks by percentage change from lowest to highest.
     - `volume`: Sorts stocks by volume from highest to lowest.
     - `-volume`: Sorts stocks by volume from lowest to highest.
     - `marketcap`: Sorts stocks by market cap from highest to lowest.
     - `-marketcap`: Sorts stocks by market cap from lowest to highest.

2. The script will fetch the top 50 stocks from the S&P 500, sort them based on the chosen criteria, and display the results.

## Example

```bash
python screener.py marketcap
```
Output:
```
Ticker  Price  Change %    Volume Market Cap
  AAPL 250.42     -0.71 1,306,971     3.79 T
 GOOGL 189.30     -1.01   942,183     2.32 T
...
```

## Next Steps

1. **Add Color**:
   - Use terminal color libraries (e.g., `colorama`) to highlight specific values (e.g., green for positive percentage changes and red for negative).
3. **Optimize Speed**:
   - Download and cache ticker data to reduce API call overhead and improve performance.
