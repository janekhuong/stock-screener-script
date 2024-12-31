import pandas
import yfinance as yf
import sys


def format_number(number):
    if number >= 1e12:
        return f"{number / 1e12:.2f} T"
    elif number >= 1e9:
        return f"{number / 1e9:.2f} B"
    else:
        return f"{number:,}"


def main(filter_type):
    url = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"
    table = pandas.read_html(url)[0]
    tickers = table["Symbol"].tolist()

    market_caps = []
    final_df = pandas.DataFrame(
        columns=["Ticker", "Price", "Change %", "Volume", "Market Cap"]
    )

    for ticker in tickers:
        ticker = yf.Ticker(ticker)
        ticker_market_cap = ticker.info.get("marketCap")

        if ticker_market_cap is None or isinstance(ticker_market_cap, float):
            ticker_market_cap = 0

        new_ticker_market_cap = format_number(ticker_market_cap)

        market_caps.append(new_ticker_market_cap)

    top_market_caps = pandas.DataFrame(
        list(zip(tickers, market_caps)), columns=["Ticker", "Market Cap"]
    )
    top_market_caps = round(top_market_caps[:50], 2)

    data_list = []

    for ticker_str in top_market_caps["Ticker"]:
        try:
            ticker = yf.Ticker(ticker_str)
            price = ticker.info.get("currentPrice")

            latest_price = ticker.history(period="1d")["Close"].iloc[-1]
            previous_close = ticker.info.get("previousClose")

            if previous_close:
                change_percentage = round(
                    ((latest_price - previous_close) / previous_close) * 100, 2
                )
            else:
                change_percentage = 0

            data = ticker.history(period="1d", interval="1m")
            volume = data["Volume"].iloc[-1] if not data["Volume"].isnull().all() else 0

            data_list.append(
                {
                    "Ticker": ticker_str,
                    "Price": price,
                    "Change %": change_percentage,
                    "Volume": f"{volume:,}",
                    "Market Cap": top_market_caps[
                        top_market_caps["Ticker"] == ticker_str
                    ]["Market Cap"].values[0],
                }
            )

        except Exception as e:
            print(f"{e} for {ticker}")

    pandas.set_option("display.max_columns", 6)
    final_df = pandas.DataFrame(data_list)

    if filter_type.lower() == "price":
        final_df = final_df.sort_values(by="Price", ascending=False)
    elif filter_type.lower() == "-price":
        final_df = final_df.sort_values(by="Price", ascending=True)
    elif filter_type.lower() == "change":
        final_df = final_df.sort_values(by="Change %", key=abs, ascending=False)
    elif filter_type.lower() == "-change":
        final_df = final_df.sort_values(by="Change %", key=abs, ascending=True)
    elif filter_type.lower() == "volume":
        final_df = final_df.sort_values(by="Volume", ascending=False)
    elif filter_type.lower() == "-volume":
        final_df = final_df.sort_values(by="Volume", ascending=True)
    elif filter_type.lower() == "marketcap":
        final_df["Market Cap Numeric"] = final_df["Market Cap"].apply(
            lambda x: float(x[:-1]) * (1e12 if x[-1] == "T" else 1e9)
        )
        final_df = final_df.sort_values(by="Market Cap Numeric", ascending=False).drop(
            columns=["Market Cap Numeric"]
        )
    elif filter_type.lower() == "-marketcap":
        final_df["Market Cap Numeric"] = final_df["Market Cap"].apply(
            lambda x: float(x[:-1]) * (1e12 if x[-1] == "T" else 1e9)
        )
        final_df = final_df.sort_values(by="Market Cap Numeric", ascending=True).drop(
            columns=["Market Cap Numeric"]
        )
    else:
        raise ValueError("Invalid command.")

    print(final_df.to_string(index=False))


if __name__ == "__main__":
    args = sys.argv
    if len(args) > 2:
        raise Exception("You must pass in a maximum of one filter")
    
    filter_type = args[1] if len(args) > 1 else "change"

    main(filter_type)
