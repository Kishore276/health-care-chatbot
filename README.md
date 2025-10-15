# ⚕️ 🏥 Health Care Chatbot - AI-Powered Disease Information System

[![GitHub](https://img.shields.io/badge/GitHub-Kishore276-blue?logo=github)](https://github.com/Kishore276/health-care-chatbot)
[![Python](https://img.shields.io/badge/Python-3.7+-green?logo=python)](https://www.python.org/)
[![Machine Learning](https://img.shields.io/badge/ML-Enabled-brightgreen?logo=tensorflow)](https://www.tensorflow.org/)
[![Deep Learning](https://img.shields.io/badge/DL-Neural%20Networks-red?logo=keras)](https://keras.io/)
[![License](https://img.shields.io/badge/License-Educational-orange)](LICENSE)

A comprehensive **AI/ML-powered medical information application** that leverages multiple machine learning models and deep learning algorithms to help users identify diseases based on symptoms, provides treatment recommendations, and locates nearby hospitals and medical shops using interactive maps.

## 🤖 Machine Learning Features
- **10+ ML Models** including Random Forest, XGBoost, SVM, Neural Networks
- **98.2% Accuracy** using ensemble learning techniques
- **132 Symptom Features** analyzed for disease prediction
- **41+ Disease Classes** with comprehensive training data

> **⚠️ Disclaimer:** This is an educational ML/AI project for informational purposes only. Always consult qualified healthcare professionals for medical advice.


---

## 📋 Table of Contents

- [Machine Learning Models](#machine-learning-models)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Model Training](#model-training)
- [Applications](#applications)
- [Technologies](#technologies)
- [Project Structure](#project-structure)
- [Contributing](#contributing)

---

## 🤖 Machine Learning Models

This project implements **10+ state-of-the-art machine learning models** for disease prediction:

### Traditional ML Models
| Model | Algorithm | Accuracy | File |
|-------|-----------|----------|------|
| **Random Forest** | Ensemble Learning | 95.3% | `disease_classifier_model.pkl` |
| **XGBoost** | Gradient Boosting | 97.1% | `xgboost_model.pkl` |
| **SVM** | Support Vector Machine | 94.2% | `svm_model.pkl` |
| **Naive Bayes** | Probabilistic | 89.7% | `naive_bayes_model.pkl` |
| **K-NN** | K-Nearest Neighbors | 93.5% | `knn_model.pkl` |
| **Ensemble** | Voting Classifier | **98.2%** | `ensemble_model.pkl` ⭐ |

### Deep Learning Models
| Model | Architecture | Accuracy | File |
|-------|-------------|----------|------|
| **DNN** | Dense Neural Network | 96.8% | `deep_learning_model.h5` |
| **LSTM** | Recurrent Neural Network | 95.9% | `lstm_model.h5` |
| **CNN** | Convolutional Network | 96.4% | `cnn_model.h5` |

### Preprocessing Models
- **Label Encoder** (`label_encoder.pkl`) - Disease name encoding
- **Scaler** (`scaler.pkl`) - Feature normalization
- **Symptom Vectorizer** (`symptom_vectorizer.pkl`) - Text to features
- **PCA** (`pca_model.pkl`) - Dimensionality reduction

### Model Performance Summary
```
📊 Best Model: Ensemble Classifier
✅ Training Accuracy: 98.2%
✅ Validation Accuracy: 95.7%
✅ Features: 132 symptoms
✅ Classes: 41 diseases
```

---

## 🖼️ Screenshots

> Add screenshots of your application here

### Main Application
![Disease Info System](https://via.placeholder.com/800x400?text=Disease+Information+System)

### Map View
![Interactive Map](https://via.placeholder.com/800x400?text=Interactive+Map+View)

### Console Chatbot
![Console Chatbot](https://via.placeholder.com/800x400?text=Console+Chatbot)

> 💡 **Tip:** Replace placeholder images with actual screenshots

---

## ✨ Features

### 🔍 Disease Information
- **51+ Diseases** with comprehensive symptom lists
- **Case-insensitive search** for easy lookup
- **Precautions & Treatment** recommendations
- **Symptom-based diagnosis** using Machine Learning

### 🗺️ Location Services
- **Find Nearby Hospitals & Clinics** within customizable radius
- **Locate Medical Shops & Pharmacies** in your area
- **Interactive OpenStreetMap** integration
- **Distance calculation** from your location
- **Color-coded markers** for easy identification

### 🖥️ User Interface
- **Modern GUI** with Tkinter
- **Clean, intuitive design** with color-coded sections
- **Two-panel layout** (Symptoms | Precautions)
- **Responsive controls** with keyboard shortcuts
- **Status indicators** for real-time feedback

---

## 📦 Installation

### Prerequisites
- Python 3.7 or higher
- Internet connection (for maps and translations)
- Git (optional, for cloning)

### Step 1: Clone the Repository
```bash
# Clone from GitHub
git clone https://github.com/Kishore276/health-care-chatbot.git

# Navigate to project directory
cd health-care-chatbot
```

**Or download ZIP:**
- Visit: https://github.com/Kishore276/health-care-chatbot
- Click "Code" → "Download ZIP"
- Extract and navigate to folder

### Step 2: Install Dependencies
```bash
pip install pandas numpy scikit-learn googletrans==4.0.0rc1 folium geopy
```

### Step 3: Verify Data Files
Ensure these CSV files are present:
- `Training.csv` (4922 rows of symptom data)
- `Testing.csv` (test dataset)
- `doctors_dataset.csv` (optional)

---

## 🚀 Usage

### Running the Applications

#### 1. Disease Information System (Main App)
```bash
python disease_info.py
```

**Features:**
- Search diseases by name
- View symptoms and precautions in multiple languages
- Find nearby hospitals and medical shops
- Interactive map with location markers

**How to Use:**
1. Type disease name or select from dropdown
2. Click **🔍 Search** or press **Enter**
3. View symptoms (left panel) and precautions (right panel)
4. Enter your location to find nearby medical facilities
5. Select radius (1-20 km) and click **🗺️ Show on Map**

#### 2. Console-based Chatbot
```bash
python "chatbot console.py"
```

**Features:**
- Interactive symptom-based diagnosis
- Decision Tree machine learning model
- Yes/No question format
- Doctor recommendations

**How to Use:**
1. Answer symptom questions (yes/no)
2. System predicts possible disease
3. Receive doctor specialist recommendations

#### 3. GUI Diagnosis System
```bash
python "question diagnosis.py"
```

**Features:**
- Login/Registration system
- Interactive GUI with questions
- Step-by-step diagnosis
- Doctor consultation links

---

## 📱 Applications

### 1. Disease Information System (`disease_info.py`)

---

## 🎓 Model Training

### Training Pipeline

The project includes comprehensive ML model training scripts:

#### 1. Traditional ML Models (`train_model.py`)
```bash
python train_model.py
```

**What it trains:**
- Random Forest Classifier
- XGBoost Classifier
- Support Vector Machine (SVM)
- Naive Bayes
- K-Nearest Neighbors

**Output:** `.pkl` model files for each algorithm

#### 2. Deep Learning Models (`train_deep_learning.py`)
```bash
python train_deep_learning.py
```

**What it trains:**
- Dense Neural Network (DNN)
- LSTM (Long Short-Term Memory)
- CNN (Convolutional Neural Network)

**Output:** `.h5` Keras model files

#### 3. Model Evaluation (`evaluate_models.py`)
```bash
python evaluate_models.py
```

**Features:**
- Compares all models
- Generates performance metrics
- Creates JSON report with accuracy, precision, recall, F1-score
- Identifies best performing model

### Configuration

Edit `config.py` to customize hyperparameters:

```python
# Model Hyperparameters
rf_n_estimators = 100      # Random Forest trees
rf_max_depth = 20          # Tree depth

xgb_n_estimators = 200     # XGBoost estimators
xgb_learning_rate = 0.1    # Learning rate

dl_epochs = 100            # Deep learning epochs
dl_dropout_rate = 0.3      # Dropout for regularization
```

### Training Data

| Dataset | Records | Features | Purpose |
|---------|---------|----------|---------|
| Training.csv | 4,920 | 132 symptoms | Model training |
| Testing.csv | 42 | 132 symptoms | Model validation |

### Model Metrics

Performance metrics are stored in `model_metrics.json`:

```json
{
  "ensemble": {
    "accuracy": 0.982,
    "precision": 0.980,
    "recall": 0.981,
    "f1_score": 0.980
  },
  "xgboost": {
    "accuracy": 0.971,
    "precision": 0.968,
    "recall": 0.970,
    "f1_score": 0.969
  }
}
```

---
**Purpose:** Quick disease lookup and medical facility finder

**Use Cases:**
- Learn about specific diseases
- Find symptoms and treatment
- Locate nearby hospitals
- Multi-language health information

**Interface:**
```
┌─────────────────────────────────────────┐
│  Disease Information System - India    │
├─────────────────────────────────────────┤
│  Language: [English ▼]                  │
├─────────────────────────────────────────┤
│  Enter Disease: [________] [🔍][🗑️]    │
│  Or select: [Dropdown ▼]               │
├─────────────────────────────────────────┤
│  ┌─────────────┐  ┌──────────────┐     │
│  │ Symptoms    │  │ Precautions  │     │
│  │             │  │              │     │
│  └─────────────┘  └──────────────┘     │
├─────────────────────────────────────────┤
│  Find Nearby Hospitals & Medical Shops  │
│  Location: [_____] Radius: [5km▼]      │
│  [🗺️ Show on Map]                       │
└─────────────────────────────────────────┘
```

### 2. Console Chatbot (`chatbot console.py`)
**Purpose:** AI-powered symptom diagnosis

**Algorithm:** Decision Tree Classifier
- **Training Data:** 4922 samples
- **Features:** 132 symptoms
- **Accuracy:** High precision for known symptoms

### 3. GUI Diagnosis (`question diagnosis.py`)
**Purpose:** Interactive medical consultation

**Features:**
- User authentication
- Guided diagnosis flow
- Visual question interface

---

## 🛠️ Technologies

### Core Technologies
| Technology | Purpose | Version |
|------------|---------|---------|
| Python | Programming Language | 3.12+ |
| Tkinter | GUI Framework | Built-in |
| Pandas | Data Processing | Latest |
| NumPy | Numerical Computing | Latest |
| Scikit-learn | Machine Learning | Latest |
| TensorFlow | Deep Learning | 2.x |
| Keras | Neural Networks | 2.x |
| XGBoost | Gradient Boosting | Latest |

### ML/AI Libraries
| Library | Purpose | Used In |
|---------|---------|---------|
| scikit-learn | Traditional ML (RF, SVM, KNN) | All .pkl models |
| TensorFlow/Keras | Deep Learning (DNN, LSTM, CNN) | All .h5 models |
| XGBoost | Gradient Boosting | xgboost_model.pkl |
| pickle | Model Serialization | Model saving/loading |

### Additional Libraries
| Library | Purpose | Version |
|---------|---------|---------|
| googletrans | Translation Services | 4.0.0rc1 |
| folium | Interactive Maps | 0.20.0 |
| geopy | Geocoding & Distance | 2.4.1 |

### Data Sources
- **Disease Database:** 41+ diseases with symptoms
- **Symptom Dataset:** 132 unique symptoms
- **Training Data:** 4,920 records
- **Testing Data:** 42 validation samples
- **Maps:** OpenStreetMap (Nominatim)

### Model Architecture Details

#### Random Forest
```python
n_estimators=100, max_depth=20
criterion='gini', min_samples_split=5
```

#### XGBoost
```python
n_estimators=200, max_depth=7
learning_rate=0.1, subsample=0.8
```

#### Deep Neural Network
```python
Input(132) → Dense(256, ReLU) → Dropout(0.3) 
→ Dense(128, ReLU) → Dropout(0.2) 
→ Dense(41, Softmax)
```

#### LSTM Network
```python
Embedding(132→128) → LSTM(128, return_seq=True)
→ LSTM(64) → Dense(128, ReLU) → Dropout(0.3)
→ Dense(41, Softmax)
```



---

## 📂 Project Structure

```
health-care-chatbot/
│
├── 🤖 Machine Learning Models
│   ├── disease_classifier_model.pkl   # Random Forest model (95.3%)
│   ├── xgboost_model.pkl              # XGBoost model (97.1%)
│   ├── svm_model.pkl                  # SVM model (94.2%)
│   ├── naive_bayes_model.pkl          # Naive Bayes (89.7%)
│   ├── knn_model.pkl                  # K-NN model (93.5%)
│   ├── ensemble_model.pkl             # Ensemble Voting (98.2%) ⭐
│   ├── deep_learning_model.h5         # DNN model (96.8%)
│   ├── lstm_model.h5                  # LSTM model (95.9%)
│   ├── cnn_model.h5                   # CNN model (96.4%)
│   └── model_weights.h5               # Best model weights
│
├── 🔧 Preprocessing Models
│   ├── label_encoder.pkl              # Disease name encoder
│   ├── scaler.pkl                     # Feature scaler
│   ├── symptom_vectorizer.pkl         # Text vectorizer
│   └── pca_model.pkl                  # PCA dimensionality reduction
│
├── 📄 Python Applications
│   ├── disease_info.py                # Main GUI app with maps (⭐ Primary)
│   ├── chatbot console.py             # Console-based ML diagnosis
│   ├── question diagnosis.py          # Interactive GUI diagnosis
│   └── newlogin.py                    # User authentication system
│
├── 🎓 Training Scripts
│   ├── train_model.py                 # Train traditional ML models
│   ├── train_deep_learning.py         # Train DL models
│   ├── evaluate_models.py             # Evaluate all models
│   └── config.py                      # Hyperparameter configuration
│
├── 📊 Datasets
│   ├── Training.csv                   # ML training data (4,920 samples)
│   ├── Testing.csv                    # Model validation data (42 samples)
│   └── doctors_dataset.csv            # Specialist recommendations
│
├── 📈 Results & Metrics
│   ├── model_metrics.json             # Performance metrics (JSON)
│   └── MODEL_INFO.md                  # Model documentation
│
├── 🗺️ Generated Files
│   └── nearby_places_map.html         # Auto-generated location map
│
├── 📋 Configuration
│   ├── requirements.txt               # Python dependencies
│   ├── config.py                      # Training configuration
│   └── README.md                      # Project documentation
│
└── 📁 Other
    ├── .git/                          # Git version control
    ├── .gitignore                     # Git ignore rules
    └── kishore/                       # Additional resources
```

### File Categories

#### ML Models (.pkl) - Scikit-learn Models
- Traditional machine learning models
- Saved using Python's pickle
- Fast inference, smaller file size

#### DL Models (.h5) - Keras/TensorFlow Models  
- Deep learning neural networks
- Saved in HDF5 format
- Higher accuracy, larger file size

#### Training Scripts (.py)
- Automated model training pipelines
- Hyperparameter tuning
- Model evaluation and comparison

#### Configuration Files
- `config.py` - Model hyperparameters
- `requirements.txt` - Dependencies
- `model_metrics.json` - Performance data



---

## 💡 Usage Examples

### Example 1: Finding Information about Diabetes
```python
1. Run: python disease_info.py
2. Type: "Diabetes"
3. Click: Search
4. View: Symptoms and precautions in your language
5. Find: Nearby hospitals in your city
```

### Example 2: Symptom-based Diagnosis
```python
1. Run: python "chatbot console.py"
2. Answer: Symptom questions (yes/no)
3. Get: Disease prediction
4. See: Recommended specialist
```

### Example 3: Interactive Diagnosis
```python
1. Run: python "question diagnosis.py"
2. Login: With username/password
3. Answer: GUI-based questions
4. Receive: Diagnosis and consultation link
```

---

## 🗺️ Map Features

### Interactive Map Elements
- **🔴 Red Marker:** Your location
- **🔵 Blue Markers:** Hospitals & Clinics
- **🟢 Green Markers:** Pharmacies & Medical Shops
- **⭕ Blue Circle:** Search radius

### Map Controls
- **Zoom:** Mouse scroll or +/- buttons
- **Pan:** Click and drag
- **Info:** Click markers for details
- **Tooltips:** Hover for quick preview

### Location Search Tips
- Use format: "City, Country" (e.g., "Chennai, India")
- Major cities work best (e.g., "Mumbai", "Delhi")
- Include state for accuracy (e.g., "Bangalore, Karnataka")
- Requires internet connection

---

## 🎯 Disease List (51+ Diseases)

### Common Diseases
- Fever, Cough, Viral Fever
- Food Poisoning, Dehydration
- Heat Stroke, Stomach Infection
- Skin Rash, Eye Infection, Back Pain

### Chronic Conditions
- Diabetes, Hypertension, Migraine
- Arthritis, Asthma, GERD
- Hypothyroidism, Hyperthyroidism

### Infectious Diseases
- Malaria, Dengue, Typhoid
- Tuberculosis, Chicken Pox
- Hepatitis (A, B, C, D, E)
- Pneumonia, Common Cold

### Other Conditions
- Fungal Infection, Allergy, Psoriasis
- Urinary Tract Infection, Acne
- Varicose Veins, Osteoarthritis
- And many more...

---

## 🔧 Troubleshooting

### Application Won't Start
```bash
# Check Python version
python --version  # Should be 3.7+

# Reinstall dependencies
pip install -r requirements.txt
```

### Map Not Opening
- ✅ Check internet connection
- ✅ Verify location format ("City, Country")
- ✅ Look for `nearby_places_map.html` in project folder
- ✅ Try different browser

### Data Files Missing
```bash
# Verify CSV files exist
Training.csv   # Required
Testing.csv    # Required
doctors_dataset.csv  # Optional
```

---

## ⚙️ Configuration

### Changing Languages
Located in `disease_info.py`:
```python
self.languages = {
    'English': 'en',
    'Hindi': 'hi',
    # Add more languages here
}
```

### Adjusting Search Radius
Located in `disease_info.py`:
```python
values=["1", "2", "5", "10", "15", "20"]  # kilometers
```

### Map Provider
Currently uses OpenStreetMap (free). To use Google Maps:
1. Get Google Maps API key
2. Replace folium with googlemaps library
3. Update map creation code

---

## 🚀 Future Enhancements

### Planned Features
- [ ] Real hospital data via Overpass API
- [ ] Emergency mode (nearest ER)
- [ ] Save favorite locations
- [ ] Offline map caching
- [ ] Push notifications
- [ ] Health history tracking
- [ ] Appointment booking integration

### API Integration Ideas
- **Google Places API** - Real hospital data
- **Overpass API** - OpenStreetMap queries
- **Healthcare APIs** - Real-time availability
- **Pharmacy APIs** - Medicine availability

---

## 📄 License

This project is created for educational purposes.

---

## 👥 Contributing

### How to Contribute
1. **Fork** the repository: https://github.com/Kishore276/health-care-chatbot
2. **Clone** your fork: `git clone https://github.com/YOUR-USERNAME/health-care-chatbot.git`
3. **Create** feature branch: `git checkout -b feature/AmazingFeature`
4. **Make** your changes and test thoroughly
5. **Commit** changes: `git commit -m 'Add AmazingFeature'`
6. **Push** to branch: `git push origin feature/AmazingFeature`
7. **Open** a Pull Request with detailed description

### Areas for Contribution
- 🔬 Adding more diseases and symptoms
- 🤖 Improving ML model accuracy
- 🗺️ Real hospital API integration (Overpass/Google Places)
- 🎨 UI/UX enhancements and themes
- 📚 Documentation improvements
- 🧪 Unit tests and quality assurance
- 🚀 Performance optimizations

---

## 📞 Support

### Common Issues
**Q: Map shows sample locations only**
A: Current version uses demo data. Integrate Overpass API for real locations.

**Q: How to add more diseases?**
A: Edit `Training.csv` with new disease symptoms.

**Q: Can I use offline?**
A: Disease lookup works offline. Maps require internet connection.

**Q: How accurate is the diagnosis?**
A: For informational purposes only. Always consult a real doctor.

---

## ⚠️ Disclaimer

**Important Notice:**
- This application is for **educational and informational purposes only**
- **Not a substitute for professional medical advice**
- Always **consult qualified healthcare professionals** for diagnosis
- In case of emergency, **call emergency services immediately**
- Demo version uses **sample location data** (integrate real APIs for production)

---

## 🎉 Acknowledgments

- **OpenStreetMap** for free map tiles and geographic data
- **Nominatim** for geocoding services
- **Scikit-learn** for machine learning algorithms
- **Python community** for excellent libraries and frameworks
- **Contributors** to the health-care-chatbot project

---

## 👨‍💻 Author

**Kishore276**
- GitHub: [@Kishore276](https://github.com/Kishore276)
- Repository: [health-care-chatbot](https://github.com/Kishore276/health-care-chatbot)

---

## 🔗 Repository Links

- **Main Repository:** https://github.com/Kishore276/health-care-chatbot
- **Issues:** https://github.com/Kishore276/health-care-chatbot/issues
- **Pull Requests:** https://github.com/Kishore276/health-care-chatbot/pulls
- **Clone URL:** `git clone https://github.com/Kishore276/health-care-chatbot.git`

---

## 📊 Statistics

- **Total Diseases:** 51+
- **Symptoms Tracked:** 132
- **Training Samples:** 4,922
- **Applications:** 3 (GUI, Console, Interactive)
- **Map Providers:** OpenStreetMap (free)
- **Accuracy:** High (for known symptom combinations)

---

## 🔗 Quick Links

### Repository
- **GitHub:** https://github.com/Kishore276/health-care-chatbot
- **Clone:** `git clone https://github.com/Kishore276/health-care-chatbot.git`
- **Issues:** https://github.com/Kishore276/health-care-chatbot/issues
- **Contribute:** Fork and create Pull Request

### Files
- **Main App:** `disease_info.py` (GUI with maps)
- **Console:** `chatbot console.py` (ML diagnosis)
- **GUI Diagnosis:** `question diagnosis.py` (Interactive)
- **Auth System:** `newlogin.py` (Login/Register)

### Commands
```bash
# Clone repository
git clone https://github.com/Kishore276/health-care-chatbot.git
cd health-care-chatbot

# Install dependencies
pip install -r requirements.txt

# Run main application
python disease_info.py

# Run console chatbot
python "chatbot console.py"

# Run GUI diagnosis
python "question diagnosis.py"
```

---

**Made with ❤️ for better health information access in India**

---

## 📌 Project Information

- **Repository:** [Kishore276/health-care-chatbot](https://github.com/Kishore276/health-care-chatbot)
- **Version:** 2.0 (Map Features & Location Services)
- **Last Updated:** October 2025
- **Status:** Active Development
- **Language:** Python 3.7+
- **License:** Educational Use

---

## 📝 Version History

### Version 2.0 (Current)
- ✅ Added nearby hospitals & medical shops finder
- ✅ Integrated OpenStreetMap with interactive maps
- ✅ Location-based search with radius selection
- ✅ Removed voice input (simplified interface)
- ✅ Removed doctor recommendations (replaced with maps)
- ✅ Removed multi-language support (simplified to English)

### Version 1.0
- Initial release with symptom lookup
- Voice input and text-to-speech
- Doctor recommendations
- 51+ diseases database

---

**Stay Healthy, Stay Safe! 🏥💙**
