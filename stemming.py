import nltk
import re
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')


"""
👨‍💻 Stemming Task

Your goal is to:
1️⃣ Read the content of either story1.txt or story2.txt.

2️⃣ Apply regex with re.sub() to remove:
    - HTML tags (e.g. <div>...</div>)
    - URLs
    - Hashtags (#), asterisks (*), excessive punctuation (e.g. !!!, ???)
    - Extra whitespace

3️⃣ Tokenize the cleaned text into words using nltk.word_tokenize.
4️⃣ Remove stopwords using nltk.corpus.stopwords.
5️⃣ Apply stemming using nltk.stem.PorterStemmer to reduce each word to its root form.
6️⃣ Print out the list of stemmed words.

📌 Hints:
- Remember to import the required NLTK modules.
- Think about what patterns to use in your regex for URLs and HTML tags.
- Inspect intermediate results to ensure your cleaning is working!

Write your code below this string.
"""
text_file = open("./story1.txt")
file_val = text_file.read()
text_file.close()

clean_story = re.sub(r'\s+', ' ', file_val).strip()  # Keep common sentence characters
cleaner_story = re.sub(r' *\.', ".", clean_story)
cleanest_story = re.sub(r'</?div>|[^\w\.\s/:]', '', cleaner_story)
cleanest_story = re.sub(r'\s+',' ', cleanest_story).strip()

sentences = sent_tokenize(cleanest_story)

words = word_tokenize(cleanest_story)

english_stopwords = set(stopwords.words('english'))

filtered_words = [word for word in words if word.lower() not in english_stopwords]

stemmer = PorterStemmer()

stemmed_story = [stemmer.stem(word) for word in filtered_words]

print(stemmed_story)

