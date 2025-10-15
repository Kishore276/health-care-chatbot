"""
Model Training Script
This script trains multiple ML models for disease prediction
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.naive_bayes import MultinomialNB
from sklearn.neighbors import KNeighborsClassifier
import xgboost as xgb
import pickle
import config

# Load data
print("Loading training data...")
training_data = pd.read_csv('Training.csv')
testing_data = pd.read_csv('Testing.csv')

# Prepare features and labels
X = training_data.drop('prognosis', axis=1)
y = training_data['prognosis']

# Split data
X_train, X_val, y_train, y_val = train_test_split(
    X, y, test_size=config.validation_split, random_state=config.random_state
)

# Train Random Forest
print("Training Random Forest...")
rf_model = RandomForestClassifier(
    n_estimators=config.rf_n_estimators,
    max_depth=config.rf_max_depth,
    random_state=config.random_state
)
rf_model.fit(X_train, y_train)
with open('disease_classifier_model.pkl', 'wb') as f:
    pickle.dump(rf_model, f)

# Train XGBoost
print("Training XGBoost...")
xgb_model = xgb.XGBClassifier(
    n_estimators=config.xgb_n_estimators,
    max_depth=config.xgb_max_depth,
    learning_rate=config.xgb_learning_rate
)
xgb_model.fit(X_train, y_train)
with open('xgboost_model.pkl', 'wb') as f:
    pickle.dump(xgb_model, f)

# Train SVM
print("Training SVM...")
svm_model = SVC(
    kernel=config.svm_kernel,
    C=config.svm_C,
    gamma=config.svm_gamma
)
svm_model.fit(X_train, y_train)
with open('svm_model.pkl', 'wb') as f:
    pickle.dump(svm_model, f)

print("Training completed! Models saved.")
