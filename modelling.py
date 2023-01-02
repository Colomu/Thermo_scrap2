import pandas as pd
from sklearn.linear_model import SGDRegressor
from sklearn.model_selection import train_test_split

# Import the load_airbnb function from the preprocessing module
from preprocessing import load_airbnb

# Load the Airbnb data with the Price_Night column as the labels
features, labels = load_airbnb(label='Price_Night')

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.2, random_state=42)

# Create an instance of the SGDRegressor model
model = SGDRegressor(max_iter=1000, tol=1e-3)

# Train the model on the training data
model.fit(X_train, y_train)

# Evaluate the model on the test data
test_score = model.score(X_test, y_test)

print(f'Test score: {test_score:.2f}')
