import numpy as np
import numpy_financial as npf
import Valuation.Functions.fincal


# dir(np)                                 #all functions contained in Numpy
# x = np.array(dir(np))
# len(x)                                  # generate an array containing all functions
# help(np.std)                            # information about sdt()
# x = np.array([[1, 2, 3], [3, 4, 6]])    # 2 by 3 matrix
# np.size(x)                              # number of data items
# np.size(x, 1)                           # show number of columns
# np.std(x)                               # standard deviation
# np.std(x, 1)
# total = x.sum()
# z = np.random.rand(50)                  # 50 random obs from [0.0, 1]
# y = np.random.normal(size=100)          # from standard normal
# r = np.array(range(0, 100), float) / 100    # from 0, 0.1, to .99
#
# np.array([100, 0.1, 2], float)          # specified array should contain the same data type
#
# x1 = [1, 2, 3, 20]
# y1 = np.array(x1, dtype=float)          # all items are float
#
# cashflows = [-100, 30, 40, 40, 50]  # First cash flow at time zero
# # x = npf.npv(0.1, cashflows)             # First input value is discount rate, second = array
# # print(round(x, 2))
# irr = npf.irr(cashflows)
# print(irr)
# print(npf.npv(irr, cashflows))

# cashflows = [-100, -50, 50, 70, 100, 90, 20]        # with one changend direction
# print(npf.irr(cashflows))






# payment = npf.pmt(0.045 / 12, 30 * 12, 2500000)     # Monthly cash flow to pay off a mortgage ; compounded montly;
# print(round(payment, 2))
#
# pv1 = npf.pv(0.1, 5, 0, 100)            # pv of one future cash flow
# print(round(pv1, 2))
# pv2 = npf.pv(0.1, 5, 100)               # pv of annuity
# print(round(pv2, 2))
#
# ret = np.array([0.1, 0.05, -0.02])
# print(np.mean(ret))                       # arithmetic mean

# print(npf.fv(0.1, 3, 0, 100))
# print(npf.pv(0.1, 3, 0, 100))           # pv of one future cash flow
# print(npf.pv(0.1, 5, 100))              # pv of annuity
# print(npf.pv(0.1, 3, 100, 100))         # pv of annuity plus pv of one fv
# print(npf.pmt(0.019 / 12, 3 * 12, 4000))
# r = npf.rate(3 * 12, 2000, -50000, 0)   # monthly effective rate
# print(r * 12)                           # annual percentage rate
# print(npf.nper(0.012, 200, -5000, 0))   # periods needed to repay a loan


## Summarizes functions ##
# npf.fv()
# npf.pv()
# npf.pmt()
# npf.npv()
# npf.rate()
# npf.nper()
# npf.irr()
# npf.mirr()
# npf.ipmt()
# npf.ppmt()




# def geoMeanReturn(ret):
#     return pow(np.prod(ret + 1), 1. / len(ret)) - 1     # Geometric mean
#
#
# ret = np.array([0.1, 0.05, -0.02])
# print(geoMeanReturn(ret))
#
# np.unique([2, 3, 4, 6, 6, 4, 4])     # Array ([2, 3, 4, 6])
# np.median([1, 2, 3, 4, 5])       # 3.0
#
