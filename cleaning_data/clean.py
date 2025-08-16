# import pandas as pd

# df = pd.read_csv('data.csv')

# df['Date'] = pd.to_datetime(df['Date'], format='mixed')

# print(df.to_string())

# --------------------------------
# Data2_Clean

# Return a new Data Frame with no empty cells:

# import pandas as pd

# df = pd.read_csv('data.csv')

# new_df = df.dropna()

# print(new_df.to_string())

# Does Not Give Any Data Of Non ..
# Note: By default, the dropna() method returns a new DataFrame, and will not change the original.


# -------------------------------------------------------------------------
# If you want to change the original DataFrame, use the inplace = True argument:


# import pandas as pd 
# df = pd.read_csv('data.csv')

# df.dropna(inplace=True)

# print(df.to_string)


# Note: Now, the dropna(inplace = True) will NOT return a new DataFrame, but it will remove all rows containing NULL values from the original DataFrame.


# --------------------------------------------------------------------------------------------------

# Replace Empty Values
# Another way of dealing with empty cells is to insert a new value instead.

# This way you do not have to delete entire rows just because of some empty cells.

# The fillna() method allows us to replace empty cells with a value:

# Example
# Replace NULL values with the number 130:

# import pandas as pd

# df = pd.read_csv('data.csv')

# df.fillna(10, inplace=True)


# ---------------------------------------------------------


# Using Mean Medain Mode 

# import pandas as pd

# df = pd.read_csv('data.csv')

# x = df["Calories"].mean()

# df.fillna({"Calories": x}, inplace=True)\
    
# import pandas as pd

# df = pd.read_csv('data.csv')

# x = df["Calories"].median()

# df.fillna({"Calories": x}, inplace=True)

# import pandas as pd

# df = pd.read_csv('data.csv')

# x = df["Calories"].mode()[0]

# df.fillna({"Calories": x}, inplace=True)


# -----------------------------------------------------

# Let's try to convert all cells in the 'Date' column into dates.

# Pandas has a to_datetime() method for this:

# ExampleGet your own Python Server
# Convert to date:

# import pandas as pd

# df = pd.read_csv('data.csv')

# df['Date'] = pd.to_datetime(df['Date'], format='mixed')

# print(df.to_string())