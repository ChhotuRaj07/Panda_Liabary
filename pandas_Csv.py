# import pandas as pd


# # Tip: use to_string() to print the entire DataFrame.

# df = pd.read_csv('data.csv')
# print(df.to_string())  


# ---------------------------------------------------------------------


# import pandas as pd 

# df = pd.read_csv('data.csv')

# print(df)



# -------------------------------------------------------------------

# max_rows
# The number of rows returned is defined in Pandas option settings.

# You can check your system's maximum rows with the pd.options.display.max_rows statement.


# import pandas as pd 

# df = (pd.options.display.max_rows)



# ------------------------------------------------------------------------------

import pandas as pd 
pd.options.display.max_rows = 9

df = pd.read_csv('data.csv')

print(df)
