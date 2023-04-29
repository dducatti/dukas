import pandas as pd
import pandas_datareader.data as web
import yfinance
import numpy_financial as fin

# acao = yfinance.Ticker("ODPV3.SA")
# info = acao.info                        # Enterprise infos
# hist = acao.history(period='max')
#
# print(hist.head())                      # First datas
# print(hist.tail())                      # Last datas
# print(dir(fin))                           #

print(fin.pv(0.1, 1, 0, 100))
