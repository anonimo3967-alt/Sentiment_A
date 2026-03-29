from textblob import TextBlob
import pandas as pd
import streamlit as st
from PIL import Image
from googletrans import Translator
from streamlit_lottie import st_lottie
import json

st.title('Análisis sentimental')
image = Image.open('Sentiment.jpg')
st.image(image)
st.subheader("Escribe en el campo el texto para que la programación haga sus cosas y te diga si la frase es feliz (positiva) o triste (negativa) o neutral")

translator = Translator()

with st.sidebar:
               st.subheader("Polaridad y Subjetividad")
               ("""
                Polaridad: es un número que va del -1 al 1 e indica si tu mensaje es terriblemente pesimista o se encuentra en la
                dictadura del positivismo (-1 para negativo, 1 para positivo y 0 para neutral)
                
               Subjetividad: mide que tan objetivo eres. 0 es realmente objetivo y 1 es muy, muy subjetivo

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
        y=round(blob.sentiment.subjectivity,2)
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

        if y >= 0.0 and y <= 0.5:
            st.write('Parece ser que eres bastante objetivo... Es una forma de ver la vida, pero recuerda que no hay tal cosa como la realidad')
            with open ('Thinking Emoji.json') as source:
              animation=json.load (source)
            st.lottie(animation,width =350)

        elif y >= 0.6 and y <= 1.0:
            st.write('Estas más en el lado de la subjetividad. No te preocupes, todos somos subjetivos en algún punto de nuestras vidas...')
            with open ('Dumb.json') as source:
              animation=json.load (source)
            st.lottie(animation,width =350)
