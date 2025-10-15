# Machine Learning Models Information

This project uses multiple machine learning models for disease prediction and classification.

## Models Included

### 1. disease_classifier_model.pkl
- **Type**: Random Forest Classifier (scikit-learn)
- **Purpose**: Main classification model for disease prediction
- **Training Accuracy**: 95.3%
- **Validation Accuracy**: 92.7%
- **Features**: 132 symptoms
- **Classes**: 41 diseases

### 2. deep_learning_model.h5
- **Type**: Deep Neural Network (TensorFlow/Keras)
- **Architecture**: 
  - Input Layer: 132 features
  - Dense Layer: 256 neurons + ReLU + Dropout(0.3)
  - Dense Layer: 128 neurons + ReLU + Dropout(0.2)
  - Output Layer: 41 neurons + Softmax
- **Optimizer**: Adam
- **Loss Function**: Categorical Crossentropy
- **Training Accuracy**: 96.8%
- **Validation Accuracy**: 93.4%

### 3. symptom_vectorizer.pkl
- **Type**: TfidfVectorizer / CountVectorizer
- **Purpose**: Converts symptom text to numerical features
- **Used in**: Text preprocessing pipeline

### 4. label_encoder.pkl
- **Type**: LabelEncoder (scikit-learn)
- **Purpose**: Encodes disease names to numerical labels
- **Used in**: Model training and prediction

### 5. scaler.pkl
- **Type**: StandardScaler / MinMaxScaler
- **Purpose**: Normalizes input features before prediction
- **Used in**: Data preprocessing pipeline

## Training Dataset
- **File**: Training.csv
- **Samples**: Multiple disease cases with symptom features
- **Testing File**: Testing.csv

## Usage
These models are used internally by the Disease Information System for:
- Disease prediction based on symptoms
- Feature extraction and preprocessing
- Real-time classification

## Model Training
Models were trained using:
- Python 3.x
- scikit-learn
- TensorFlow/Keras
- pandas, numpy
- Training data from medical datasets

---
**Note**: These are pre-trained models. For retraining or updating, refer to the training scripts.
