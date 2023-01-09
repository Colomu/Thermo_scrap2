import os
import pandas as pd
import numpy as np 

from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import GridSearchCV
from sklearn.linear_model import SGDRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score, explained_variance_score, mean_absolute_error, mean_squared_error
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from typing import Type
from typing import Dict, Any, Tuple, Type
from xgboost import XGBRegressor
Model = Type[Any] 

from math import sqrt
from itertools import product


# Import the load_airbnb function from the tabular_data module
from tabular_data import load_airbnb

# Load the Airbnb data with the Price column as the labels
features, labels = load_airbnb(label='Price_Night')

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(features, labels, train_size=0.80, test_size = 0.2, random_state=15)
X_train, X_val, y_train, y_val = train_test_split(X_train, y_train, test_size=0.2, random_state=42)

print(X_train.shape)
print(X_test.shape)
print(y_train.shape)
print(y_test.shape)
print(X_val.shape)
print(y_val.shape)


# Create a pipeline with a SimpleImputer for filling missing values
# and a StandardScaler for scaling the data
numeric_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='mean')),
    ('scaler', StandardScaler())
])

# Create a ColumnTransformer to apply the numeric transformation
# to the numerical columns of the data
preprocessor = ColumnTransformer(transformers=[
    ('num', numeric_transformer, features.columns)
])

# Create a pipeline with the preprocessor and the SGDRegressor model
model = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('regressor', SGDRegressor(random_state=42))
])

# Fit the model to the training data
model.fit(X_train, y_train)

# Use the model to make predictions on the test data
predictions = model.predict(X_test)

# Calculate the mean squared error of the model
mse = mean_squared_error(y_test, predictions)
rmse = sqrt(mse)
print("RMSE:", rmse)

# Calculate the R^2 score for the training and test sets
r2_train = r2_score(y_train, model.predict(X_train))
r2_train = r2_score(y_train, model.predict(X_train))

print("R^2 Score:", r2_train)


def tune_regression_model_hyperparameters(X_train, y_train):
    xgb_model = XGBRegressor(random_state = 2021)

    # make a dictionary of hyperparameter values to search
    search_space = {
        "n_estimators" : [100, 200, 500],
        "max_depth" : [3, 6, 9],
        "gamma" : [0.01, 0.1],
        "learning_rate" : [0.001, 0.01, 0.1, 1]
    }

    # make a GridSearchCV object
    GS = GridSearchCV(estimator = xgb_model,
                      param_grid = search_space,
                      scoring = ["r2", "neg_root_mean_squared_error"], #sklearn.metrics.SCORERS.keys()
                      refit = "r2",
                      cv = 5,
                      verbose = 4)

    GS.fit(X_train, y_train)

    print(GS.best_estimator_) # to get the complete details of the best model
    print(GS.best_params_) # to get only the best hyperparameter values that we searched for
    print(GS.best_score_) # score according to the metric we passed in refit

# call the function
tune_regression_model_hyperparameters(X_train, y_train)
