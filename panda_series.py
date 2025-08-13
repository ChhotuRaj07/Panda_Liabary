# What is a Series?
# A Pandas Series is like a column in a table.

# It is a one-dimensional array holding data of any type.

# import pandas as pd
 
# a = [1,3,4,5]
 
# myvar = pd.Series(a)
 
# print(myvar)

# print(myvar[0])



# -------------------------------------------------------------------

# Create labels
# With the index argument, you can name your own labels.

# import pandas as pd

# a = [1,7,6]

# myvar = pd.Series(a, index= ["x", "y", "z"])

# print("Specific Index with Name as Label ")

# print(myvar)
# print("I Access a Value of y Index as say index no 1 as a numerical value so as we create own label on it call ity his name of index ", myvar["y"])


#  ---------------------------------------------------------------------------------------------------------

# Key/Value Objects as Series
# You can also use a key/value object, like a dictionary, when creating a Series.

# Create a simple Pandas Series from a dictionary:



# import pandas as pd

# calories = {"day1" : 420 ,"day2": 380, "day3": 530}

# myvar = pd.Series(calories)

# print(myvar)

# -------------------------------------------------------------------------------------


# Key/Value Objects as Series
# You can also use a key/value object, like a dictionary, when creating a Series.

# import pandas as pd

# calories = {"day1": 420, "day2": 380, "day3": 390}

# myvar = pd.Series( calories , index= ["day1" , "day2"])
                  
# print(myvar)

# print(myvar["day2"])



# Create a DataFrame from two Series:

import pandas as pd

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

myvar = pd.DataFrame(data)

print("In data frame of 2 Series:")
print(myvar)