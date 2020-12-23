import numpy as np
import pandas as pd
import Constants

churn_file_path = Constants.DATA_PATH+'/churn.csv'


# (1) DATA ANALYSIS
## (1.1) DATA LOADING
#To read csv file
churn = pd.read_csv(churn_file_path, sep=',')

# (1.2) DATA ANALYSIS
# Data Size or Shape
print("Churn data shape is: ",churn.shape)

# Column Names
print("Churn Column List is: ",list(churn.columns))

# Describe data staticstics
print("Churn Description: ",churn.describe())

# First 3 rows
print("Churn first 3 rows: ",churn.head(3))

# (1.3) Target Identification
# Target is the class/category to which the data will be assigned.
# the aim is to identify whether the customer will churn or not.
# By observing the columns, the Churn? column has values True. or False. 
# We can hence call this case study, a Binary Classification since it has only two possible outcomes.

# Identifying the outcome/target variable.
# Churn = True. means customer will churn. 
churn_target=churn['Churn?'] 
print("'Churn?' column is Target Variable. Column values look like: ")
print(churn_target)

# (1.4) Feature Identification
# In any classification problem, identifying the right features plays a 
# major role. So, how do we identify the features(columns) that influence 
# the prediction.

# In our case by analyzing the dataset, we can understand that the columns 
# like Phone Number might be irrelevant as they are not dependent on call 
# usage pattern.

# Since Churn? is our target variable, we will be removing it from the 
# feature set.

# With these assumptions we will extract all the relevant columns 
# required for our classification.
cols_to_drop = ['Phone','Churn?']
#axis=1 depicts drop along columns
churn_feature = churn.drop(cols_to_drop,axis=1)
print("Churn feature columns are: ")
print(churn_feature)

# (2) PREPROCESSING OF DATA
# The raw data usually contains noise, missing values, and outliers.
# Also, The dimensionality of the data may be high in many cases.
# The first and foremost step in any data analysis task is to assess 
# the data quality.
#  Depending on the type of the data and data quality, 
#  we have to choose the appropriate pre-processing techniques

# Categorical Data
# The data which can be grouped into some kind of category or 
# multiple categories are known as categorical data.

# For example, in our case study the telecom users can be grouped by state,
# so State can be considered as a categorical variable. 
# Similar is the case for Area Code.

# The data represented in yes/no fashion can also be considered as 
# categorical data. For example, the people with 
# International plan(Int'l plan=yes) can be considered as a group.
# Hence, Int'l Plan is also a categorical variable.

# In order to Identify the categorical variable in a data :
churn_categorical = churn.select_dtypes(include=[object])
print("Categorical columns identified are: ")
print(churn_categorical)


# Handling Categorical Data
# Categorical data has a lot of hidden information. 
# It is important to treat such variables.

# Also, most of the machine learning algorithms in python (sklearn library) 
# requires input features as numerical arrays. 
# If the categorical data is given as such, it will result in an error. 
# The following are some methods to deal such variables:

# Convert to boolean
# Label Encoding
# One hot Encoding

# Convert to boolean
# The 'yes'/'no' type categorical variables can be converted to boolean values( True/False). 
# The Numpy array package in python will automatically convert it to 1 or 0.

# In our example,the columns Int'l Plan, VMail Plan are 
# categorical variables with yes/no values.

#Changing the 'yes or no' values to boolean
yes_no_cols = ["Int'l Plan","VMail Plan"]
churn_feature[yes_no_cols] = churn_feature[yes_no_cols] == 'yes'
print("Int'l Plan converted to boolean: ")
print(churn_feature["Int'l Plan"])

# Label Encoding
# Label encoding is a technique used to map non-numerical labels 
# to numerical labels. The numerical values are encoded with values 
# ranging from 0 : N (no of unique labels).
from sklearn import preprocessing
label_encoder = preprocessing.LabelEncoder()
churn_feature['Area Code'] = label_encoder.fit_transform(churn_feature['Area Code'])
print("Area code after label encoding: ")
print(churn_feature['Area Code'])
# After doing label encoding, the Area Code column is converted to numerical values.

