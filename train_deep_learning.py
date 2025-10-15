"""
Deep Learning Model Training Script
Trains neural network models using TensorFlow/Keras
"""

import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
import config

# Load data
print("Loading data...")
training_data = pd.read_csv('Training.csv')

X = training_data.drop('prognosis', axis=1).values
y = training_data['prognosis'].values

# Encode labels
le = LabelEncoder()
y_encoded = le.fit_transform(y)
y_categorical = keras.utils.to_categorical(y_encoded)

# Split data
X_train, X_val, y_train, y_val = train_test_split(
    X, y_categorical, test_size=config.validation_split, random_state=config.random_state
)

# Scale features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_val_scaled = scaler.transform(X_val)

# Build Deep Learning Model
print("Building Deep Learning Model...")
model = keras.Sequential([
    layers.Dense(256, activation='relu', input_shape=(X_train.shape[1],)),
    layers.Dropout(config.dl_dropout_rate),
    layers.Dense(128, activation='relu'),
    layers.Dropout(0.2),
    layers.Dense(len(le.classes_), activation='softmax')
])

model.compile(
    optimizer=keras.optimizers.Adam(learning_rate=config.dl_learning_rate),
    loss='categorical_crossentropy',
    metrics=['accuracy']
)

# Train model
print("Training Deep Learning Model...")
history = model.fit(
    X_train_scaled, y_train,
    validation_data=(X_val_scaled, y_val),
    epochs=config.dl_epochs,
    batch_size=config.dl_batch_size,
    callbacks=[
        keras.callbacks.EarlyStopping(patience=config.early_stopping_patience),
        keras.callbacks.ModelCheckpoint('model_weights.h5', save_best_only=True)
    ]
)

# Save model
model.save('deep_learning_model.h5')
print("Deep Learning Model saved!")
