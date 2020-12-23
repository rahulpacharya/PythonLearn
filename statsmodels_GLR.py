# A dataset is created with scores a team got 
# and Won or lost that respective game
# This is to illustrate how the score is helping us 
# predict the binary outcome win/lose

import pandas as pd
import statsmodels.api as sm
import statsmodels.formula.api as smf
#from __future__ import print_function
Scores = [(200,1),(100,0),(150,1),(320,1),(270,1),(134,0),(322,1),(140,0),(210,0),(199,0)]
Labels = ['Score','Win']
df = pd.DataFrame.from_records(Scores, columns=Labels)
glm_binom = sm.GLM(df.Win, df.Score, family=sm.families.Binomial())
res = glm_binom.fit()
print(res.summary())

# The value of the score coef tells us how it is able to 
# tell us to what extent it is able to 
# predict the likilihood of winning a game 

##########################
## Machince learning perspective of the above using scikit
# The previous example was a statistical perspective. 
# The current example will give a machine learning perspective.

from sklearn.datasets import make_classification
X, y = make_classification(n_samples=100, n_features=2,
                           n_informative=2, n_redundant=0,
                           n_clusters_per_class=1,
                           class_sep = 2.0, random_state=101)

#The above code creates a sample dataset for a binary classification problem.
#2 features are created and the 2 classes are created for the given features
print("X Is: ",X)
print("y is: ",y)

# The output above is the data that is fed to the logistic regression model.
# This is an example for Binary Classification.

## Plotting the data
import matplotlib.pyplot as plt
plt.scatter(X[:, 0], X[:, 1], marker='o', c=y,
            linewidth=0, edgecolor=None)
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.show()

#Splitting the data
# we are splitting the training and test sets.
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y.astype(float),test_size=0.33, random_state=101)

# Following is how to fit a logistic regression model 
# and view the classification report.
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
clf = LogisticRegression()
clf.fit(X_train, y_train.astype(int))
y_clf = clf.predict(X_test)
print(classification_report(y_test, y_clf))

#Precision = TP/(TP + FP)
# Precision is similar to accuracy but looks at only the 
# positively predicted data.

#Recall = TP / (TP + FN)
# Recall is also similar to accuracy, it looks at only the 
# relevant data.

# ROC Curve
from sklearn.metrics import roc_curve
from sklearn.metrics import auc
# Compute fpr, tpr, thresholds and roc auc
fpr, tpr, thresholds = roc_curve(y_test, y_clf)
#roc_auc = auc(y_test, y_clf)
# Plot ROC curve
#plt.plot(fpr, tpr, label='ROC curve (area = %0.3f)' % roc_auc)
plt.plot([0, 1], [0, 1], 'k--')  # random predictions curve
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.0])
plt.xlabel('False Positive Rate or (1 - Specifity)')
plt.ylabel('True Positive Rate or (Sensitivity)')
plt.title('Receiver Operating Characteristic')
plt.legend(loc="lower right")

#Confusion matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_clf)
print(cm)

# Accuracy for this model is 
# (14+18) / (14+1+0+18) = 0.96969

# Sensitivity for the model is 100%

# Specificity for the model is 94%

# Based on the numbers we can interpret that 
# the model is able to clearly separate the 
# data into 2 classes.

# The model is also able to designate the 
# individual numbers that do not belong to a 
# specific class as negative.


# Hands On
from sklearn import datasets
iris = datasets.load_iris()
iris_X = iris.data
iris_y = iris.target
#print(iris_X) print(iris_y)
print(iris.feature_names)
print(iris.target_names)

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(iris_X, iris_y.astype(float),test_size=0.33, random_state=101)


from sklearn.linear_model import LogisticRegression
model = LogisticRegression()
model.fit(X_train, y_train.astype(int))

y_pred = model.predict(X_test)

from sklearn.metrics import classification_report
print(classification_report(y_test, y_pred))

###########################################
# POISSON REGRESSION MODEL FOR COUNT DATA
###########################################

import numpy as np
import pandas as pd
import statsmodels.api as sm

dataset = pd.DataFrame({'A':np.random.rand(100)*1000, 

                        'B':np.random.rand(100)*100,  

                        'C':np.random.rand(100)*10, 

                        'target':np.random.randint(0, 5, 100)})

#We are creating a sample dataframe . 
#The variables are random numbers.
#The Dependent variable signifies count data.
#The Independent variables are random numbers.

X = dataset[['A','B','C']]

X['constant'] = 1

y = dataset['target']

size = 1e5

nbeta = 3

# The code splits the dependent and the independent 
# variables. The required parameters are also set here.

fam = sm.families.Poisson()

pois_glm = sm.GLM(y,X, family=fam)

pois_res = pois_glm.fit()

print(pois_res.summary())

