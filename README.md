# 🏥 Disease Information System - India

A comprehensive medical information application that helps users identify diseases based on symptoms, provides treatment recommendations, and locates nearby hospitals and medical shops using interactive maps.

---

## 📋 Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Applications](#applications)
- [Technologies](#technologies)
- [Project Structure](#project-structure)
- [Contributing](#contributing)

---

## ✨ Features

### 🔍 Disease Information
- **51+ Diseases** with comprehensive symptom lists
- **Case-insensitive search** for easy lookup
- **Multi-language support** (10 Indian languages)
- **Precautions & Treatment** recommendations
- **Symptom-based diagnosis** using Machine Learning

### 🗺️ Location Services
- **Find Nearby Hospitals & Clinics** within customizable radius
- **Locate Medical Shops & Pharmacies** in your area
- **Interactive OpenStreetMap** integration
- **Distance calculation** from your location
- **Color-coded markers** for easy identification

### 🌐 Multi-Language Support
- English
- Hindi (हिंदी)
- Tamil (தமிழ்)
- Telugu (తెలుగు)
- Bengali (বাংলা)
- Marathi (मराठी)
- Gujarati (ગુજરાતી)
- Kannada (ಕನ್ನಡ)
- Malayalam (മലയാളം)
- Punjabi (ਪੰਜਾਬੀ)

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

### Step 1: Clone or Download
```bash
cd C:\Codes\CSP 1stProject(Failed)
```

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

### Additional Libraries
| Library | Purpose | Version |
|---------|---------|---------|
| googletrans | Translation Services | 4.0.0rc1 |
| folium | Interactive Maps | 0.20.0 |
| geopy | Geocoding & Distance | 2.4.1 |

### Data Sources
- **Disease Database:** 51+ diseases with symptoms
- **Symptom Dataset:** 132 unique symptoms
- **Training Data:** 4922 records
- **Maps:** OpenStreetMap (Nominatim)

---

## 📂 Project Structure

```
CSP 1stProject(Failed)/
│
├── 📄 disease_info.py          # Main application (GUI)
├── 📄 chatbot console.py       # Console-based diagnosis
├── 📄 question diagnosis.py    # GUI diagnosis with login
├── 📄 newlogin.py             # Authentication system
│
├── 📊 Training.csv            # Training dataset (4922 rows)
├── 📊 Testing.csv             # Test dataset
├── 📊 doctors_dataset.csv     # Doctor recommendations
│
├── 🗺️ nearby_places_map.html  # Generated map (auto-created)
│
├── 📋 requirements.txt         # Python dependencies
└── 📖 README.md               # This file
```

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

### Translation Not Working
- ✅ Check internet connection
- ✅ Verify `googletrans==4.0.0rc1` is installed
- ✅ Try selecting different language

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
1. Fork the repository
2. Create feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open Pull Request

### Areas for Contribution
- Adding more diseases
- Improving ML accuracy
- Real API integration
- UI/UX enhancements
- Documentation improvements

---

## 📞 Support

### Common Issues
**Q: Map shows sample locations only**
A: Current version uses demo data. Integrate Overpass API for real locations.

**Q: How to add more diseases?**
A: Edit `Training.csv` with new disease symptoms.

**Q: Can I use offline?**
A: Disease lookup works offline. Maps and translation require internet.

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

- **OpenStreetMap** for free map tiles
- **Nominatim** for geocoding services
- **Scikit-learn** for ML algorithms
- **Python community** for excellent libraries

---

## 📊 Statistics

- **Total Diseases:** 51+
- **Symptoms Tracked:** 132
- **Training Samples:** 4,922
- **Languages Supported:** 10
- **Map Providers:** OpenStreetMap (free)
- **Accuracy:** High (for known symptom combinations)

---

## 🔗 Quick Links

### Files
- **Main App:** `disease_info.py`
- **Console:** `chatbot console.py`
- **GUI Diagnosis:** `question diagnosis.py`

### Commands
```bash
# Run main application
python disease_info.py

# Run console chatbot
python "chatbot console.py"

# Run GUI diagnosis
python "question diagnosis.py"

# Install dependencies
pip install -r requirements.txt
```

---

**Made with ❤️ for better health information access in India**

**Version:** 2.0 (Updated with Map Features)
**Last Updated:** October 2025

---

## 📝 Version History

### Version 2.0 (Current)
- ✅ Added nearby hospitals & medical shops finder
- ✅ Integrated OpenStreetMap with interactive maps
- ✅ Location-based search with radius selection
- ✅ Removed voice input (simplified interface)
- ✅ Removed doctor recommendations (replaced with maps)

### Version 1.0
- Initial release with symptom lookup
- Multi-language support
- Voice input and text-to-speech
- Doctor recommendations
- 51+ diseases database

---

**Stay Healthy, Stay Safe! 🏥💙**
