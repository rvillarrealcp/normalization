import nltk
import re
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')

"""
👨‍💻 Lemmatization Task

Your goal is to:
1️⃣ Read the content of either story1.txt or story2.txt.
2️⃣ Apply regex with re.sub() to remove:
    - HTML tags (e.g. <div>...</div>)
    - URLs
    - Hashtags (#), asterisks (*), excessive punctuation (e.g. !!!, ???)
    - Extra whitespace

3️⃣ Tokenize the cleaned text into words using nltk.word_tokenize.
4️⃣ Remove stopwords using nltk.corpus.stopwords.
5️⃣ Tag each word with its part of speech using nltk.pos_tag.
6️⃣ Map POS tags to WordNet tags so the lemmatizer can use them.
7️⃣ Apply lemmatization using nltk.stem.WordNetLemmatizer, passing the correct POS.
8️⃣ Print out the list of lemmatized words.

📌 Hints:
- You’ll need a helper function to convert Treebank POS tags to WordNet POS tags.
- Check your intermediate outputs (POS tags, lemmatized results).

Write your code below this string.
"""
text_file = open("./story2.txt")
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

lemmatizer = WordNetLemmatizer()

lemmatized_words = [lemmatizer.lemmatize(word) for word in filtered_words]

print(lemmatized_words)