# Note: Make sure that the values in the label encoded fields 
# does not overlap with any other columns within the dataset.

# One Hot Encoding
# One Hot Encoding / Dummy Coding is one of the preprocessing technique 
# that maps the categorical features onto a set of columns 
# that has values 1 or 0 to represent the presence or absence of that feature.
print('Churn data size before one hot encoding',churn_feature.shape)
print('No of unique states',len(churn_feature['State'].unique()))

#Give the feature and columns to one hot encode in 'columns' 
# and column rename prefix in 'prefix'
churn_dumm=pd.get_dummies(churn_feature, columns=["State"], prefix=["State"])

print('Churn data size after one hot encoding',churn_dumm.shape)
#converting to numpy matrix
churn_matrix = churn_dumm.values.astype(np.float)
# In this case, we have 51 unique columns being created with 
# headers State_<STATE_CODE>.



# Missing Values
# If we encounter any missing values for any feature in our dataset, we need to 
# handle those values for better classification.
# Missing Inputs : Strategies
### By deleting the observations
# If we have sufficient number of observations in our data, we can delete those rows
#  or observations containing missing values. Make sure that deletion of missing inputs 
# will not create any bias.
### By deleting the variables
# We can drop those variables based on a threshold. If it has more than 
# 50% missing values, we can eliminate those features. If one variable is 
# having 20% of missing values, we can impute that variable 
# rather than dropping it.
### Imputing
# The missing values can be replaced by taking the mean, median or mode of the 
# values present in a particular column.
from sklearn.impute import SimpleImputer
#Missing values replaced by mean
imp=SimpleImputer(missing_values=np.nan,strategy='mean',fill_value=None,verbose=0,copy=True)
#Fit to data, then transform it.
churn_matrix=imp.fit_transform(churn_matrix)
# In our dataset, we do not have any missing values. if we did, 
# the mean is taken for the column which has the value NaN and imputed.


#Standardization
# Standardization is a technique for re-scaling variable to a mean of zero 
# and standard deviation of one.

# It is used to transform the data to its center by ignoring the 
# shape of the distribution.

# The mean is subtracted from each value which results to a mean of zero. 
# Then, the difference is divided by its standard deviation, resulting in 
# a standard deviation of one.

from sklearn.preprocessing import StandardScaler
#Standardize the data by removing the mean and scaling to unit variance
scaler = StandardScaler()
#Fit to data, then transform it.
churn_matrix = scaler.fit_transform(churn_matrix)


# Class Imbalance
# Class imbalance occurs when the number of data samples of a class 
# is less than the number of data samples of another class.

# Machine learning algorithms works better when each class samples are roughly 
# equal. In classification problems, the variation in number of data samples 
# will lead to model fitting issues.

# How to handle class imbalance:
# One technique to solve the class imbalance problem is balancing the dataset.
##  Under-sampling will sample the majority class to same size as the minority class.
##  Oversampling will sample the minority class to same size as the majority class.
#In the algorithm level, we can adjust the class weight, decision threshold or 
# modify an algorithm to perform on imbalanced data.




# Classification Algorithms
# There are various algorithms to solve the classification problems. 

# The following are the steps involved in building a classification model:
# Initailize the classifier to be used.

# Train the classifier - All classifiers in scikit-learn uses a fit(X, y) method
#  to fit the model(training) for the given train data X and train label y.

# Predict the target - Given an unlabeled observation X, the predict(X) returns 
# the predicted label y.

# Evaluate the classifier model - The score(X,y) returns the score for the
# given test data X and test label y.

# Train and Test Data
# partitioning the data into train and test for building the classifier model.
#  This split will be used for explanation of classification algorithms.

