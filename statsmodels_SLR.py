# statsmodels is a complement to scipy package
# provides the following :
# Descriptive Statistics
# Estimation and Inference for statistical Models

import pandas as pd

price = [160,180,200,220,240,260,280]  # price of house

sale = [126,103,82,75,82,40,20] # no. of units sold

priceDF = pd.DataFrame(price, columns=list('x'))

saleDF = pd.DataFrame(sale, columns=list('y'))

houseDf = pd.concat((priceDF, saleDF),axis=1)

print(priceDF)
print(saleDF)
print(houseDf)

import statsmodels.formula.api as smf

smfModel = smf.ols('y~x',data=houseDf).fit()

print(smfModel.summary())

#In the output
# Dep. Variable: The Dependent Variable
# Model: Algorithm used. Here, it is Ordinary Least Squares
# Method: Parameter Fitting method. Here, it is Least Squares
# No. Observations: Number of rows used for model fitting.
# DF Residuals: The degrees of freedom of the residuals (Difference between the number of observations and parameters).
# DF Model: The degrees of freedom of the model (The number of parameters estimated in the model excluding the constant term) .
# R-squared: Measure that says how well the model has performed with respect to the baseline model.


## HANDS ON 1 
from sklearn.datasets import load_boston
import pandas as pd

# using boston housing price dataset
boston = load_boston()
dataset = pd.DataFrame(data=boston.data, columns=boston.feature_names)
dataset['target'] = boston.target
print("BOSTON DATA SET")
print(dataset.head())

# The 'target' column has the dependent values(housing prices) and rest of the colums are the independent values that influence the target values
# Lets find the relation between 'housing price' and 'average number of rooms per dwelling' using stats model
# Assign the values of column "RM"(average number of rooms per dwelling) to variable X
# Similarly assign the values of 'target'(housing price) column to variable Y
import statsmodels.api as sm
X = dataset['RM']
Y = dataset['target']
X = sm.add_constant(X)
print("Average Number of Rooms per dwelling is:")
print(X)
print("Housing price is:")
print(Y)

# initialise the OLS model by passing target(Y) and attribute(X).Assign the model to variable 'statsModel'
# fit the model and assign it to variable 'fittedModel', make sure you add constant term to input X'
fittedModel = sm.OLS(Y,X).fit()
print("FITTED MODEL SUMMARY FOR BOSTON")
print(fittedModel.summary())
print('Rsquared value is: ',fittedModel.rsquared)
print('Model parameters are: ',fittedModel.params)