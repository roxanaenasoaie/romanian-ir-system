import stanza
from unidecode import unidecode
import re
from nltk.corpus import stopwords
import nltk

stanza.download('ro')
nltk.download('stopwords')


def remove_diacritics(text):
    return unidecode(text)


def tokenize_text(text):
    return re.sub(r"[^\w\s]", "", text)


stop_words = set(stopwords.words('romanian'))


def remove_stopwords(text):
    words = text.split()
    return ' '.join([word for word in words if word.lower() not in stop_words])


nlp = stanza.Pipeline('ro', processors='tokenize,lemma')


def lemmatize_text(text):
    doc = nlp(text)
    lemmas = [word.lemma for sentence in doc.sentences for word in sentence.words]
    return ' '.join(lemmas)


def preprocess_text(text):
    if not isinstance(text, str):
        raise ValueError("Input to preprocess_text must be a string")
    text = lemmatize_text(text)
    text = remove_diacritics(text)
    text = tokenize_text(text)
    text = remove_stopwords(text)
    return text

