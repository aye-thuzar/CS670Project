import streamlit as st
import torch
import torch.nn.functional as F
import transformers
from transformers import AutoTokenizer, AutoModelForSequenceClassification

st.title('Can I Patent This?')

# steamlit form
form = st.form(key='sentiment-form')
user_input = form.text_area(label = 'Enter your text', value = "I love steamlit and hugging face!")
submit = form.form_submit_button('Submit')

model_name = "distilbert-base-uncased-finetuned-sst-2-english"
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
      
