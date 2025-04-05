import yfinance as yf

def get_data(ticker: str):
    """
    """
    try:
        stock = yf.Ticker(ticker)
        data = stock.history(period ="1d")
        info = stock.info

        if not data.empty and "sector" in info:
            return{
                "name": info.get("longName", "Unknown"),
                "ticker": ticker,
                "price": data["Close"].iloc[-1],
                "market_cap": info.get("marketCap", 0),
                "sector": info.get ("sector", "N/A"),
                "volume": info.get("volume", 0)

            }
        else:
            raise ValueError (f"There is no data found for the ticker {ticker}")     
    except Exception as e:
        print(f"Error for the data {ticker}: {e}")
        return None