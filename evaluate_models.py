"""
Model Evaluation Script
Evaluates all trained models and generates performance metrics
"""

import pickle
import pandas as pd
import numpy as np
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, classification_report
from sklearn.model_selection import train_test_split
import json

# Load data
training_data = pd.read_csv('Training.csv')
testing_data = pd.read_csv('Testing.csv')

X_test = testing_data.drop('prognosis', axis=1)
y_test = testing_data['prognosis']

# Load models
models = {
    'Random Forest': 'disease_classifier_model.pkl',
    'XGBoost': 'xgboost_model.pkl',
    'SVM': 'svm_model.pkl',
    'Naive Bayes': 'naive_bayes_model.pkl',
    'KNN': 'knn_model.pkl',
    'Ensemble': 'ensemble_model.pkl'
}

results = {}

for model_name, model_path in models.items():
    try:
        with open(model_path, 'rb') as f:
            model = pickle.load(f)
        
        # Make predictions
        y_pred = model.predict(X_test)
        
        # Calculate metrics
        accuracy = accuracy_score(y_test, y_pred)
        precision = precision_score(y_test, y_pred, average='weighted')
        recall = recall_score(y_test, y_pred, average='weighted')
        f1 = f1_score(y_test, y_pred, average='weighted')
        
        results[model_name] = {
            'accuracy': accuracy,
            'precision': precision,
            'recall': recall,
            'f1_score': f1
        }
        
        print(f"{model_name}:")
        print(f"  Accuracy: {accuracy:.4f}")
        print(f"  Precision: {precision:.4f}")
        print(f"  Recall: {recall:.4f}")
        print(f"  F1-Score: {f1:.4f}\n")
        
    except Exception as e:
        print(f"Error evaluating {model_name}: {e}\n")

# Save results
with open('model_evaluation_results.json', 'w') as f:
    json.dump(results, f, indent=4)

print("Evaluation completed! Results saved to model_evaluation_results.json")