seed=7 #To generate same sequence of random numbers
from sklearn.model_selection import train_test_split
#Splitting the data for training and testing(90% train,10% test)
train_data,test_data, train_label, test_label = train_test_split(churn_matrix, churn_target, test_size=.1,random_state=seed)


# The decision tree model predicts the class/target by learning 
# simple decision rules from the features of the data.
from sklearn.tree import DecisionTreeClassifier
#Initializing decision tree classifier
classifier=DecisionTreeClassifier(random_state=seed)
#Model training
classifier = classifier.fit(train_data, train_label)
#After being fitted, the model can then be used to predict the output.
churn_predicted_target=classifier.predict(test_data)
#Evaluating the classifier
score = classifier.score(test_data, test_label)
print('Decision Tree Classifier : ',score)


# Naive Bayes classifiers are a family of simple probabilistic classifiers 
# based on applying Bayes' theorem with strong (naive) independence assumptions 
# between the features."
from sklearn.naive_bayes import GaussianNB
classifier=GaussianNB()
classifier = classifier.fit(train_data, train_label)
churn_predicted_target=classifier.predict(test_data)
score = classifier.score(test_data, test_label)
print('Naive Bayes : ',score)

# Stochastic Gradient Descent Classifier
# Used for large scale learning
# Supports different loss functions & penalties for classification
from sklearn.linear_model import SGDClassifier
classifier =  SGDClassifier(loss='modified_huber', shuffle=True,random_state=seed)
classifier = classifier.fit(train_data, train_label)
churn_predicted_target=classifier.predict(test_data)
score = classifier.score(test_data, test_label)
print('SGD classifier : ',score)

# Support Vector Machine(SVM) is effective in high dimensional spaces.
# Effective in cases where number of dimensions is greater than the number of samples.
# It works really well with clear margin of separation.
from sklearn.svm import SVC
classifier = SVC(kernel="linear", C=0.025,random_state=seed)
classifier = classifier.fit(train_data, train_label)
churn_predicted_target=classifier.predict(test_data)
score = classifier.score(test_data, test_label)
print('SVM Classifier : ',score)

# Random Forest Classifier
# Controls over fitting
# A random forest fits a number of decision tree classifiers on various 
# sub-samples of the dataset and uses averaging to improve the predictive accuracy.
from sklearn.ensemble import RandomForestClassifier
classifier = RandomForestClassifier(max_depth=5, n_estimators=10, max_features=10,random_state=seed)
classifier = classifier.fit(train_data, train_label)
churn_predicted_target=classifier.predict(test_data)
score = classifier.score(test_data, test_label)
print('Random Forest Classifier : ',score)

###################
# Model Tuning
# The classification algorithms in machine learning are parameterized. 
# Modification of any of those parameters can influence the results. 
# So algorithm/model tuning is very essential to find out the best model.

# For example, lets take Random Forest Classifier and change the values of 
# few parameters (n_ estimators,max_ features)
from sklearn.ensemble import RandomForestClassifier
classifier = RandomForestClassifier(max_depth=5, n_estimators=15, max_features=60,random_state=seed)
classifier = classifier.fit(train_data, train_label)
score=classifier.score(test_data, test_label)
print('Random Forest classification after model tuning',score)



#######
# Partitioning Data
# It is a mistake to test and train on same dataset because the classifier 
# would fail to predict correctly for any unseen data. 
# This could result in overfitting.

# To avoid this problem,
# We split our data to train set, validation set and test set.
# 1.Training Set: The data used to train the classifier.
# 2.Validation Set: The data used to tune the classifer model parameters 
# i.e, to understand how well the model has been trained (a part of training data).
# 3.Testing Set: The data used to evaluate the performance of the classifier
# (unseen data by the classifier).
# This will help us to know the efficiency of our model.

