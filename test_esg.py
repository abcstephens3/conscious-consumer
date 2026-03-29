import yfinance as yf

ticker = yf.Ticker("XOM")
esg = ticker.sustainability
print(esg)
