import scipy as sp
import numpy as np

cashflows = [-100, 50, 40, 20, 10, 50]          # First cash flow at time zero
x = np.npv(0.1, cashflows)                      # First input value is discount rate, second = array
print(round(x, 2))
