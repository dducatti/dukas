import numpy as np
import statsmodels.api as sm
import statsmodels.api as api

# dir(api) to find more information about submodule
# dir(sm) to find more information about the module
### OLS (ordinary least square) regression
y = [1, 2, 3, 4, 2, 3, 4]
x = range(1, 8)
x = sm.add_constant(x)
results = sm.OLS(y, x). fit()
print(results.params)

# read_clipboard      # Input data from clipboard
# read_csv            # Input data form a csv (comma separated value)
# read_excel          # Input data from an Excel file
# read_fwf            # Input data with a fixed width
# read_gbq            # Load data from Google BigQuery
# read_hdf            # Read HDF4 format data
# read_html           # Input data from a web page
# read_json           # Read JSON (JavaScript Object Notation) data
# read_msgpack        # MessagePack is a fast, compact binary serialization format, suitable for similar data to JSON
# read_pickle         # Input a Python dataset called pickle
# read_sas            # Input data from a SAS dataset
# read_sql            # Input data from SQL database
# real_sql_query      # Input data from a query
# real_sql_table      # Read SQL database table into a DataFrame
# read_stata          # Input data from a Stata dataset
# read_table          # input data from a text file

