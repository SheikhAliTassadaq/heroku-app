# -*- coding: utf-8 -*-
"""
Created on Wed Jul 24 17:43:10 2024

@author: SHEIKH ALI TASSADAQ
"""


import pickle 
import streamlit as st
from streamlit_option_menu import option_menu


heart_disease_prediction = pickle.load(open("C:/Users/SHEIKH ALI TASSADAQ/Desktop/multiple disease prediction system/saved models/heart_disease_model.sav","rb")) 
parkinson_prediction = pickle.load(open("C:/Users/SHEIKH ALI TASSADAQ/Desktop/multiple disease prediction system/saved models/parkinson.sav","rb"))
diabeties_prediction = pickle.load(open("C:/Users/SHEIKH ALI TASSADAQ/Desktop/multiple disease prediction system/saved models/trained_model.sav","rb"))

with st.sidebar:
    selected = option_menu('MULTIPLE DISEASE PREDICTION SYSTEM', 
                      ['Heart Disease Prediction',
                       'Parkinson Disease Prediction',
                       'Diabeties Prediction '], 
                      default_index=0)

if selected == heart_disease_prediction:
    
    
   st.title("Heart Disease Prediction System using ML")
   
   col1 , col2 , col3 , = st.columns(3)
   
   with col1:
       age = st.text_input('Enter Your Age ')
   
   with col2:
       sex = st.text_input('GENDER')
       
   with col3:
       cp = st.text_input('Enter cp Value ')
       
   with col1:
       trestbps = st.text_input('Enter trestbps value ')
   
   with col2:
       chol = st.text_input('Enter Chol Value')
         
   with col3:
       fbs = st.text_input('Enter fbs Value ')
   
   with col1:
       restecg = st.text_input('Enter restecg Value')
      
   with col2:
       thalach = st.text_input('Enter thalach Value ')  
      
   with col3:
       restecg = st.text_input('Enter restecg Value')  
      
   with col1:
       exang = st.text_input('Enter exang Value ')
      
   with col2:
       oldpeak = st.text_input('Enter oldpeak Value ')
      
   with col3:
       slope = st.text_input(' Enter slope Value ')
          
   with col1:
       ca = st.text_input('Enter ca Value ')
   
   with col2:
       thal = st.text_input('Enter thal Value')

   heart_diag = ' '
   
   if st.button('Heart Disease Test Result'):
       hd_prediction = model.predict([[age,sex,cp , trestbps , chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])
       
       if hd_prediction[0] == 0:
           print("The person does not Have Heart Disease ")
       else:
           print('The Person Have Heart Disease ')
   st.success(heart_diag)
    
if (selected == parkinson_prediction):
    
    st.title("Parkinson Disease Prediction System using ML")
    

    col1 , col2 , col3 , = st.columns(3)
    
    with col1:
        MDVP:Fhi(Hz)= st.text_input('MDVP:Fhi(Hz) ')
    
    with col2:
        MDVP:Flo(Hz) = st.text_input('MDVP:Flo(Hz)')
        
    with col3:
        MDVP:Jitter(%) = st.text_input('MDVP:Jitter(%)')
        
    with col1:
        MDVP:Jitter(Abs) = st.text_input('MDVP:Jitter(Abs) ')
    
    with col2:
        MDVP:RAP = st.text_input('MDVP:RAP')
          
    with col3:
        MDVP:PPQ = st.text_input('MDVP:PPQ ')
    
    with col1:
        Jitter:DDP = st.text_input('Jitter:DDP')
       
    with col2:
        MDVP:Shimmer = st.text_input('MDVP:Shimmer')  
       
    with col3:
        MDVP:Shimmer(dB) = st.text_input('MDVP:Shimmer(dB)')  
       
    with col1:
        Shimmer:APQ3 = st.text_input('Shimmer:APQ3 ')
       
    with col2:
        Shimmer:APQ5 = st.text_input('Shimmer:APQ5 ')
       
    with col3:
        MDVP:APQ = st.text_input(' MDVP:APQ ')
           
    with col1:
        Shimmer:DDA = st.text_input('Shimmer:DDA ')
    
    with col2:
        NHR = st.text_input('NHR')
        
    with col2:
       HNR= st.text_input('HNR')    
    with col2:
        RPDE = st.text_input('RPDE')    
    with col2:
        DFA = st.text_input('DFA')
    with col2:
        spread1 = st.text_input('spread1')
    with col2:
        spread2 = st.text_input('spread2')
    with col2:
        D2 = st.text_input('D2')
    with col2:
        PPE = st.text_input('PPE')

    parkinson_daig = ' '
   
    if st.button('Parkinson Disease Test Result'):
        pd_prediction = model.predict([[MDVP:Fhi(Hz), MDVP:Flo(Hz),MDVP:Jitter(%) ,  MDVP:Jitter(Abs), MDVP:RAP, MDVP:PPQ, Jitter:DDP, MDVP:Shimmer, MDVP:Shimmer(dB), Shimmer:APQ3, Shimmer:APQ5, MDVP:APQ, Shimmer:DDA,NHR , HNR ,RPDE ,DFA ,spread1,spread2 , D2 ,PPE  ]])
       
        if pd_prediction[0] == 0:
            print("The person does not Have Parkinson Disease ")
        else:
            print('The Person Have Parkinson Disease ')
    st.success(parkinson_daig)   




if selected == diabeties_prediction:
    
    
    st.title("Diabeties Prediction System using ML")
    col1 , col2 , col3 , = st.columns(3)
   
       
    with col1:
        Pregnancies = st.text_input(' NO of Pregnancies ')
   
    with col2:
        Glucose = st.text_input('Enter Glucose Value')
         
    with col3:
        BloodPressure = st.text_input('Enter BloodPressure Value ')
   
    with col1:
        SkinThickness = st.text_input('Enter SkinThickness Value')
      
    with col2:
        Insulin = st.text_input('Enter Insulin Value ')  
      
    with col3: 
        BMI = st.text_input('Enter BMI Value')  
      
    with col1:
        DiabetesPedigreeFunction = st.text_input('Enter DiabetesPedigreeFunction Value ')
      
    with col2:
        Age = st.text_input('Enter Age ')
      
    diab_diag = ' '
    
    if st.button('Diabetic Diagnosis Test Result'):
        d_prediction = Classifiers.predict([[Pregnancies,Glucose ,BloodPressure , SkinThickness, Insulin, BMI , DiabetesPedigreeFunction, Age ]])
       
        if d_prediction[0] == 0: 
            print("The person is not diabetic patient ")
        else:
            print('The Person is diabetic patient ')
    st.success(diab_diag)