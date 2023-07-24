import streamlit as st
from transformers import pipeline

st.title('Sentiment Analysis using Transformers pipeline function')

# steamlit form
form = st.form(key='sentiment-form')
user_input = form.text_area(label = 'Enter your text', value = "I love steamlit and hugging face!")
submit = form.form_submit_button('Submit')

if submit:
    classifier = pipeline("sentiment-analysis") #using the pipeline() function
    result = classifier(user_input)[0]
    label = result['label']
    score = result['score']

    if label == 'POSITIVE':
        st.success(f'{label} sentiment (score: {score})')
    else:
        st.error(f'{label} sentiment (score: {score})')
