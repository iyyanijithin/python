#We can also use google colab
#But starting the basic way

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Load the data using pandas
dataset =  pd.read_csv('Data.csv')

#After loading the data.
#We will divide the data into two parts
#Feature and dendentant variables
#In our case Feature would be x
#Dependnt will be you y (dependent variables followed by y)
x = dataset.iloc[:, :-1].values
y = dataset.iloc[:,-1].values

print(x)
print(y)