# Cross Validation
# Cross validation is a model validation technique to evaluate the performance 
# of a model on unseen data (validation set).
# It is a better estimate to evaluate - 
# testing accuracy than training accuracy on unseen data.

# Points to remember :
# Cross validation gives high variance if the testing set and training set 
# are not drawn from same population.
# Allowing training data to be included in testing data will not give actual 
# performance results.
# In cross validation, the number of samples used for training the model is reduced 
# and the results depend upon the choice of pair of training and testing sets.

# Stratified Shuffle Split
# StratifiedShuffleSplit would suit our case study (Churn) as the dataset 
# has a class imbalance which can be seen from the below code snippet:

# The StratifiedShuffleSplit splits the data by taking equal number of samples 
# from each class in a random manner.

from sklearn.model_selection import StratifiedShuffleSplit
sss = StratifiedShuffleSplit(n_splits=1,test_size=0.1, random_state=7)
sss.get_n_splits(churn_matrix,churn_target)
print(sss)
#test_size=0.1 denotes that 10 % of the dataset is used for testing.

# This selection is then used to split the data into test and train sets.

from sklearn.neighbors import KNeighborsClassifier
from sklearn.multiclass import OneVsRestClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn import svm
classifiers = [
    DecisionTreeClassifier(),
    GaussianNB(),
    SGDClassifier(loss='modified_huber', shuffle=True),
    SVC(kernel="linear", C=0.025),
    KNeighborsClassifier(),
    OneVsRestClassifier(svm.LinearSVC()),
    RandomForestClassifier(max_depth=5, n_estimators=10, max_features=10),
    AdaBoostClassifier(),
   ]
for clf in classifiers:
    score=0
    for train_index, test_index in sss.split(churn_matrix,churn_target):
        X_train, X_test = churn_matrix[train_index], churn_matrix[test_index]
        y_train, y_test = churn_target[train_index], churn_target[test_index]
        clf.fit(X_train, y_train)
        score=score+clf.score(X_test, y_test)
    print(score)

# The above code uses ensemble of classifiers for cross validation. 
# It helps to select the best classifier based on the cross validation scores. 
# The classifier with the highest score can be used for building the classification model.

# Note: You may add or remove classifiers based on the requirement.
    
    
    
    
# PERFORMANCE EVALUATION MEASURES
    
# Classification Accuracy
# The classification accuracy is defined as the percentage of correct predictions.

from sklearn.metrics import accuracy_score
print('Accuracy Score',accuracy_score(test_label,churn_predicted_target))  
# This simple classification accuracy will not tell us the types of errors
# by our classifier.
# Its just an easiest method, but it will not give us the latent distribution 
# of response values.

# Confusion Matrix
# It is a technique used to evaluate the performance of a classifier.

# It visually depicts the performance in a tabular form that has 2 dimensions 
# namely “actual” and “predicted” sets of data.

# The rows and columns of the table shows the count of false positives, 
# false negatives, true positives and true negatives.

from sklearn.metrics import confusion_matrix
print('Confusion Matrix',confusion_matrix(test_label,churn_predicted_target))
# The first parameter shows true values and second parameter shows predicted values.

###                            predicted data:
###                            positive         negative
###actual data: positive       TP              FN
###actual data: negative       FP              TN

#TP (True Positive) - The number of correct predictions that the occurrence is positive
#FP (False Positive) - The number of incorrect predictions that the occurrence is positive
#FN (False Negative) - The number of incorrect predictions that the occurrence is negative
#TN (True Negative)- The number of correct predictions that the occurrence is negative
#TOTAL - The total number of occurrence


# The classification_report function shows a text report showing the commonly
# used classification metrics.

from sklearn.metrics import classification_report
target_names = ['False.', 'True.']
print(classification_report(test_label, churn_predicted_target, target_names=target_names))

# Precision
# When a positive value is predicted, how often is the prediction correct?

# Recall
# It is the true positive rate.
# When the actual value is positive, how often is the prediction correct?
