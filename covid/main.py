import pandas as pd
import numpy as np

#insert data
data = pd.read_csv("data.csv")

data = data.drop("Date" , axis = 1)






#testing
print(data.isnull().sum())
