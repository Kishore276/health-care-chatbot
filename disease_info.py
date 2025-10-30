from tkinter import *
from tkinter import ttk, messagebox
import pandas as pd
import numpy as np
from googletrans import Translator
import threading
import os
import webbrowser
import folium
from geopy.geocoders import Nominatim
from geopy.distance import geodesic

class DiseaseInfoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Disease Information System - India")
        self.root.geometry("1200x900")  # Increased window size
        self.root.configure(bg='#ecf0f1')
        
        # Make window resizable
        self.root.resizable(True, True)
        
        # Set minimum window size
        self.root.minsize(1000, 700)
        
        # Initialize translator and geolocator
        try:
            self.translator = Translator()
            self.geolocator = Nominatim(user_agent="disease_info_app")
        except Exception as e:
            messagebox.showwarning("Initialization Warning", 
                f"Initialization warning: {str(e)}\nSome features may not work.")
            self.translator = None
        
        # Supported languages
        self.languages = {
            'English': 'en',
            'Hindi': 'hi',
            'Tamil': 'ta',
            'Telugu': 'te',
            'Bengali': 'bn',
            'Marathi': 'mr',
            'Gujarati': 'gu',
            'Kannada': 'kn',
            'Malayalam': 'ml',
            'Punjabi': 'pa'
        }
        self.output_language = 'en'  # Default output language
        
        # Load the dataset
        try:
            self.training_dataset = pd.read_csv('Training.csv')
            # Add common Indian diseases
            self.add_common_diseases()
            self.disease_data = self.prepare_disease_data()
            
            # Get unique disease names and create case-insensitive mapping
            self.diseases = sorted(self.training_dataset['prognosis'].unique())
            # Create lowercase mapping for case-insensitive search
            self.disease_map = {disease.lower(): disease for disease in self.diseases}
        except Exception as e:
            messagebox.showerror("Error", f"Error loading data: {str(e)}")
            return
        
        self.create_widgets()
    
    def add_common_diseases(self):
        """Add more common diseases found in India"""
        # Common Indian diseases to add
        common_diseases = {
            'Fever': {
                'body_ache': 1, 'chills': 1, 'fatigue': 1, 'headache': 1, 
                'sweating': 1, 'weakness_in_limbs': 1
            },
            'Cough': {
                'cough': 1, 'throat_irritation': 1, 'chest_pain': 1,
                'breathlessness': 1, 'phlegm': 1
            },
            'Viral Fever': {
                'high_fever': 1, 'body_ache': 1, 'fatigue': 1, 'headache': 1,
                'chills': 1, 'sweating': 1, 'weakness_in_limbs': 1
            },
            'Food Poisoning': {
                'vomiting': 1, 'diarrhoea': 1, 'abdominal_pain': 1,
                'nausea': 1, 'dehydration': 1, 'stomach_pain': 1
            },
            'Dehydration': {
                'dehydration': 1, 'sunken_eyes': 1, 'weakness_in_limbs': 1,
                'dizziness': 1, 'fatigue': 1
            },
            'Heat Stroke': {
                'high_fever': 1, 'dehydration': 1, 'headache': 1,
                'dizziness': 1, 'nausea': 1, 'sweating': 1
            },
            'Stomach Infection': {
                'stomach_pain': 1, 'vomiting': 1, 'diarrhoea': 1,
                'nausea': 1, 'abdominal_pain': 1
            },
            'Skin Rash': {
                'skin_rash': 1, 'itching': 1, 'redness_of_eyes': 1
            },
            'Eye Infection': {
                'redness_of_eyes': 1, 'watering_from_eyes': 1,
                'itching': 1, 'irritation_in_anus': 0
            },
            'Back Pain': {
                'back_pain': 1, 'muscle_pain': 1, 'stiff_neck': 1,
                'weakness_in_limbs': 1
            }
        }
        
        # Add these diseases to the dataset if they don't exist
        for disease_name, symptoms in common_diseases.items():
            if disease_name not in self.training_dataset['prognosis'].values:
                # Create a row with all symptoms as 0
                new_row = {col: 0 for col in self.training_dataset.columns}
                # Set the disease name
                new_row['prognosis'] = disease_name
                # Set the specific symptoms
                for symptom, value in symptoms.items():
                    if symptom in new_row:
                        new_row[symptom] = value
                # Append to dataset
                self.training_dataset = pd.concat([self.training_dataset, pd.DataFrame([new_row])], ignore_index=True)
    
    def prepare_disease_data(self):
        """Prepare disease data with symptoms"""
        disease_data = {}
        
        # Get all symptom columns (all except 'prognosis')
        symptom_cols = [col for col in self.training_dataset.columns if col != 'prognosis']
        
        # For each unique disease, find all associated symptoms
        for disease in self.training_dataset['prognosis'].unique():
            disease_rows = self.training_dataset[self.training_dataset['prognosis'] == disease]
            
            # Get symptoms that have value 1 for this disease
            symptoms = []
            for col in symptom_cols:
                if disease_rows[col].max() == 1:
                    # Convert column name to readable format
                    symptom_name = col.replace('_', ' ').title()
                    symptoms.append(symptom_name)
            
            disease_data[disease] = {
                'symptoms': symptoms,
                'precautions': self.get_precautions(disease)
            }
        
        return disease_data
    
    def get_precautions(self, disease):
        """Get precautions for a disease"""
        # Comprehensive precautions for all diseases
        precautions_map = {
            'Fungal infection': [
                'Keep affected area clean and dry',
                'Use antifungal medications as prescribed',
                'Wear loose, breathable clothing',
                'Avoid sharing personal items'
            ],
            'Allergy': [
                'Avoid known allergens',
                'Take prescribed antihistamines',
                'Keep environment clean',
                'Consult allergist for testing'
            ],
            'GERD': [
                'Avoid spicy and fatty foods',
                'Eat smaller meals',
                'Don\'t lie down immediately after eating',
                'Elevate head while sleeping'
            ],
            'Chronic cholestasis': [
                'Follow prescribed medication',
                'Avoid alcohol',
                'Maintain healthy diet',
                'Regular medical checkups'
            ],
            'Drug Reaction': [
                'Stop the suspected medication',
                'Consult doctor immediately',
                'Keep list of allergies',
                'Avoid self-medication'
            ],
            'Peptic ulcer diseae': [
                'Avoid NSAIDs and aspirin',
                'Reduce stress',
                'Avoid alcohol and smoking',
                'Eat regular, balanced meals'
            ],
            'AIDS': [
                'Take antiretroviral therapy regularly',
                'Practice safe sex',
                'Regular medical monitoring',
                'Maintain healthy lifestyle'
            ],
            'Diabetes': [
                'Monitor blood sugar regularly',
                'Follow prescribed diet',
                'Exercise regularly',
                'Take medications as prescribed'
            ],
            'Gastroenteritis': [
                'Stay hydrated',
                'Rest adequately',
                'Eat bland foods',
                'Maintain hand hygiene'
            ],
            'Bronchial Asthma': [
                'Avoid triggers and allergens',
                'Use inhaler as prescribed',
                'Monitor breathing regularly',
                'Keep rescue inhaler handy'
            ],
            'Hypertension': [
                'Reduce salt intake',
                'Exercise regularly',
                'Manage stress',
                'Take medications regularly'
            ],
            'Migraine': [
                'Identify and avoid triggers',
                'Get adequate sleep',
                'Stay hydrated',
                'Take prescribed medications'
            ],
            'Common Cold': [
                'Rest and stay hydrated',
                'Use steam inhalation',
                'Wash hands frequently',
                'Avoid close contact with others'
            ],
            'Pneumonia': [
                'Complete antibiotic course',
                'Rest adequately',
                'Stay hydrated',
                'Avoid smoking'
            ],
            'Dimorphic hemmorhoids(piles)': [
                'Increase fiber intake',
                'Drink plenty of water',
                'Avoid straining',
                'Use prescribed medications'
            ],
            'Heart attack': [
                'Take prescribed medications',
                'Follow cardiac rehabilitation',
                'Reduce stress',
                'Maintain healthy lifestyle'
            ],
            'Varicose veins': [
                'Exercise regularly',
                'Elevate legs when resting',
                'Wear compression stockings',
                'Avoid prolonged standing'
            ],
            'Hypothyroidism': [
                'Take thyroid medication daily',
                'Regular thyroid function tests',
                'Maintain healthy diet',
                'Monitor symptoms'
            ],
            'Hyperthyroidism': [
                'Take prescribed medications',
                'Regular monitoring',
                'Avoid excessive iodine',
                'Manage stress'
            ],
            'Hypoglycemia': [
                'Eat regular meals',
                'Monitor blood sugar',
                'Carry glucose tablets',
                'Avoid excessive alcohol'
            ],
            'Osteoarthristis': [
                'Maintain healthy weight',
                'Exercise regularly',
                'Use pain relief as needed',
                'Physical therapy'
            ],
            'Arthritis': [
                'Stay active',
                'Maintain healthy weight',
                'Take prescribed medications',
                'Use heat/cold therapy'
            ],
            '(vertigo) Paroymsal  Positional Vertigo': [
                'Avoid sudden head movements',
                'Practice balance exercises',
                'Stay hydrated',
                'Consult doctor for exercises'
            ],
            'Acne': [
                'Keep face clean',
                'Avoid touching face',
                'Use non-comedogenic products',
                'Consult dermatologist if severe'
            ],
            'Urinary tract infection': [
                'Drink plenty of water',
                'Complete antibiotic course',
                'Urinate frequently',
                'Maintain hygiene'
            ],
            'Psoriasis': [
                'Moisturize regularly',
                'Avoid triggers',
                'Use prescribed medications',
                'Manage stress'
            ],
            'Impetigo': [
                'Keep area clean',
                'Complete antibiotic course',
                'Avoid touching sores',
                'Wash hands frequently'
            ],
            'Tuberculosis': [
                'Complete full course of antibiotics',
                'Wear mask to prevent spread',
                'Ensure good ventilation',
                'Regular follow-up with doctor'
            ],
            'Hepatitis A': [
                'Practice good hand hygiene',
                'Avoid contaminated food and water',
                'Get vaccinated',
                'Rest and stay hydrated'
            ],
            'Hepatitis B': [
                'Get vaccinated',
                'Avoid sharing needles',
                'Practice safe sex',
                'Regular liver function monitoring'
            ],
            'Hepatitis C': [
                'Take antiviral medications as prescribed',
                'Avoid alcohol',
                'Regular medical monitoring',
                'Prevent transmission to others'
            ],
            'Hepatitis D': [
                'Get hepatitis B vaccination',
                'Avoid sharing needles',
                'Regular liver checkups',
                'Follow medical treatment'
            ],
            'Hepatitis E': [
                'Ensure safe drinking water',
                'Practice good hygiene',
                'Rest adequately',
                'Avoid raw or undercooked food'
            ],
            'Alcoholic hepatitis': [
                'Stop alcohol consumption immediately',
                'Follow nutritious diet',
                'Take prescribed medications',
                'Regular liver function tests'
            ],
            'Jaundice': [
                'Stay hydrated',
                'Eat light, easily digestible food',
                'Avoid alcohol',
                'Rest adequately'
            ],
            'Malaria': [
                'Complete antimalarial medication course',
                'Use mosquito nets',
                'Eliminate standing water',
                'Stay hydrated and rest'
            ],
            'Dengue': [
                'Rest and stay hydrated',
                'Monitor platelet count',
                'Use mosquito repellent',
                'Seek immediate care if symptoms worsen'
            ],
            'Typhoid': [
                'Complete antibiotic course',
                'Drink plenty of fluids',
                'Eat easily digestible food',
                'Practice good hygiene'
            ],
            'Chicken pox': [
                'Stay isolated to prevent spread',
                'Avoid scratching blisters',
                'Apply calamine lotion',
                'Get vaccinated for prevention'
            ],
            'Cervical spondylosis': [
                'Practice neck exercises',
                'Maintain good posture',
                'Use ergonomic pillow',
                'Apply heat or ice therapy'
            ],
            'Paralysis (brain hemorrhage)': [
                'Follow physical therapy regularly',
                'Take prescribed medications',
                'Control blood pressure',
                'Avoid smoking and excessive alcohol'
            ],
            'hepatitis A': [
                'Practice good hand hygiene',
                'Avoid contaminated food and water',
                'Get vaccinated',
                'Rest and stay hydrated'
            ],
            'Fever': [
                'Rest adequately',
                'Stay hydrated - drink plenty of water',
                'Take prescribed fever medication',
                'Use cold compress on forehead'
            ],
            'Cough': [
                'Stay hydrated',
                'Use cough syrup as prescribed',
                'Avoid cold drinks',
                'Use steam inhalation'
            ],
            'Viral Fever': [
                'Complete rest',
                'Drink plenty of fluids',
                'Take paracetamol for fever',
                'Eat light, nutritious food'
            ],
            'Food Poisoning': [
                'Stay hydrated with ORS',
                'Eat bland foods (BRAT diet)',
                'Avoid dairy and spicy foods',
                'Seek medical help if severe'
            ],
            'Dehydration': [
                'Drink ORS or coconut water',
                'Avoid caffeine and alcohol',
                'Eat water-rich foods',
                'Rest in cool environment'
            ],
            'Heat Stroke': [
                'Move to cool, shaded area',
                'Drink plenty of water',
                'Use cool water to lower body temperature',
                'Seek immediate medical attention'
            ],
            'Stomach Infection': [
                'Take prescribed antibiotics',
                'Stay hydrated',
                'Eat light, easy-to-digest food',
                'Maintain proper hygiene'
            ],
            'Skin Rash': [
                'Keep area clean and dry',
                'Avoid scratching',
                'Apply calamine lotion',
                'Consult dermatologist if persists'
            ],
            'Eye Infection': [
                'Avoid touching eyes',
                'Use prescribed eye drops',
                'Clean eyes with warm water',
                'Don\'t share towels or cosmetics'
            ],
            'Back Pain': [
                'Practice good posture',
                'Do gentle stretching exercises',
                'Apply heat or ice packs',
                'Avoid heavy lifting'
            ]
        }
        
        # Return specific precautions if available, otherwise general advice
        return precautions_map.get(disease, [
            'Consult a healthcare professional',
            'Follow prescribed treatment',
            'Maintain healthy lifestyle',
            'Regular medical checkups'
        ])
    
    def create_widgets(self):
        # Title
        title_frame = Frame(self.root, bg='#2c3e50', height=80)
        title_frame.pack(fill=X)
        title_frame.pack_propagate(False)
        
        title_label = Label(title_frame, text="⚕️ 🏥 Disease Information System", 
                          font=("Arial", 24, "bold"), bg='#2c3e50', fg='white')
        title_label.pack(pady=25)
        
        # Language Selection Frame
        lang_frame = Frame(self.root, bg='#34495e', pady=8)
        lang_frame.pack(fill=X)
        
        Label(lang_frame, text="🌐 Output Language:", font=("Arial", 10, "bold"), 
              bg='#34495e', fg='white').pack(side=LEFT, padx=(30, 10))
        
        self.lang_var = StringVar(value='English')
        lang_dropdown = ttk.Combobox(lang_frame, textvariable=self.lang_var, 
                                    values=list(self.languages.keys()), 
                                    width=15, font=("Arial", 9), state='readonly')
        lang_dropdown.pack(side=LEFT)
        lang_dropdown.bind('<<ComboboxSelected>>', self.on_language_change)
        
        # Search Frame
        search_frame = Frame(self.root, bg='#ecf0f1', pady=15)
        search_frame.pack(fill=X, padx=30)
        
        # Center the search controls
        search_container = Frame(search_frame, bg='#ecf0f1')
        search_container.pack()
        
        Label(search_container, text="Enter Disease Name:", font=("Arial", 12, "bold"), 
              bg='#ecf0f1', fg='#2c3e50').grid(row=0, column=0, padx=(0, 10), sticky=W)
        
        # Single Entry box for typing disease name (case-insensitive)
        self.disease_var = StringVar()
        self.disease_entry = Entry(search_container, textvariable=self.disease_var, 
                                   width=35, font=("Arial", 12), bd=2, relief=SOLID)
        self.disease_entry.grid(row=0, column=1, padx=5, ipady=6)
        self.disease_entry.bind('<Return>', lambda e: self.show_disease_info())
        self.disease_entry.focus()
        
        search_btn = Button(search_container, text="🔍 Search", command=self.show_disease_info,
                          bg='#27ae60', fg='white', font=("Arial", 11, "bold"),
                          padx=15, pady=6, cursor='hand2', relief=RAISED, bd=2)
        search_btn.grid(row=0, column=2, padx=5)
        
        clear_btn = Button(search_container, text="🗑️ Clear", command=self.clear_results,
                          bg='#e74c3c', fg='white', font=("Arial", 11, "bold"),
                          padx=15, pady=6, cursor='hand2', relief=RAISED, bd=2)
        clear_btn.grid(row=0, column=3, padx=5)
        
        voice_btn = Button(search_container, text="🎤 Voice", 
                          bg='#9b59b6', fg='white', font=("Arial", 11, "bold"),
                          padx=15, pady=6, cursor='hand2', relief=RAISED, bd=2)
        voice_btn.grid(row=0, column=4, padx=5)
        
        # Dropdown suggestion
        Label(search_container, text="Or select from list:", font=("Arial", 10), 
              bg='#ecf0f1', fg='#7f8c8d').grid(row=1, column=0, padx=(0, 10), pady=(10, 0), sticky=W)
        
        self.disease_combo = ttk.Combobox(search_container, textvariable=self.disease_var, 
                                         values=self.diseases, width=33, font=("Arial", 11), state='readonly')
        self.disease_combo.grid(row=1, column=1, columnspan=3, pady=(10, 0), sticky=W)
        
        # Status label
        self.status_label = Label(search_container, text="", font=("Arial", 9, "italic"), 
                                 bg='#ecf0f1', fg='#e74c3c')
        self.status_label.grid(row=2, column=0, columnspan=4, pady=(5, 0))
        
        # Info label
        info_frame = Frame(self.root, bg='#3498db', pady=6)
        info_frame.pack(fill=X, padx=30, pady=(10, 0))
        
        info_label = Label(info_frame, text="💡 Tip: Type disease name or select from dropdown | Press Enter to search | Find nearby hospitals & medical shops", 
                         font=("Arial", 9, "italic"), bg='#3498db', fg='white')
        info_label.pack()
        
        # Symptom Checker Frame
        symptom_checker_frame = Frame(self.root, bg='#ecf0f1', pady=10)
        symptom_checker_frame.pack(fill=X, padx=30)
        
        # Create container for symptom checker
        symptom_container = Frame(symptom_checker_frame, bg='#ffffff', bd=2, relief=GROOVE)
        symptom_container.pack(fill=X, padx=5, pady=5)
        
        # Header
        symptom_header = Frame(symptom_container, bg='#e67e22', pady=8)
        symptom_header.pack(fill=X)
        
        Label(symptom_header, text="🔍 Symptom-Based Disease Prediction", 
              font=("Arial", 13, "bold"), bg='#e67e22', fg='white').pack()
        
        # Input area
        symptom_input_frame = Frame(symptom_container, bg='#ffffff', pady=10)
        symptom_input_frame.pack(fill=X, padx=10)
        
        Label(symptom_input_frame, text="Enter your symptoms (comma-separated):", 
              font=("Arial", 10, "bold"), bg='#ffffff', fg='#2c3e50').pack(anchor=W, pady=(0, 5))
        
        # Symptom entry
        symptom_entry_frame = Frame(symptom_input_frame, bg='#ffffff')
        symptom_entry_frame.pack(fill=X)
        
        self.symptom_input_var = StringVar()
        self.symptom_entry = Entry(symptom_entry_frame, textvariable=self.symptom_input_var, 
                                   font=("Arial", 10), bd=2, relief=SOLID)
        self.symptom_entry.pack(side=LEFT, fill=X, expand=True, ipady=4)
        
        predict_btn = Button(symptom_entry_frame, text="🔬 Predict Disease", 
                           command=self.predict_disease_from_symptoms,
                           bg='#e67e22', fg='white', font=("Arial", 10, "bold"),
                           padx=15, pady=4, cursor='hand2', relief=RAISED, bd=2)
        predict_btn.pack(side=LEFT, padx=(10, 0))
        
        # Example text
        Label(symptom_input_frame, 
              text="Example: fever, headache, cough, body ache", 
              font=("Arial", 8, "italic"), bg='#ffffff', fg='#7f8c8d').pack(anchor=W, pady=(5, 0))
        
        # Results Frame
        results_frame = Frame(self.root, bg='#ecf0f1')
        results_frame.pack(fill=BOTH, expand=True, padx=30, pady=15)
        
        # Disease Name Label
        self.disease_name_label = Label(results_frame, text="", 
                                       font=("Arial", 16, "bold"), bg='#ecf0f1', fg='#c0392b')
        self.disease_name_label.pack(pady=(0, 10))
        
        # Create two columns for better layout
        content_frame = Frame(results_frame, bg='#ecf0f1')
        content_frame.pack(fill=BOTH, expand=True)
        
        # Left column - Symptoms
        left_frame = Frame(content_frame, bg='#ecf0f1')
        left_frame.pack(side=LEFT, fill=BOTH, expand=True, padx=(0, 5))
        
        # Symptoms Frame
        symptoms_label_frame = LabelFrame(left_frame, text="📋 Symptoms", 
                                        font=("Arial", 12, "bold"), bg='#ffffff',
                                        fg='#2c3e50', padx=12, pady=12, relief=GROOVE, bd=2)
        symptoms_label_frame.pack(fill=BOTH, expand=True)
        
        # Scrollbar for symptoms
        symptoms_scroll = Scrollbar(symptoms_label_frame)
        symptoms_scroll.pack(side=RIGHT, fill=Y)
        
        self.symptoms_text = Text(symptoms_label_frame, wrap=WORD, 
                                 yscrollcommand=symptoms_scroll.set,
                                 font=("Arial", 10), bg='#fffef7', height=15, bd=0,
                                 padx=10, pady=5)
        self.symptoms_text.pack(fill=BOTH, expand=True)
        symptoms_scroll.config(command=self.symptoms_text.yview)
        
        # Right column - Precautions
        right_frame = Frame(content_frame, bg='#ecf0f1')
        right_frame.pack(side=RIGHT, fill=BOTH, expand=True, padx=(5, 0))
        
        # Precautions Frame
        precautions_label_frame = LabelFrame(right_frame, text="💊 Precautions & Treatment", 
                                           font=("Arial", 12, "bold"), bg='#ffffff',
                                           fg='#2c3e50', padx=12, pady=12, relief=GROOVE, bd=2)
        precautions_label_frame.pack(fill=BOTH, expand=True)
        
        # Scrollbar for precautions
        precautions_scroll = Scrollbar(precautions_label_frame)
        precautions_scroll.pack(side=RIGHT, fill=Y)
        
        self.precautions_text = Text(precautions_label_frame, wrap=WORD,
                                    yscrollcommand=precautions_scroll.set,
                                    font=("Arial", 10), bg='#f0fff4', height=10, bd=0,
                                    padx=10, pady=5)
        self.precautions_text.pack(fill=BOTH, expand=True)
        precautions_scroll.config(command=self.precautions_text.yview)
        

        
        # Map Section Frame (Main Feature at Bottom)
        map_main_frame = Frame(self.root, bg='#ecf0f1', pady=10)
        map_main_frame.pack(fill=X, padx=30, side=BOTTOM, before=results_frame)
        
        # Create prominent map container
        map_container = Frame(map_main_frame, bg='#ffffff', bd=3, relief=GROOVE)
        map_container.pack(fill=X, padx=5, pady=5)
        
        # Map header with prominent styling
        map_header = Frame(map_container, bg='#2980b9', pady=12)
        map_header.pack(fill=X)
        
        Label(map_header, text="🗺️ 🏥 Find Nearby Hospitals & Medical Shops", 
              font=("Arial", 16, "bold"), bg='#2980b9', fg='white').pack()
        
        Label(map_header, text="🟢 Green = Hospitals & Clinics  |  🔵 Blue = Medical Stores & Pharmacies", 
              font=("Arial", 11), bg='#2980b9', fg='#ecf0f1').pack(pady=(5, 0))
        
        # Map input area
        map_input_frame = Frame(map_container, bg='#ffffff', pady=15)
        map_input_frame.pack(fill=X, padx=20)
        
        # Location input row
        location_row = Frame(map_input_frame, bg='#ffffff')
        location_row.pack(fill=X, pady=(0, 10))
        
        Label(location_row, text="📍 Enter Location:", font=("Arial", 12, "bold"), 
              bg='#ffffff', fg='#2c3e50').pack(side=LEFT, padx=(0, 10))
        
        self.map_location_var = StringVar()
        self.map_location_entry = Entry(location_row, textvariable=self.map_location_var, 
                                        width=30, font=("Arial", 11), bd=2, relief=SOLID)
        self.map_location_entry.pack(side=LEFT, padx=5, ipady=4)
        
        Label(location_row, text="(e.g., Mumbai, India or Chennai or Delhi)", 
              font=("Arial", 9, "italic"), bg='#ffffff', fg='#7f8c8d').pack(side=LEFT, padx=(10, 0))
        
        # Distance selection row
        distance_row = Frame(map_input_frame, bg='#ffffff')
        distance_row.pack(fill=X, pady=(0, 15))
        
        Label(distance_row, text="📏 Search Radius:", font=("Arial", 12, "bold"), 
              bg='#ffffff', fg='#2c3e50').pack(side=LEFT, padx=(0, 10))
        
        self.map_radius_var = StringVar(value="5")
        radius_dropdown = ttk.Combobox(distance_row, textvariable=self.map_radius_var, 
                                      values=["1", "2", "3", "5", "8", "10", "15", "20"], 
                                      width=10, font=("Arial", 11), state='readonly')
        radius_dropdown.pack(side=LEFT, padx=5)
        
        Label(distance_row, text="kilometers", font=("Arial", 11), 
              bg='#ffffff', fg='#2c3e50').pack(side=LEFT, padx=(5, 20))
        
        # Map action buttons
        map_btn = Button(distance_row, text="🗺️ Show Hospitals & Medical Shops", 
                        command=self.show_map_locations,
                        bg='#27ae60', fg='white', font=("Arial", 12, "bold"),
                        padx=20, pady=8, cursor='hand2', relief=RAISED, bd=3)
        map_btn.pack(side=LEFT, padx=10)
        
        open_existing_btn = Button(distance_row, text="📂 Open Last Map", 
                                  command=self.open_existing_map,
                                  bg='#3498db', fg='white', font=("Arial", 12, "bold"),
                                  padx=15, pady=8, cursor='hand2', relief=RAISED, bd=3)
        open_existing_btn.pack(side=LEFT, padx=5)
        
        # Map status label
        self.map_status_label = Label(map_container, text="", font=("Arial", 10, "italic"), 
                                     bg='#ffffff', fg='#e74c3c')
        self.map_status_label.pack(pady=(0, 10))
        
        # Footer
        footer_frame = Frame(self.root, bg='#34495e', height=30)
        footer_frame.pack(fill=X, side=BOTTOM)
        footer_frame.pack_propagate(False)
        
        footer_label = Label(footer_frame, text="⚕️ Stay Healthy, Stay Safe | Total Diseases Available: " + str(len(self.diseases)), 
                           font=("Arial", 9), bg='#34495e', fg='white')
        footer_label.pack(pady=6)
    
    def show_disease_info(self):
        disease_input = self.disease_var.get().strip()
        
        if not disease_input:
            messagebox.showwarning("Warning", "Please enter or select a disease!")
            return
        
        # Case-insensitive search
        disease_lower = disease_input.lower()
        
        # Find the actual disease name (case-insensitive)
        disease = None
        if disease_lower in self.disease_map:
            disease = self.disease_map[disease_lower]
        else:
            # Try partial matching
            matches = [d for d in self.diseases if disease_lower in d.lower()]
            if matches:
                disease = matches[0]
                # Ask user if this is what they meant
                if len(matches) > 1:
                    match_list = '\n'.join(matches[:5])
                    result = messagebox.askyesno("Multiple Matches Found", 
                                                f"Did you mean '{matches[0]}'?\n\nOther matches:\n{match_list}")
                    if not result:
                        return
            else:
                messagebox.showerror("Not Found", 
                                   f"Disease '{disease_input}' not found!\n\n" +
                                   "Please check spelling or select from dropdown.\n" +
                                   f"Total {len(self.diseases)} diseases available.")
                return
        
        if disease not in self.disease_data:
            messagebox.showerror("Error", "Disease data not available!")
            return
        
        # Store current disease
        self.current_disease = disease
        
        # Clear previous results
        self.clear_results()
        
        # Display disease name with success message
        disease_display = disease
        if self.output_language != 'en':
            try:
                translated = self.translator.translate(disease, src='en', dest=self.output_language)
                disease_display = f"{disease} ({translated.text})"
            except:
                pass
        
        self.disease_name_label.config(text=f"✅ {disease_display}")
        
        # Get data
        symptoms = self.disease_data[disease]['symptoms']
        precautions = self.disease_data[disease]['precautions']
        
        # Display symptoms with better formatting and translation
        self.symptoms_text.config(state=NORMAL)
        
        # Header
        header_text = f"Total Symptoms Found: {len(symptoms)}"
        if self.output_language != 'en':
            try:
                translated = self.translator.translate(header_text, src='en', dest=self.output_language)
                header_text = f"{header_text} ({translated.text})"
            except:
                pass
        
        self.symptoms_text.tag_config("header", font=("Arial", 12, "bold"), foreground="#16a085")
        self.symptoms_text.insert(END, header_text + "\n", "header")
        self.symptoms_text.insert(END, "─" * 60 + "\n\n")
        
        # Symptoms in columns with translation
        for i, symptom in enumerate(symptoms, 1):
            symptom_display = symptom
            if self.output_language != 'en':
                try:
                    translated = self.translator.translate(symptom, src='en', dest=self.output_language)
                    symptom_display = f"{symptom} ({translated.text})"
                except:
                    pass
            
            self.symptoms_text.tag_config("bullet", foreground="#2980b9", font=("Arial", 11, "bold"))
            self.symptoms_text.insert(END, "✓ ", "bullet")
            self.symptoms_text.insert(END, f"{symptom_display}\n")
        
        self.symptoms_text.config(state=DISABLED)
        
        # Display precautions with better formatting and translation
        self.precautions_text.config(state=NORMAL)
        
        # Header
        precaution_header = "Important Precautions:"
        if self.output_language != 'en':
            try:
                translated = self.translator.translate(precaution_header, src='en', dest=self.output_language)
                precaution_header = f"{precaution_header} ({translated.text})"
            except:
                pass
        
        self.precautions_text.tag_config("header", font=("Arial", 12, "bold"), foreground="#d35400")
        self.precautions_text.insert(END, precaution_header + "\n", "header")
        self.precautions_text.insert(END, "─" * 60 + "\n\n")
        
        for i, precaution in enumerate(precautions, 1):
            precaution_display = precaution
            if self.output_language != 'en':
                try:
                    translated = self.translator.translate(precaution, src='en', dest=self.output_language)
                    precaution_display = f"{precaution} ({translated.text})"
                except:
                    pass
            
            self.precautions_text.tag_config("number", foreground="#c0392b", font=("Arial", 11, "bold"))
            self.precautions_text.insert(END, f"{i}. ", "number")
            self.precautions_text.insert(END, f"{precaution_display}\n\n")
        
        self.precautions_text.config(state=DISABLED)
        
        # Store current disease
        self.current_disease = disease
    
    def clear_results(self):
        self.disease_name_label.config(text="")
        self.symptoms_text.config(state=NORMAL)
        self.symptoms_text.delete(1.0, END)
        self.symptoms_text.config(state=DISABLED)
        self.precautions_text.config(state=NORMAL)
        self.precautions_text.delete(1.0, END)
        self.precautions_text.config(state=DISABLED)
        self.current_disease = None
        self.status_label.config(text="")
    
    def predict_disease_from_symptoms(self):
        """Predict diseases based on entered symptoms"""
        symptom_input = self.symptom_input_var.get().strip()
        
        if not symptom_input:
            messagebox.showwarning("Warning", "Please enter at least one symptom!")
            self.symptom_entry.focus()
            return
        
        # Parse input symptoms
        input_symptoms = [s.strip().lower() for s in symptom_input.split(',')]
        
        # Get all symptom columns from dataset
        symptom_cols = [col for col in self.training_dataset.columns if col != 'prognosis']
        
        # Normalize symptom column names (replace _ with space)
        symptom_col_map = {col.replace('_', ' ').lower(): col for col in symptom_cols}
        
        # Match input symptoms to dataset columns
        matched_symptoms = []
        unmatched_symptoms = []
        
        for inp_symptom in input_symptoms:
            # Try exact match first
            if inp_symptom in symptom_col_map:
                matched_symptoms.append(symptom_col_map[inp_symptom])
            else:
                # Try partial matching
                partial_matches = [col for col_name, col in symptom_col_map.items() 
                                 if inp_symptom in col_name or col_name in inp_symptom]
                if partial_matches:
                    matched_symptoms.append(partial_matches[0])
                else:
                    unmatched_symptoms.append(inp_symptom)
        
        if not matched_symptoms:
            messagebox.showerror("No Match", 
                               f"Could not match any symptoms!\n\n" +
                               f"Unrecognized: {', '.join(unmatched_symptoms)}\n\n" +
                               "Please check spelling or try different symptoms.")
            return
        
        # Create symptom vector
        symptom_vector = pd.Series(0, index=symptom_cols)
        for symptom in matched_symptoms:
            symptom_vector[symptom] = 1
        
        num_input_symptoms = len(matched_symptoms)
        
        # Calculate match scores for each disease
        disease_scores = []
        
        for disease in self.training_dataset['prognosis'].unique():
            disease_rows = self.training_dataset[self.training_dataset['prognosis'] == disease]
            disease_symptoms = disease_rows[symptom_cols].max()  # Use max to get all symptoms for disease
            
            # Calculate matching score
            match_count = sum((symptom_vector == 1) & (disease_symptoms == 1))
            total_disease_symptoms = disease_symptoms.sum()
            
            if match_count > 0:
                # Improved scoring algorithm:
                # 1. Precision: How many input symptoms match the disease
                precision = (match_count / num_input_symptoms) * 100
                
                # 2. Coverage: How many disease symptoms are covered
                coverage = (match_count / total_disease_symptoms) * 100 if total_disease_symptoms > 0 else 0
                
                # 3. Combined score with weighted average
                # Precision is more important (60%) than coverage (40%)
                score = (precision * 0.6) + (coverage * 0.4)
                
                # Bonus for exact matches (all input symptoms match)
                if match_count == num_input_symptoms:
                    score += 10
                
                disease_scores.append({
                    'disease': disease,
                    'score': min(score, 100),  # Cap at 100
                    'matched': match_count,
                    'total': int(total_disease_symptoms),
                    'precision': precision,
                    'coverage': coverage
                })
        
        # Sort by score, then by matched count
        disease_scores.sort(key=lambda x: (x['score'], x['matched']), reverse=True)
        
        # Filter out very low scores (less than 10%)
        disease_scores = [d for d in disease_scores if d['score'] >= 10]
        
        # Get top 5 predictions
        top_predictions = disease_scores[:5]
        
        if not top_predictions:
            messagebox.showinfo("No Predictions", 
                              "Could not find matching diseases with sufficient confidence.\n" +
                              "Try adding more symptoms or check spelling.")
            return
        
        # Display results
        self.display_prediction_results(top_predictions, matched_symptoms, unmatched_symptoms)
    
    def display_prediction_results(self, predictions, matched_symptoms, unmatched_symptoms):
        """Display disease prediction results"""
        # Clear previous results
        self.clear_results()
        
        # Update disease name label
        self.disease_name_label.config(
            text=f"🔬 Disease Prediction Results (Top {len(predictions)} Matches)",
            fg='#e67e22'
        )
        
        # Display in symptoms panel
        self.symptoms_text.config(state=NORMAL)
        
        # Header
        self.symptoms_text.tag_config("header", font=("Arial", 12, "bold"), foreground="#e67e22")
        self.symptoms_text.insert(END, f"📊 Predicted Diseases (Based on Your Symptoms)\n", "header")
        self.symptoms_text.insert(END, "─" * 60 + "\n\n")
        
        # Matched symptoms info
        self.symptoms_text.tag_config("info", font=("Arial", 10, "bold"), foreground="#16a085")
        self.symptoms_text.insert(END, f"✓ Your Symptoms Matched ({len(matched_symptoms)}):\n", "info")
        
        self.symptoms_text.tag_config("symptom_list", font=("Arial", 9), foreground="#2c3e50")
        for i, symptom in enumerate(matched_symptoms, 1):
            symptom_name = symptom.replace('_', ' ').title()
            self.symptoms_text.insert(END, f"   {i}. {symptom_name}\n", "symptom_list")
        
        if unmatched_symptoms:
            self.symptoms_text.insert(END, "\n")
            self.symptoms_text.tag_config("warning", font=("Arial", 10, "bold"), foreground="#e74c3c")
            self.symptoms_text.insert(END, f"✗ Not Recognized:\n", "warning")
            self.symptoms_text.tag_config("unmatched", font=("Arial", 9), foreground="#95a5a6")
            for symptom in unmatched_symptoms:
                self.symptoms_text.insert(END, f"   • {symptom}\n", "unmatched")
        
        self.symptoms_text.insert(END, "\n" + "─" * 60 + "\n\n")
        
        # Display predictions
        self.symptoms_text.tag_config("prediction_header", font=("Arial", 11, "bold"), foreground="#2c3e50")
        self.symptoms_text.insert(END, "🎯 Possible Diseases:\n\n", "prediction_header")
        
        for i, pred in enumerate(predictions, 1):
            # Rank and disease name
            rank_symbol = "🥇" if i == 1 else "🥈" if i == 2 else "🥉" if i == 3 else f"{i}."
            
            # Color based on confidence
            if pred['score'] >= 70:
                color = "#27ae60"  # Green - High confidence
                confidence = "High"
            elif pred['score'] >= 40:
                color = "#f39c12"  # Orange - Medium confidence
                confidence = "Medium"
            else:
                color = "#e74c3c"  # Red - Low confidence
                confidence = "Low"
            
            self.symptoms_text.tag_config(f"disease{i}", 
                                         font=("Arial", 11, "bold"), 
                                         foreground=color)
            
            self.symptoms_text.insert(END, f"{rank_symbol} {pred['disease']}\n", f"disease{i}")
            
            # Score and match info with better formatting
            self.symptoms_text.tag_config(f"details{i}", font=("Arial", 9), foreground="#34495e")
            
            details = (f"   • Match Score: {pred['score']:.1f}% ({confidence} Confidence)\n"
                      f"   • Symptoms Matched: {pred['matched']} out of {pred['total']} disease symptoms\n"
                      f"   • Precision: {pred['precision']:.1f}% (your symptoms in disease)\n"
                      f"   • Coverage: {pred['coverage']:.1f}% (disease symptoms covered)\n")
            
            self.symptoms_text.insert(END, details, f"details{i}")
            self.symptoms_text.insert(END, "\n")
        
        self.symptoms_text.insert(END, "─" * 60 + "\n")
        self.symptoms_text.tag_config("note", font=("Arial", 8, "italic"), foreground="#7f8c8d")
        self.symptoms_text.insert(END, 
                                 "\n💡 Tip: Select a disease from the dropdown above to see complete details.\n"
                                 "⚠️  This is AI-based prediction for information only. Consult a doctor!\n"
                                 "🔍 For better accuracy, enter more specific symptoms.",
                                 "note")
        
        self.symptoms_text.config(state=DISABLED)
        
        # Display precautions for top prediction
        if predictions:
            top_disease = predictions[0]['disease']
            precautions = self.disease_data[top_disease]['precautions']
            symptoms_list = self.disease_data[top_disease]['symptoms']
            
            self.precautions_text.config(state=NORMAL)
            
            self.precautions_text.tag_config("header", font=("Arial", 12, "bold"), foreground="#e67e22")
            self.precautions_text.insert(END, 
                                        f"💊 Recommended Precautions\n", 
                                        "header")
            self.precautions_text.insert(END, 
                                        f"For: {top_disease}\n", 
                                        "header")
            self.precautions_text.insert(END, "─" * 60 + "\n\n")
            
            # All symptoms of this disease
            self.precautions_text.tag_config("symptom_header", font=("Arial", 10, "bold"), foreground="#3498db")
            self.precautions_text.insert(END, "📋 All Symptoms of This Disease:\n", "symptom_header")
            
            self.precautions_text.tag_config("symptom_text", font=("Arial", 9), foreground="#34495e")
            symptom_text = ", ".join(symptoms_list[:10])  # Show first 10
            if len(symptoms_list) > 10:
                symptom_text += f", and {len(symptoms_list) - 10} more..."
            self.precautions_text.insert(END, f"{symptom_text}\n\n", "symptom_text")
            
            # Precautions
            self.precautions_text.tag_config("precaution_header", font=("Arial", 10, "bold"), foreground="#e67e22")
            self.precautions_text.insert(END, "🏥 Precautions & Treatment:\n\n", "precaution_header")
            
            for i, precaution in enumerate(precautions, 1):
                self.precautions_text.tag_config("number", foreground="#c0392b", font=("Arial", 10, "bold"))
                self.precautions_text.insert(END, f"{i}. ", "number")
                self.precautions_text.tag_config("precaution", font=("Arial", 9), foreground="#2c3e50")
                self.precautions_text.insert(END, f"{precaution}\n\n", "precaution")
            
            self.precautions_text.insert(END, "─" * 60 + "\n\n")
            self.precautions_text.tag_config("warning_box", font=("Arial", 9, "bold"), foreground="#e74c3c")
            self.precautions_text.insert(END, 
                                        "⚠️  IMPORTANT DISCLAIMER:\n",
                                        "warning_box")
            self.precautions_text.tag_config("disclaimer", font=("Arial", 8), foreground="#95a5a6")
            self.precautions_text.insert(END,
                                        "This prediction is based on AI analysis and should NOT\n"
                                        "replace professional medical diagnosis. Please consult\n"
                                        "a qualified healthcare provider for accurate diagnosis\n"
                                        "and treatment.",
                                        "disclaimer")
            
            self.precautions_text.config(state=DISABLED)
    
    def on_language_change(self, event=None):
        """Handle language change"""
        selected_lang = self.lang_var.get()
        self.output_language = self.languages[selected_lang]
        # Re-display current results if any
        if hasattr(self, 'current_disease') and self.current_disease:
            self.show_disease_info()
    

    
    def show_map_locations(self):
        """Show hospitals and medical shops on map based on user input"""
        location_text = self.map_location_var.get().strip()
        
        if not location_text:
            messagebox.showwarning("Warning", "Please enter your location!")
            self.map_location_entry.focus()
            return
        
        try:
            radius_km = float(self.map_radius_var.get())
        except:
            radius_km = 5.0
        
        self.map_status_label.config(text="🔍 Finding your location and nearby medical facilities...", fg='#3498db')
        self.root.update()
        
        # Run in thread to avoid freezing UI
        thread = threading.Thread(target=self.create_location_map, args=(location_text, radius_km))
        thread.daemon = True
        thread.start()
    
    def open_existing_map(self):
        """Open the last created map file"""
        map_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'nearby_places_map.html')
        
        if os.path.exists(map_file):
            try:
                import platform
                # Use OS-specific command for reliable opening
                if platform.system() == 'Windows':
                    os.startfile(map_file)
                elif platform.system() == 'Darwin':  # macOS
                    os.system(f'open "{map_file}"')
                else:  # Linux
                    os.system(f'xdg-open "{map_file}"')
                
                self.map_status_label.config(text="✅ Map opened in browser!", fg='#27ae60')
                messagebox.showinfo("Map Opened", 
                                  f"The map has been opened in your web browser!\n\n"
                                  f"📂 File location:\n{map_file}\n\n"
                                  f"💡 Tip: You can also double-click 'nearby_places_map.html'\n"
                                  f"in the project folder to open it anytime.")
            except Exception as e:
                messagebox.showerror("Error", 
                                   f"Could not open map automatically.\n\n"
                                   f"Please manually open:\n{map_file}\n\n"
                                   f"You can double-click the file in File Explorer.\n\n"
                                   f"Error: {str(e)}")
        else:
            messagebox.showwarning("No Map Found", 
                                 "No map has been created yet!\n\n"
                                 "Please:\n"
                                 "1. Enter a location (e.g., 'Mumbai, India')\n"
                                 "2. Select radius (1-20 km)\n"
                                 "3. Click 'Show Hospitals & Medical Shops' button\n\n"
                                 "The map will be created and opened in your browser.")
            self.map_location_entry.focus()
    
    def create_location_map(self, location_text, radius_km):
        """Create OpenStreetMap with nearby hospitals and medical shops"""
        try:
            # Geocode the location
            location = self.geolocator.geocode(location_text, timeout=10)
            
            if not location:
                self.root.after(0, lambda: messagebox.showerror(
                    "Location Not Found", 
                    f"Could not find '{location_text}'.\nTry: 'City, Country' format (e.g., 'Chennai, India')"))
                self.root.after(0, lambda: self.map_status_label.config(text="❌ Location not found", fg='#e74c3c'))
                return
            
            lat, lon = location.latitude, location.longitude
            
            self.root.after(0, lambda: self.map_status_label.config(
                text=f"📍 Location found! Searching for hospitals & medical shops within {radius_km} km...", 
                fg='#27ae60'))
            
            # Create folium map
            map_obj = folium.Map(
                location=[lat, lon],
                zoom_start=13,
                tiles='OpenStreetMap'
            )
            
            # Add marker for user location
            folium.Marker(
                [lat, lon],
                popup=f"<b>Your Location</b><br>{location.address}",
                tooltip="You are here",
                icon=folium.Icon(color='red', icon='home', prefix='fa')
            ).add_to(map_obj)
            
            # Add circle to show search radius
            folium.Circle(
                radius=radius_km * 1000,  # Convert to meters
                location=[lat, lon],
                color='#3498db',
                fill=True,
                fillColor='#3498db',
                fillOpacity=0.1,
                popup=f'Search Radius: {radius_km} km'
            ).add_to(map_obj)
            
            # Note: OpenStreetMap Overpass API would be needed for real nearby search
            # For demonstration, we'll add some sample markers
            # In production, you would use Overpass API or Google Places API
            
            # Sample hospitals (these are examples - in production use real API)
            sample_hospitals = [
                {"name": "City General Hospital", "lat": lat + 0.01, "lon": lon + 0.01, "type": "hospital"},
                {"name": "Metro Medical Center", "lat": lat - 0.01, "lon": lon + 0.015, "type": "hospital"},
                {"name": "Emergency Clinic", "lat": lat + 0.015, "lon": lon - 0.01, "type": "clinic"},
                {"name": "Sunrise Hospital", "lat": lat + 0.008, "lon": lon + 0.018, "type": "hospital"},
                {"name": "Community Health Center", "lat": lat - 0.018, "lon": lon - 0.008, "type": "clinic"},
                {"name": "Specialized Surgery Center", "lat": lat + 0.020, "lon": lon - 0.015, "type": "hospital"},
            ]
            
            sample_pharmacies = [
                {"name": "MedPlus Pharmacy", "lat": lat + 0.008, "lon": lon - 0.008, "type": "pharmacy"},
                {"name": "Apollo Pharmacy", "lat": lat - 0.012, "lon": lon - 0.005, "type": "pharmacy"},
                {"name": "HealthCare Medical Store", "lat": lat - 0.005, "lon": lon + 0.012, "type": "pharmacy"},
                {"name": "Quick Meds", "lat": lat + 0.012, "lon": lon + 0.008, "type": "pharmacy"},
                {"name": "24/7 Medical Store", "lat": lat - 0.008, "lon": lon + 0.016, "type": "pharmacy"},
                {"name": "Generic Medicine Shop", "lat": lat + 0.016, "lon": lon - 0.012, "type": "pharmacy"},
                {"name": "Wellness Pharmacy", "lat": lat - 0.015, "lon": lon - 0.010, "type": "pharmacy"},
            ]
            
            # Add hospital markers (GREEN as requested)
            for hospital in sample_hospitals:
                distance = geodesic((lat, lon), (hospital['lat'], hospital['lon'])).km
                if distance <= radius_km:
                    folium.Marker(
                        [hospital['lat'], hospital['lon']],
                        popup=f"<b>🏥 {hospital['name']}</b><br>Type: {hospital['type'].title()}<br>Distance: {distance:.2f} km<br>Services: Emergency, Surgery, ICU",
                        tooltip=f"🏥 {hospital['name']}",
                        icon=folium.Icon(color='green', icon='plus-square', prefix='fa')
                    ).add_to(map_obj)
            
            # Add medical store/pharmacy markers (BLUE as requested)
            for pharmacy in sample_pharmacies:
                distance = geodesic((lat, lon), (pharmacy['lat'], pharmacy['lon'])).km
                if distance <= radius_km:
                    folium.Marker(
                        [pharmacy['lat'], pharmacy['lon']],
                        popup=f"<b>💊 {pharmacy['name']}</b><br>Type: Medical Store<br>Distance: {distance:.2f} km<br>Services: Medicines, First Aid",
                        tooltip=f"💊 {pharmacy['name']}",
                        icon=folium.Icon(color='blue', icon='medkit', prefix='fa')
                    ).add_to(map_obj)
            
            # Save map to HTML file
            map_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'nearby_places_map.html')
            map_obj.save(map_file)
            
            # Update status
            self.root.after(0, lambda: self.map_status_label.config(
                text=f"✅ Map created! Opening in browser...", 
                fg='#27ae60'))
            
            # Open map in browser with multiple fallback methods
            try:
                # Method 1: Try default browser
                import platform
                if platform.system() == 'Windows':
                    os.startfile(map_file)
                elif platform.system() == 'Darwin':  # macOS
                    os.system(f'open "{map_file}"')
                else:  # Linux
                    os.system(f'xdg-open "{map_file}"')
                
                self.root.after(100, lambda: self.map_status_label.config(
                    text=f"✅ Map opened! Check your web browser.", 
                    fg='#27ae60'))
            except Exception as e:
                # Method 2: Fallback to webbrowser module
                try:
                    webbrowser.open('file://' + map_file)
                    self.root.after(100, lambda: self.map_status_label.config(
                        text=f"✅ Map opened in browser!", 
                        fg='#27ae60'))
                except:
                    # If both fail, show file location
                    self.root.after(0, lambda: self.map_status_label.config(
                        text=f"⚠️ Map saved at: {map_file}", 
                        fg='#f39c12'))
            
            # Show success message
            self.root.after(500, lambda: messagebox.showinfo(
                "Map Created Successfully!", 
                f"🗺️ Interactive map has been created!\n\n"
                f"📍 Location: {location.address}\n"
                f"� Green markers = Hospitals/Clinics\n"
                f"� Blue markers = Medical Stores/Pharmacies\n"
                f"🔴 Red marker = Your Location\n"
                f"⭕ Blue circle = {radius_km} km search radius\n\n"
                f"📁 File saved at:\n{map_file}\n\n"
                f"💡 The map should open automatically in your browser.\n"
                f"If not, use the 'Open Last Map' button or\n"
                f"double-click the 'nearby_places_map.html' file.\n\n"
                f"Note: Currently showing sample locations.\n"
                f"For real data, integrate Overpass API or Google Places API."))
            
        except Exception as e:
            error_msg = str(e)
            self.root.after(0, lambda: messagebox.showerror(
                "Error", 
                f"Error creating map: {error_msg}\n\nMake sure you have internet connection."))
            self.root.after(0, lambda: self.map_status_label.config(
                text="❌ Error creating map", fg='#e74c3c'))

if __name__ == "__main__":
    root = Tk()
    app = DiseaseInfoApp(root)
    root.mainloop()
