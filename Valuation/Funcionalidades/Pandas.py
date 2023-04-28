import pandas as pd
import numpy as np
# print(dir(pd)) #to show all functions contained in the pandas module

# dates = pd.date_range('20160101', periods=5)    #generate an index array
# np.random.seed(12345)
# x = pd.DataFrame(np.random.rand(5, 2), index=dates, columns=('A', 'B'))     # Pandas DataFrame with dates as its index
# print(x)                                                                  # Columns defines the names of those columns
#                                # Seed: because it is used in the program and return the same values for all users
# x.describe()                                    # Descbribe() offer the properties of those two columns

# x = pd.Series([1, 4, -3, np.nan, 5])
# m = np.mean(x)          #mean() = mean of [1, 4, -3, 5]
# x.fillna(m)
# print(x.fillna(m))      #fillna() replace missing values

# np.random.seed(123)
# df = pd.DataFrame(np.random.randn(10, 4))
# print(df)

# np.random.seed(123)     # Fix the random numbers
# x = np.arange(1, 10.1, .25) ** 2
# n = np.size(x)
# y = pd.Series(x + np.random.randn(n))
# bad = np.array([4, 13, 14, 15, 16, 20, 30])     # Generate a few missing values
# x[bad] = np.nan                 # missing code is np.nan
# methods = ['linear', 'quadratic', 'cubic']
# df = pd.DataFrame({m: x.interpolate(method=m) for m in methods})
# df.plot()


# np.random.seed(123)
# df = pd.Series(np.random.randn(100))
# df.to_pickle('test.pkl')        # Save the pickle dataset
# x = pd.read_pickle("c:/temp/test.pkl")
# print(x[:5])

# x = pd.DataFrame({'key':['A', 'B', 'C', 'D'], 'value': [0.1, 0.2, -0.5, 0.9]})
# y = pd.DataFrame({'key':['B', 'D', 'D', 'E'], 'value': [2, 3, 4, 6]})
# z = pd.merge(x, y, on='key')
# print(x)
# print(y)
# print(z)
from datetime import *

from datetime import datetime

date1 = datetime(2010, 2, 3)
date2 = datetime(2010, 3, 31)
print(date2 - date1)                # Difference between two dates

