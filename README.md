# BANKING_SENTIMENTAL_ANALYSIS
This is a model  using BERT NEURAL NETWORK BERT NERUAL NETWORK and the Hugging Face Transformers library to classify the sentiment of reviews of top 5 banks in VN
** Data is scraped from GG map reviews, using Data Scraper extension


** NOTE: The reason we check for both string and list data types in the sentence variable is to handle different ways the text data could be structured in the DataFrame

Data Variability: This dataset is from Kaggle , and may have varying data structures. Sometimes the content column might contain a single string per review, and other times it could contain a list of strings representing multiple sentences from a single review(icons...). By checking for both string and list data types, the code can handle these variations and still perform sentiment analysis on the text data.

Model Compatibility: The Hugging Face Transformers pipeline (NLP) expects text input in the format of a single string or a list of strings. This is why we need to ensure that the input to the pipeline (sentence[0] in our case) is either a string or a list of strings.
