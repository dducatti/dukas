from matplotlib.pyplot import *
import numpy as np
import numpy_financial as npf
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

# daily = pd.read_csv('C:/Users/dduca/OneDrive/Documentos/python/AAPL.csv', index_col=0, parse_dates=True)
# daily.index.name = 'Date'
# daily.shape
# daily.head(3)
# daily.tail(3)
# mpf.plot(daily, type='candle', mav=(3, 4, 6), volume=True)     # types: 'candle', 'line', 'renko', 'pnf' # mav = moving average


# cashflows = [-120, 50, 60, 70]
# rate = []
# npv = []
# x = (0, 0.7)
# y = (0, 0)
# for i in range(1, 70):
#     rate.append(0.01 * i)
#     npv.append(npf.npv(0.01 * i, cashflows))
#
# title("NPV profile")
# xlabel('Discount Rate')
# ylabel('NPV (Net Present Value)')
# plot(rate, npv)
# plot(x, y)
# show()


cashflow = [504, -432, -432, -432, 832]
rate = []
npv = []
x = [0, 0.3]
y = [0, 0]
for i in range(1, 30):
    rate.append(0.01 * i)
    npv.append(npf.npv(0.01 * i, cashflow))

title('IRR')
xlabel('Discount Rate')
ylabel('NPV (Net Present Value)')
plt.plot(x, y), plt.plot(rate, npv)
plt.show()
