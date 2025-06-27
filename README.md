# 📝 Normalization Assignment

Welcome to your Normalization Assignment!

In this exercise, you will practice applying text pre-processing techniques critical for natural language processing (NLP) tasks such as chatbot development. You’ll work through:

✅ Noise removal using regex  
✅ Stopword removal using NLTK  
✅ Stemming to reduce words to their root form  
✅ Lemmatization for dictionary-level normalization  

## 🚀 Your Tasks

1️⃣ Open and clean the noisy text files (`story1.txt` and `story2.txt`).  
2️⃣ In `stemming.py`, follow the provided instructions to apply regex noise removal, tokenization, stopword removal, and stemming.  
3️⃣ In `lemmatization.py`, follow the provided instructions to apply regex noise removal, tokenization, stopword removal, and lemmatization with part-of-speech (POS) tagging.  

## 💡 Notes

- Install NLTK and download its resources:
  
  ```bash
  pip install nltk
  ```

- Then in Python:

  ```python
  import nltk
  nltk.download('punkt')
  nltk.download('stopwords')
  nltk.download('wordnet')
  nltk.download('averaged_perceptron_tagger')
  ```

- Focus on writing clean, modular code.

- Use print statements to inspect your outputs at each step!

🎯 Deliverables
✅ A cleaned, normalized list of words for both stemming and lemmatization.

Good luck, and have fun!
