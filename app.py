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

st.write("This model is tuned with all patent applications submitted in Jan 2016 in [the Harvard USPTO patent dataset.](https://github.com/suzgunmirac/hupd)")

st.write("You can upload a .csv file with a patent application to calculate the patentability score.")

# prepopulate with a sample csv file that has one patent application
dataframe = pd.read_csv('patent_application.csv') 

# to upload a .csv file with one application
uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    # To read file as bytes:
    bytes_data = uploaded_file.getvalue()
    #st.write(bytes_data)

    # To convert to a string based IO:
    stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
    #st.write(stringio)

    # To read file as string:
    string_data = stringio.read()
    #st.write(string_data)

    # Can be used wherever a "file-like" object is accepted:
    dataframe = pd.read_csv(uploaded_file)

# drop decision column if it exists
if 'decision' in dataframe.columns:
    dataframe.drop(['decision'], axis=1, inplace = True)
    
st.write(dataframe)

form = st.form(key='abstract-claims-form')
user_input_abstract = form.text_area(label = 'abstract', value = dataframe['abstract'][0])
user_input_claims = form.text_area(label = 'claims', value = dataframe['claims'][0])
submit = form.form_submit_button('Submit')

model_name = "ayethuzar/tuned-for-patentability"
model = AutoModelForSequenceClassification.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

text = [user_input_abstract + user_input_claims]

#testing = "text " + user_input_abstract
#testing_str = f"{text}"
#st.markdown(testing_str, unsafe_allow_html=True)

if submit:
    batch = tokenizer(text, padding = True, truncation = True, max_length = 512, return_tensors = "pt")
    
    with torch.no_grad():
      outputs = model(**batch)
      #st.write(outputs)
      predictions = F.softmax(outputs.logits, dim = 1)
      result = "Patentability Score: " + str(predictions.numpy()[0])
      html_str = f"""<style>p.a {{font: bold {28}px Courier;color:#1D5D9B;}}</style><p class="a">{result}</p>"""
      st.markdown(html_str, unsafe_allow_html=True)
      
tuple_of_choices = ('patent_number', 'title', 'background', 'summary', 'description')

# steamlit form
option = st.selectbox('Which other sections would you like to view?', tuple_of_choices)

st.write('You selected:', option)

user_input_other = st.text_area(label = 'other', value = dataframe[option][0])
