# MistralTest

## Overview
RAG is a repository for experimenting with language models and retrieval-based question answering systems using the LangChain framework. The project focuses on building a retrieval-based QA system capable of answering questions based on pre-processed text data.

## Features
- **Data Processing:** Utilizes the `dataprocessing` module to load and preprocess text data, making it suitable for training and inference.
- **Model Setup:** Implements the `modelsetup` module to configure the language model and its components, including embeddings, LLMS (Language Learning Models), and vector stores for efficient retrieval.
- **Question Answering:** Provides a user-friendly interface (commented code in the main.py for a console shell or deployement using gradio) for querying the QA system, allowing users to input questions and receive corresponding answers based on the trained model.

## Model
This project leverages the LangChain framework and integrates with Hugging Face's Sentence Transformers library to employ a powerful language model for sentence embeddings. The model chosen here:  Mistral 7B Instruct v0.1 - GGUF 
Link: https://huggingface.co/TheBloke/Mistral-7B-Instruct-v0.1-GGUF

## Usage
1. Install the required dependencies by running `pip install -r requirements.txt`.
2. Prepare your data (pdf files) and place it in the appropriate directory (e.g., `data/`).
3. Configure the model by specifying the model path downloaded and other parameters in `modelsetup.py`.
4. Run `main.py` to interact with the QA system. Enter your questions at the prompt and receive answers based on the trained model.

## Requirements
- Used Python 3.11.5 (may work with other versions)
- LangChain framework
- Additional dependencies listed in `requirements.txt`
- Download a LLM
