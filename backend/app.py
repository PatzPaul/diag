from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import pandas as pd
from database import store_user_data, get_user_data

app = Flask(__name__)
CORS(app)

# Load the trained model
model_filename = 'recommendation_model.joblib'
model = joblib.load(model_filename)

# ... (your existing imports)


@app.route('/api/recommendations', methods=['POST'])
def get_recommendations():
    user_data = request.get_json()
    username = user_data.get('username', '')
    symptoms = user_data.get('symptoms', [])

    # Store user data in the database
    diagnosis = "SampleDiagnosis"  # Replace with the actual diagnosis
    store_user_data(username, diagnosis, symptoms)
    # Load your recommendations data
    recommendations = {
      'Headache': 'Take a pain reliever and get plenty of rest.',
    'Skin_issues': 'Consult a dermatologist for further evaluation.',
    'Cough': 'Stay hydrated and consider taking cough medicine.',
    'Fever': 'Take fever-reducing medication and rest.',
    'Sore_throat': 'Gargle with warm saltwater and rest your voice.',
    'Common_cold': 'Get plenty of rest and stay hydrated.',
    'Flu': 'Stay home, get plenty of rest, and drink fluids.',
    'Allergies': 'Avoid triggers and take antihistamines if needed.',
    'Asthma': 'Follow your asthma action plan and use inhaler as prescribed.',
    'Bronchitis': 'Rest, stay hydrated, and use cough medicine if needed.',
    'Pneumonia': 'Seek medical attention and follow prescribed treatment.',
    'Stomach_ache': 'Avoid heavy meals and try drinking ginger tea.',
    'Indigestion': 'Avoid trigger foods and consider antacids.',
    'Gastritis': 'Eat small, bland meals and avoid spicy foods.',
    'Gastroenteritis': 'Stay hydrated and eat easily digestible foods.',
    'Food_poisoning': 'Stay hydrated and rest, seek medical attention if severe.',
    'Diarrhea': 'Stay hydrated and eat bland foods like bananas and rice.',
    'Constipation': 'Eat fiber-rich foods and stay hydrated.',
    'Urinary_tract_infection': 'Drink plenty of water and see a doctor for antibiotics.',
    'Kidney_stones': 'Drink plenty of water and follow medical advice.',
    'Back_pain': 'Apply heat or ice, and consider over-the-counter pain relievers.',
    'Sprain': 'Rest, elevate the injured area, and use ice packs.',
    'Strain': 'Rest and apply ice packs to the affected area.',
    'Fracture': 'Seek immediate medical attention for proper evaluation.',
    'Migraine': 'Find a quiet, dark space and take prescribed medication if available.',
    'Depression': 'Reach out to a mental health professional for support.',
    'Anxiety': 'Practice relaxation techniques and consider therapy.',
    'Insomnia': 'Establish a sleep routine and create a calming bedtime environment.',
    'Obesity': 'Start a balanced diet and exercise regularly.',
    'Diabetes': 'Monitor blood sugar levels and follow dietary guidelines.',
    'Hypertension': 'Reduce salt intake and follow a heart-healthy diet.',
    'High_cholesterol': 'Eat a low-cholesterol diet and exercise regularly.',
    'Heartburn': 'Avoid trigger foods and consider antacids.',
    'Arthritis': 'Exercise regularly and consider pain-relief medication.',
    'Osteoporosis': 'Take calcium supplements and engage in weight-bearing exercises.',
    'Anemia': 'Eat iron-rich foods and consider iron supplements.',
    'Thyroid_disorder': 'Follow medical advice and take prescribed medication.',
    'Menstrual_cramps': 'Apply a heating pad and consider over-the-counter pain relievers.',
    'Menopause': 'Seek medical advice and consider hormone therapy if needed.',
    'Endometriosis': 'Consult a gynecologist for further evaluation and treatment.',
    'Pregnancy': 'Seek prenatal care and follow medical advice.',
    'Infertility': 'Consult a fertility specialist for evaluation and options.',
    'Sexually_transmitted_infection': 'Seek medical attention and practice safe sex.',
    'Common_cold': 'Get plenty of rest and stay hydrated.',
    'Flu': 'Stay home, get plenty of rest, and drink fluids.',
    'Allergies': 'Avoid triggers and take antihistamines if needed.',
    'Asthma': 'Follow your asthma action plan and use inhaler as prescribed.',
    'Bronchitis': 'Rest, stay hydrated, and use cough medicine if needed.',
    'Pneumonia': 'Seek medical attention and follow prescribed treatment.',
    'Stomach_ache': 'Avoid heavy meals and try drinking ginger tea.',
    'Indigestion': 'Avoid trigger foods and consider antacids.',
    'Gastritis': 'Eat small, bland meals and avoid spicy foods.',
    'Gastroenteritis': 'Stay hydrated and eat easily digestible foods.',
    'Food_poisoning': 'Stay hydrated and rest, seek medical attention if severe.',
    'Diarrhea': 'Stay hydrated and eat bland foods like bananas and rice.',
    'Constipation': 'Eat fiber-rich foods and stay hydrated.',
    'Urinary_tract_infection': 'Drink plenty of water and see a doctor for antibiotics.',
    'Kidney_stones': 'Drink plenty of water and follow medical advice.',
    'Back_pain': 'Apply heat or ice, and consider over-the-counter pain relievers.',
    'Sprain': 'Rest, elevate the injured area, and use ice packs.',
    'Strain': 'Rest and apply ice packs to the affected area.',
    'Fracture': 'Seek immediate medical attention for proper evaluation.',
    'Migraine': 'Find a quiet, dark space and take prescribed medication if available.',
    'Depression': 'Reach out to a mental health professional for support.',
    'Anxiety': 'Practice relaxation techniques and consider therapy.',
    'Insomnia': 'Establish a sleep routine and create a calming bedtime environment.',
    'Obesity': 'Start a balanced diet and exercise regularly.',
    'Diabetes': 'Monitor blood sugar levels and follow dietary guidelines.',
    'Hypertension': 'Reduce salt intake and follow a heart-healthy diet.',
    'High_cholesterol': 'Eat a low-cholesterol diet and exercise regularly.',
    'Heartburn': 'Avoid trigger foods and consider antacids.',
    'Arthritis': 'Exercise regularly and consider pain-relief medication.',
    'Osteoporosis': 'Take calcium supplements and engage in weight-bearing exercises.',
    'Anemia': 'Eat iron-rich foods and consider iron supplements.',
    'Thyroid_disorder': 'Follow medical advice and take prescribed medication.',
    'Menstrual_cramps': 'Apply a heating pad and consider over-the-counter pain relievers.',
    'Menopause': 'Seek medical advice and consider hormone therapy if needed.',
    'Endometriosis': 'Consult a gynecologist for further evaluation and treatment.',
    'Pregnancy': 'Seek prenatal care and follow medical advice.',
    'Infertility': 'Consult a fertility specialist for evaluation and options.',
    'Sexually_transmitted_infection': 'Seek medical attention and practice safe sex.',
    'Sinus_infection': 'Use nasal decongestants and consider warm compresses.',
    'Tonsillitis': 'Gargle with warm saltwater and get plenty of rest.',
    'Ear_infection': 'Use warm compresses and take pain relievers if needed.',
    'Conjunctivitis': 'Use warm compresses and avoid touching the eyes.',
    'Rash': 'Avoid irritants and consider topical creams for relief.',
    'Acne': 'Keep skin clean and consider over-the-counter acne treatments.',
    'Eczema': 'Keep skin moisturized and avoid triggers.',
    'Sunburn': 'Apply aloe vera gel and avoid sun exposure.',
    'Insect_bites': 'Apply ice packs and consider anti-itch creams.',
    'Athlete\'s_foot': 'Keep feet clean and dry, and use antifungal creams.',
    'Ringworm': 'Use antifungal creams and keep the area dry.',
    'Cold_sores': 'Use antiviral creams and avoid triggers.',
    'Chickenpox': 'Stay home and avoid scratching to prevent infection.',
    'Measles': 'Stay home and rest to prevent spread to others.',
    'Mumps': 'Stay home and rest, apply warm compresses for swelling.',
    'Rubella': 'Stay home and rest, avoid contact with pregnant women.',
    'Whooping_cough': 'Seek medical attention and stay isolated to prevent spread.',
    'Impetigo': 'Keep skin clean and use antibiotic creams as prescribed.',
    'Scabies': 'Seek medical attention for proper treatment and avoid close contact with others.',
    'Lice': 'Use over-the-counter lice treatments and wash bedding and clothing.',
    'Fungal_infections': 'Use antifungal creams and keep the area clean and dry.',
    'Parasitic_infections': 'Seek medical attention for proper diagnosis and treatment.',
    'Viral_infections': 'Get plenty of rest and stay hydrated.',
    'Bacterial_infections': 'Seek medical attention for proper diagnosis and antibiotics if needed.',
    'Respiratory_infections': 'Stay home, get plenty of rest, and drink fluids.',
    'Gastrointestinal_infections': 'Stay hydrated and eat easily digestible foods.',
    'Sexually_transmitted_infections': 'Seek medical attention and practice safe sex.',
    'Urinary_tract_infections': 'Drink plenty of water and see a doctor for antibiotics.',
    'Inflammatory_conditions': 'Follow medical advice and take prescribed medication.',
    'Autoimmune_conditions': 'Follow medical advice and take prescribed medication.',
    'Neurological_disorders': 'Seek medical attention for proper evaluation and treatment.',
    'Cardiovascular_disorders': 'Follow medical advice and adopt a heart-healthy lifestyle.',
    'Respiratory_disorders': 'Follow medical advice and take prescribed medication.',
    'Digestive_disorders': 'Follow medical advice and dietary guidelines.',
    'Musculoskeletal_disorders': 'Follow medical advice and consider physical therapy.',
    'Hormonal_imbalances': 'Seek medical advice for hormone testing and treatment options.',
    'Sleep_disorders': 'Establish a sleep routine and create a calming bedtime environment.',
    'Emotional_distress': 'Reach out to a mental health professional for support.',
    'Skin_conditions': 'Consult a dermatologist for further evaluation and treatment.',
    'Hair_loss': 'Consult a dermatologist for further evaluation and treatment.',
    'Nail_conditions': 'Consult a dermatologist for further evaluation and treatment.',
    'Eye_conditions': 'Consult an ophthalmologist for further evaluation and treatment.',
    'Ear_conditions': 'Consult an otolaryngologist for further evaluation and treatment.',
    'Oral_conditions': 'Consult a dentist for further evaluation and treatment.',
    'Bone_conditions': 'Consult an orthopedic specialist for further evaluation and treatment.',
    'Joint_conditions': 'Consult an orthopedic specialist for further evaluation and treatment.',
    'Muscle_conditions': 'Consult a physiotherapist for further evaluation and treatment.',
    'Nervous_system_conditions': 'Seek medical attention for proper evaluation and treatment.',
    'Reproductive_system_conditions': 'Consult a gynecologist for further evaluation and treatment.',
    'Endocrine_system_conditions': 'Follow medical advice and take prescribed medication.',
    'Circulatory_system_conditions': 'Follow medical advice and adopt a heart-healthy lifestyle.',
    'Respiratory_system_conditions': 'Follow medical advice and take prescribed medication.',
    'Digestive_system_conditions': 'Follow medical advice and dietary guidelines.',
    'Skeletal_system_conditions': 'Follow medical advice and consider physical therapy.',
    'Hormonal_system_conditions': 'Seek medical advice for hormone testing and treatment options.',
    'Sleep_system_conditions': 'Establish a sleep routine and create a calming bedtime environment.',
    'Emotional_system_conditions': 'Reach out to a mental health professional for support.'
    }


    # Generate recommendations based on symptoms
    matched_recommendations = []
    for symptom in symptoms:
        if symptom in recommendations:
            matched_recommendations.append(recommendations[symptom])
        else:
            matched_recommendations.append("No specific recommendation available for this symptom. Seek further advice.")

    return jsonify({'recommendations': matched_recommendations})

# ... (the rest of your code)


@app.route('/api/userdata', methods=['GET'])
def get_user_data_route():
    user_data = get_user_data()
    return jsonify({'user_data': user_data})

if __name__ == '__main__':
    app.run(debug=True)
