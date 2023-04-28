from matplotlib.pyplot import *
import numpy as np
from pylab import *

### Gráfico Linear
# plot([1, 2, 3, 9])
# xlabel("x- axis")
# ylabel("my number")
# title("my figure")
# show()

### Gráfico seno e cosseno
# x = np.linspace(-np.pi, np.pi, 256, endpoint=True)
# C, S = np.cos(x), np.sin(x)
# plot(x, C), plot(x, S)
# show()

### Gráfico de dispersão
# n = 1024
# X = np.random.normal(0, 1, n)
# Y = np.random.normal(0, 1, n)
# scatter(X, Y)
# show()

import datetime
import matplotlib.pyplot as plt
import pandas as pd
import mplfinance as mpf

daily = pd.read_csv('C:/Users/dduca/OneDrive/Documentos/python/AAPL.csv', index_col=0, parse_dates=True)
daily.index.name = 'Date'
daily.shape
daily.head(3)
daily.tail(3)
mpf.plot(daily, type='candle', mav=(3, 4, 6), volume=True)     # types: 'candle', 'line', 'renko', 'pnf' # mav = moving average
