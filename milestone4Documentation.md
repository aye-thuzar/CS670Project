{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": []
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "source": [
        "# CS 670 Project - Finetuning Language Models"
      ],
      "metadata": {
        "id": "plgYaqGbr0LM"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "************************\n",
        "\n",
        "Deliverables\n",
        "\n",
        "************************\n",
        "\n",
        "Milestone-3 notebook: https://github.com/aye-thuzar/CS670Project/blob/main/CS670_milestone_3_AyeThuzar.ipynb\n",
        "\n",
        "Hugging Face App: https://huggingface.co/spaces/ayethuzar/can-i-patent-this\n",
        "\n",
        "Landing Page for the App: https://sites.google.com/view/cs670-finetuning-language-mode/home\n",
        "\n",
        "App Demonstration Video: [https://youtu.be/UEWUe-8fDOw](https://youtu.be/IXMJDoUqXK4)\n",
        "\n",
        "The tuned model shared to the Hugging Face Hub: https://huggingface.co/ayethuzar/tuned-for-patentability/tree/main\n",
        "\n",
        "************************\n"
      ],
      "metadata": {
        "id": "GIL5rFb4r5dc"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "Dataset: https://github.com/suzgunmirac/hupd"
      ],
      "metadata": {
        "id": "oAdWeGdcr8_T"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "**Data Preprocessing**\n",
        "\n",
        " I used the load_dataset function to load all the patent applications that were filed to the USPTO in January 2016. We specify the date ranges of the training and validation sets as January 1-21, 2016 and January 22-31, 2016, respectively. This is a smaller dataset.\n",
        "\n",
        " There are two datasets: train and validation. Here are the steps I did:\n",
        "\n",
        " - Label-to-index mapping for the decision status field\n",
        " - map the 'abstract' and 'claims' sections and tokenize them using pretrained('distilbert-base-uncased') tokenizer\n",
        " - format them\n",
        " - use DataLoader with batch_size = 16"
      ],
      "metadata": {
        "id": "DwKVDJSWr_Tc"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "**milestone 3:**\n",
        "\n",
        "The following notebook has the tuned model. There are 6 classes in the Harvard USPTO patent dataset and I decided to encode them as follow:\n",
        "\n",
        "decision_to_str = {'REJECTED': 0, 'ACCEPTED': 1, 'PENDING': 1, 'CONT-REJECTED': 0, 'CONT-ACCEPTED': 1, 'CONT-PENDING': 1}\n",
        "\n",
        "so that I can get a patentability score between 0 and 1.\n",
        "\n",
        "I use the pertained-model 'distilbert-base-uncased' from the Hugging face hub and tune it with the smaller dataset.\n",
        "\n",
        "My tuned model's performance is not good but I ran out of time. =(\n",
        "\n",
        "milestone3 notebook: https://github.com/aye-thuzar/CS670Project/blob/main/CS670_milestone_3_AyeThuzar.ipynb\n",
        "\n",
        "The tuned model shared to the Hugging Face Hub: https://huggingface.co/ayethuzar/tuned-for-patentability/tree/main\n",
        "\n",
        "I tested my shared model here: https://github.com/aye-thuzar/CS670Project/blob/main/CS670_Examples.ipynb"
      ],
      "metadata": {
        "id": "TCLsgp79sBnG"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "**milestone 4**\n",
        "\n",
        "This is the landing page for milestone 4 : https://sites.google.com/view/cs670-finetuning-language-mode/home\n",
        "\n",
        "The documentation for milestone 4: https://github.com/aye-thuzar/CS670Project/blob/main/milestone4Documentation.md\n",
        "\n",
        "I did not get a chance to fix my video, so it only has the model before I tuned it. After my tuned it, my model is only showing a patentabiilty score no matter which texts, I put for abstract and claims. =("
      ],
      "metadata": {
        "id": "O9Y9HKhZ5-09"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "**************\n",
        "\n",
        "References:\n",
        "\n",
        "1. https://colab.research.google.com/drive/1_ZsI7WFTsEO0iu_0g3BLTkIkOUqPzCET?usp=sharing#scrollTo=B5wxZNhXdUK6\n",
        "2. https://huggingface.co/AI-Growth-Lab/PatentSBERTa\n",
        "3. https://huggingface.co/anferico/bert-for-patents\n",
        "4. https://huggingface.co/transformers/v3.2.0/custom_datasets.html\n",
        "5. https://colab.research.google.com/drive/1TzDDCDt368cUErH86Zc_P2aw9bXaaZy1?usp=sharing\n",
        "6. https://huggingface.co/docs/transformers/model_sharing\n",
        "7. https://docs.streamlit.io/library/api-reference/widgets/st.file_uploader"
      ],
      "metadata": {
        "id": "VXhpu-LosEKk"
      }
    }
  ]
}