
# CS 670 Project - Finetuning Language Models

************************

Milestone-3 notebook: https://github.com/aye-thuzar/CS670Project/blob/main/CS670_milestone_3_AyeThuzar.ipynb

Hugging Face App: 

Landing Page for the App: https://sites.google.com/view/cs670-finetuning-language-mode/home

App Demonstration Video: 


************************

## Summary

***********

**milestone1:** https://github.com/aye-thuzar/CS670Project/blob/main/README_milestone_1.md

**milestone2:** https://github.com/aye-thuzar/CS670Project/blob/main/README_milestone-2.md

Dataset: https://github.com/suzgunmirac/hupd

**Data Preprocessing**

 I used the load_dataset function to load all the patent applications that were filed to the USPTO in January 2016. We specify the date ranges of the training and validation sets as January 1-21, 2016 and January 22-31, 2016, respectively. This is a smaller dataset.

 There are two datasets: train and validation. Here are the steps I did:

 - Label-to-index mapping for the decision status field
 - map the 'abstract' and 'claims' sections and tokenize them using pretrained('distilbert-base-uncased') tokenizer
 - format them
 - use DataLoader with batch_size = 16

**milestone3:**

The following notebook has the tuned model.

milestone3 notebook: https://github.com/aye-thuzar/CS670Project/blob/main/CS670_milestone_3_AyeThuzar.ipynb

**milestone4:**

Please see Milestone4Documentation.md: 

Here is the landing page for my app: 


**************

References:

1. https://colab.research.google.com/drive/1_ZsI7WFTsEO0iu_0g3BLTkIkOUqPzCET?usp=sharing#scrollTo=B5wxZNhXdUK6

2. https://huggingface.co/AI-Growth-Lab/PatentSBERTa

3. https://huggingface.co/anferico/bert-for-patents

4. https://huggingface.co/transformers/v3.2.0/custom_datasets.html

