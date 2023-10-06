#import library

import streamlit as st
import joblib

#make choice box
AGE = {0: '0-9', 1: '10-19', 2: '20-24', 3: '25-59', 4: '60+'}
CHOICES = {0: "No", 1: "Yes"}
GENDER_CHOICE = {0: "Male", 1: "Female"}

st.title("Asthma Detector Model")
st.subheader('Please Insert The Informations')

def gender_func(option):
    return GENDER_CHOICE[option]

def format_func(option):
    return CHOICES[option]

def age_func(option):
    return AGE[option]


tiredness = st.selectbox(
    'Tiredness', 
    options=list(CHOICES.keys()), format_func=format_func)

dry_cough = st.selectbox(
    'Dry Cough', 
    options=list(CHOICES.keys()), format_func=format_func)

difficulty_in_breathing = st.selectbox(
    'Difficulty in Breathing', 
    options=list(CHOICES.keys()), format_func=format_func)

sore_throat = st.selectbox(
    'Sore Throat', 
    options=list(CHOICES.keys()), format_func=format_func)

none_sympton = st.selectbox(
    'None Sympton', 
    options=list(CHOICES.keys()), format_func=format_func)

pains = st.selectbox(
    'Pains', 
    options=list(CHOICES.keys()), format_func=format_func)

nasal_congestion = st.selectbox(
    'Nasal Congestion', 
    options=list(CHOICES.keys()), format_func=format_func)

runny_nose = st.selectbox(
    'Runny Nose', 
    options=list(CHOICES.keys()), format_func=format_func)

none_experiencing = st.selectbox(
    'None Experiencing', 
    options=list(CHOICES.keys()), format_func=format_func)

age_range = st.selectbox(
    'Age Range', 
    options=list(AGE.keys()), format_func=age_func)

gender = st.selectbox(
    'Gender', 
    options=list(GENDER_CHOICE.keys()), format_func=gender_func)

#load saved models
import pickle
with open('rf.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

# Create a Streamlit UI
predict_button = st.button('Predict')

if predict_button:
    criteria = [sore_throat, pains, age_range]
    prediction = model.predict([criteria])[0]
    if prediction == 0:
        label_text = 'You Have Asthma'
    else:
        label_text = 'Congratulations, You are Okay!!'

    # Display the prediction
    st.write(f'Severity: {label_text}')
