from pandas_datareader import data as pdr
import yfinance as yf
ticker = 'SPY'

yf.pdr_override()
data = pdr.get_data_yahoo(ticker, start='2017-01-01', end='2017-04-30', )

print(data.Open)
ret = data.close[1:] / data.close[:-1] - 1
print(ret)
