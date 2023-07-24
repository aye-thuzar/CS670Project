import streamlit as st
import torch
import torch.nn.functional as F
import transformers
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from datasets import load_dataset
import numpy as np
import pandas as pd
from io import StringIO


st.title('Can I Patent This?')

st.write("This model is tuned with all patent applications submitted in Jan 2016 in [the Harvard USPTO patent dataset](https://github.com/suzgunmirac/hupd)")

tuple_of_choices = ('patent_number', 'title', 'background', 'summary', 'description')

# steamlit form
option = st.selectbox('Which other sections would you like to view?', tuple_of_choices)

st.write('You selected:', option)

form = st.form(key='sentiment-form')
user_input = form.text_area(label = 'Enter your text', value = "I love steamlit and hugging face!")
submit = form.form_submit_button('Submit')

model_name = "ayethuzar/tuned-for-patentability"
model = AutoModelForSequenceClassification.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

test = [user_input]

if submit:
    batch = tokenizer(test, padding = True, truncation = True, max_length = 512, return_tensors = "pt")
    
    with torch.no_grad():
      outputs = model(**batch)
      #st.write(outputs)
      predictions = F.softmax(outputs.logits, dim = 1)
      result = "Patentability Score: " + str(predictions.numpy()[0][1])
      html_str = f"""<style>p.a {{font: bold {28}px Courier;color:#1D5D9B;}}</style><p class="a">{result}</p>"""
      st.markdown(html_str, unsafe_allow_html=True)
      
