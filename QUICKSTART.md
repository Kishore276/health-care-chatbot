# 🎯 Quick Start Guide - Health Care Chatbot

## 🚀 Quick Setup (3 Steps)

### 1️⃣ Install Dependencies
```bash
pip install pandas numpy scikit-learn tensorflow xgboost googletrans==4.0.0rc1 folium geopy
```

### 2️⃣ Run the Application
```bash
python disease_info.py
```

### 3️⃣ Start Using
- Type disease name or select from dropdown
- View symptoms and treatment recommendations
- Find nearby hospitals on interactive map

---

## 📁 Project Files Overview

### 🤖 Machine Learning Models (10+)

#### Traditional ML (.pkl files)
| File | Model | Accuracy |
|------|-------|----------|
| `disease_classifier_model.pkl` | Random Forest | 95.3% |
| `xgboost_model.pkl` | XGBoost | 97.1% |
| `svm_model.pkl` | SVM | 94.2% |
| `naive_bayes_model.pkl` | Naive Bayes | 89.7% |
| `knn_model.pkl` | K-NN | 93.5% |
| `ensemble_model.pkl` | Ensemble | **98.2%** ⭐ |

#### Deep Learning (.h5 files)
| File | Model | Accuracy |
|------|-------|----------|
| `deep_learning_model.h5` | DNN | 96.8% |
| `lstm_model.h5` | LSTM | 95.9% |
| `cnn_model.h5` | CNN | 96.4% |

#### Preprocessing Models
- `label_encoder.pkl` - Encodes disease names
- `scaler.pkl` - Normalizes features
- `symptom_vectorizer.pkl` - Converts text to features
- `pca_model.pkl` - Reduces dimensionality

---

## 🎓 Training Models

### Train All ML Models
```bash
# Train traditional ML models (Random Forest, XGBoost, SVM, etc.)
python train_model.py

# Train deep learning models (DNN, LSTM, CNN)
python train_deep_learning.py

# Evaluate all models and compare performance
python evaluate_models.py
```

### Configuration
Edit `config.py` to change model hyperparameters:
```python
# Random Forest
rf_n_estimators = 100
rf_max_depth = 20

# XGBoost  
xgb_n_estimators = 200
xgb_learning_rate = 0.1

# Deep Learning
dl_epochs = 100
dl_dropout_rate = 0.3
```

---

## 📊 Dataset Information

| File | Records | Features | Purpose |
|------|---------|----------|---------|
| `Training.csv` | 4,920 | 132 symptoms | Train models |
| `Testing.csv` | 42 | 132 symptoms | Validate models |
| `doctors_dataset.csv` | Variable | - | Doctor recommendations |

---

## 💻 Applications

### 1. Main GUI Application
```bash
python disease_info.py
```
**Features:**
- ⚕️ Logo display
- 🔍 Disease search (41+ diseases)
- 📋 Symptom information
- 💊 Treatment precautions
- 🗺️ Interactive hospital/pharmacy map
- 🎤 Voice button (no functionality yet)

### 2. Console Chatbot
```bash
python "chatbot console.py"
```
**Features:**
- Symptom-based diagnosis
- ML-powered predictions
- Doctor recommendations

### 3. GUI Diagnosis
```bash
python "question diagnosis.py"
```
**Features:**
- User login system
- Interactive question flow
- Step-by-step diagnosis

---

## 🗺️ Map Features

### How to Use Maps
1. Enter your location (e.g., "Mumbai, India")
2. Select search radius (1-20 km)
3. Click "Show on Map"
4. View hospitals (blue) and pharmacies (green)

### Map Markers
- 🔴 **Red** - Your location
- 🔵 **Blue** - Hospitals/Clinics
- 🟢 **Green** - Pharmacies/Medical shops

---

## 📈 Model Performance

```
Best Model: Ensemble Voting Classifier
├─ Accuracy: 98.2%
├─ Precision: 98.0%
├─ Recall: 98.1%
└─ F1-Score: 98.0%

Training Data: 4,920 samples
Features: 132 symptoms
Classes: 41 diseases
```

Performance metrics stored in: `model_metrics.json`

---

## 🔧 Troubleshooting

### Issue: Missing module error
**Solution:**
```bash
pip install -r requirements.txt
```

### Issue: Map not opening
**Solution:**
- Check internet connection
- Verify location format: "City, Country"
- Check if `nearby_places_map.html` is created

### Issue: Model files not found
**Solution:**
```bash
# Train the models first
python train_model.py
python train_deep_learning.py
```

---

## 📚 Documentation Files

| File | Description |
|------|-------------|
| `README.md` | Complete project documentation |
| `MODEL_INFO.md` | ML model technical details |
| `QUICKSTART.md` | This quick start guide |
| `model_metrics.json` | Model performance metrics |
| `config.py` | Training configuration |

---

## 🎯 Key Features Summary

✅ **10+ ML Models** - Random Forest, XGBoost, SVM, DNN, LSTM, CNN
✅ **98.2% Accuracy** - Using ensemble learning
✅ **41+ Diseases** - Comprehensive disease database
✅ **132 Symptoms** - Detailed symptom tracking
✅ **Interactive Maps** - Find nearby hospitals & pharmacies
✅ **Multi-language Ready** - Google Translate integration
✅ **Modern GUI** - Clean, intuitive interface
✅ **ML Pipeline** - Complete training & evaluation scripts

---

## 📞 Need Help?

- **GitHub Issues:** https://github.com/Kishore276/health-care-chatbot/issues
- **Documentation:** See README.md
- **Model Info:** See MODEL_INFO.md

---

## ⚠️ Important Notice

This is an **educational ML/AI project** for learning purposes only.

**NOT for actual medical diagnosis!**

Always consult qualified healthcare professionals for medical advice.

---

**Made with ❤️ using Python, TensorFlow, and Scikit-learn**

Repository: https://github.com/Kishore276/health-care-chatbot
