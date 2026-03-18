from textblob import TextBlob
import pandas as pd
import streamlit as st
from PIL import Image
from googletrans import Translator
from streamlit_lottie import st_lottie
import json

st.title('Análisis de Sentimiento')
image = Image.open('Sentiment.jpg')
st.image(image)
st.subheader("Escribe en el campo el texto para que la programación haga sus cosas y te diga si la frase es feliz (positiva) o triste (negativa) o neutral")

translator = Translator()

with st.sidebar:
               st.subheader("Polaridad y Subjetividad")
               ("""
                Polaridad: Indica si el sentimiento expresado en el texto es positivo, negativo o neutral. 
                Su valor oscila entre -1 (muy negativo) y 1 (muy positivo), con 0 representando un sentimiento neutral.
                
               Subjetividad: Mide cuánto del contenido es subjetivo (opiniones, emociones, creencias) frente a objetivo
               (hechos). Va de 0 a 1, donde 0 es completamente objetivo y 1 es completamente subjetivo.

                 """
               ) 

with st.expander('Analizar texto'):
    text = st.text_input('Escribe s´il vous plaît: ')
    if text:

        translation = translator.translate(text, src="es", dest="en")
        trans_text = translation.text
        blob = TextBlob(trans_text)
        st.write('Polaridad: ', round(blob.sentiment.polarity,2))
        st.write('Subjetividad: ', round(blob.sentiment.subjectivity,2))
        x=round(blob.sentiment.polarity,2)
        if x > 0.0 and x <=1.0:
            st.write( 'El robot de divinal inteligencia detecto que escribiste algo positivo 😊')
            with open ('Robot.json') as source:
              animation=json.load (source)
            st.lottie(animation,width =350)
        elif x >=-1 and x < 0:
            st.write( 'El robot de broncineas trenzas detecto que escribiste algo negativo 😔')
            with open ('bad emoji.json') as source:
              animation=json.load (source)
            st.lottie(animation,width =350)
        else:
            st.write( 'Parece ser que el robot carisimo del internet no detecta ninguna emoción, es decir, neutral 😐')
            with open ('Neutral face.json') as source:
              animation=json.load (source)
            st.lottie(animation,width =350)
