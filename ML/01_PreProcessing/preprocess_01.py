#We can also use google colab
#But starting the basic way

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import LabelEncoder

#Load the data using pandas
dataset =  pd.read_csv('Data.csv')

#After loading the data.
#We will divide the data into two parts
#Feature and dendentant variables
#In our case Feature would be x
#Dependnt will be you y (dependent variables followed by y)
x = dataset.iloc[:, :-1].values
y = dataset.iloc[:,-1].values
print(type(x))
print(x)
print(y)

#Do more sample on iloc
imputer = SimpleImputer(missing_values=np.nan,strategy='mean')
imputer.fit(x[:,1:3])
x[:,1:3] = imputer.transform(x[:,1:3])
print(x)



#Categorical encoding
#If we have data like gender /countries we can use categorical encoding
ct = ColumnTransformer(transformers=[('encoder', OneHotEncoder(), [0])], remainder='passthrough')
x = np.array(ct.fit_transform(x))
print(x)


le = LabelEncoder()
y = le.fit_transform(y)
print(y)

#Feature scalling
#Get all the data of  feature variables in the same range
#if the ranges are not good then one feature will dominate other feature
#Not all models need feature scalling

#Standardization and Normalization
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
x = sc.fit_transform(x)
print(x)

# Splitting the dataset into the Training set and Test set
#Over fitting when it learns too much
#under fitting when data is too less
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 0)
print(X_train)
print(X_test)
print(y_train)
print(y_test)