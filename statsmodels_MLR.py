import pandas as pd
price = [160,180,200,220,240,260,280]
sale = [126,103,82,75,82,40,20]
cars = [0,9,19,5,25,1,20]
priceDF = pd.DataFrame(price, columns=list('x'))
saleDF = pd.DataFrame(sale, columns=list('y'))
carsDf = pd.DataFrame(cars, columns=list('z'))
houseDf = pd.concat([priceDF,saleDF,carsDf],axis=1)
print(houseDf)

# fit the model by giving the dependent (number of units sold) "Y" 
# and independent variables (price of the house, number of cars sold).
import statsmodels.api as sm
X = houseDf.drop(['y'], axis=1)
y = houseDf.y
Xc = sm.add_constant(X)
linear_regression = sm.OLS(y,Xc)
fitted_model = linear_regression.fit()

print(fitted_model.summary())

#Coef column gives the value of estimated coefficients (B0, B1, B2 etc.)
#If the coef is zero then that independent variable does not predict the dependent variable correctly.
#Std err denotes how much each coefficient varies from the estimated value

#t-value - = Estimated coef/stderr
#P(>|t|) how likely the estimated value is zero
# This value also indicates how significant a variable is to a model.
# The smaller the value, the more significant a given variable is to the model.
# it is better to remove variables with higher values of `P(>|t|)`
# Choose the coef with low Pr(>|t|) value

# Handling Multicollinearity
# A good practice while fitting multiple regression model is to check if there is any correlation among the independent variables.
# In python, for a random array X the command to find correlation is X.corr()
# Reject that variable with correlation outside the range -0.7 and 0.7 with any other variable.

# HANDS ON:
from sklearn.datasets import load_boston
import pandas as pd
boston = load_boston()
dataset = pd.DataFrame(data=boston.data, columns=boston.feature_names)
dataset['target'] = boston.target
print(dataset.head())

# create a datframe named as 'X' such that it includes all the feature columns 
# and drop the target column. 
# assign the 'target' columns to variiable Y
X = dataset.drop(['target'], axis=1)
Y = dataset['target']

# Now the dataframe X has just the features that influence the target
# print the correlation matrix for dataframe X. Use '.corr()' function to compute correlation matrix
# from the correlation matrix note down the correlation value between 'CRIM' and 'PTRATIO' and assign it to variable 'corr_value'

print(X.corr())                   #print correlation matrix for X
corr_value = 0.289946

# initalize the OLS model with target Y and dataframe X(features), 
# make sure you add constant to input X
# fit the model and print the summary

import statsmodels.api as sm
Xc = sm.add_constant(X)
linear_regression = sm.OLS(Y,Xc)
fitted_model = linear_regression.fit()
print(fitted_model.summary())


# FEATURE SCALING
# 1. Normalization : recscaling to range of [-1,1]
from sklearn import preprocessing
import numpy as np
sampleData = np.array([[ -3., -1.,  4.]])
normalized_sampleData = preprocessing.normalize(sampleData)
print("\nNormalized data is: ",normalized_sampleData)

# 2. Standardization : removing the arithmetic mean and dividing by the standard deviation.
from sklearn.preprocessing import StandardScaler
X = np.array([[1,2,3,4,5]])
rescaledX = StandardScaler().fit_transform(X)
print("\nStandardized data is: ",rescaledX)
