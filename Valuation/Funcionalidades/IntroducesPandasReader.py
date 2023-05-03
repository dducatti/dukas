import datetime
import pandas_datareader.data as web
import yfinance as yf
import numpy as np
yf.pdr_override()

ticker = 'IBM'
start = datetime.datetime(2000, 6, 1)
end = datetime.datetime(2022, 6, 1)
msft = web.DataReader(ticker, start, end)
msft['% Change'] = (msft['Adj Close'] / msft['Adj Close'].shift(1)) - 1
print(msft['% Change'])

