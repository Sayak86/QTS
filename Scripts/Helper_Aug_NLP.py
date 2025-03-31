# import libraries
import spacy
import string
import re,nltk
from nltk.corpus import stopwords
# Load spaCy English model
nlp = spacy.load("en_core_web_sm")
custom_stopwords = {"com","bank","regard","dear","regards","attach","team","hi","hello","thanks","thank","kindly"}
# Ensure necessary resources are downloaded
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

# stopwords
stopwords = set(stopwords.words('english'))
stopwords.update(custom_stopwords)


# Function to preprocess email body
def preprocess_text(text):
    text = re.sub(r'\W+', ' ', text)  # Remove punctuation & special characters
    doc = nlp(text.lower())  # Convert to lowercase and tokenize
    tokens = [
        token.lemma_ for token in doc  # Lemmatization
        if token.is_alpha and token.text not in stopwords  # Remove stopwords and non-alphabetic tokens
    ]
    return tokens

