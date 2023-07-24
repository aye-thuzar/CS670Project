# CS 670 Project - Finetuning Language Models

************************

Deliverables

************************

Milestone-3 notebook: https://github.com/aye-thuzar/CS670Project/blob/main/CS670_milestone_3_AyeThuzar.ipynb

Hugging Face App: https://huggingface.co/spaces/ayethuzar/can-i-patent-this

Landing Page for the App: https://sites.google.com/view/cs670-finetuning-language-mode/home

App Demonstration Video: 

The tuned model shared to the Hugging Face Hub: https://huggingface.co/ayethuzar/tuned-for-patentability/tree/main

************************

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

The following notebook has the tuned model. There are 6 classes in the Harvard USPTO patent dataset and I decided to encode them as follow:

decision_to_str = {'REJECTED': 0, 'ACCEPTED': 1, 'PENDING': 1, 'CONT-REJECTED': 0, 'CONT-ACCEPTED': 1, 'CONT-PENDING': 1}

so that I can get a patentability score between 0 and 1.

I use the pertained-model 'distilbert-base-uncased' from the Hugging face hub and tune it with the smaller dataset.

The average accuracy of the validation set is about 89%.

milestone3 notebook: https://github.com/aye-thuzar/CS670Project/blob/main/CS670_milestone_3_AyeThuzar.ipynb

The tuned model shared to the Hugging Face Hub: https://huggingface.co/ayethuzar/tuned-for-patentability/tree/main

I tested my shared model here: https://github.com/aye-thuzar/CS670Project/blob/main/CS670_Examples.ipynb

**milestone4:**

Please see Milestone4Documentation.md: 

Here is the landing page for my app: https://sites.google.com/view/cs670-finetuning-language-mode/home


**************

References:

1. https://colab.research.google.com/drive/1_ZsI7WFTsEO0iu_0g3BLTkIkOUqPzCET?usp=sharing#scrollTo=B5wxZNhXdUK6

2. https://huggingface.co/AI-Growth-Lab/PatentSBERTa

3. https://huggingface.co/anferico/bert-for-patents

4. https://huggingface.co/transformers/v3.2.0/custom_datasets.html

5. https://colab.research.google.com/drive/1TzDDCDt368cUErH86Zc_P2aw9bXaaZy1?usp=sharing
