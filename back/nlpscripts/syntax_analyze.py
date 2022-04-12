import nltk
nltk.download('averaged_perceptron_tagger')
nltk.download("punkt")
import nltk.corpus
from nltk.tokenize import word_tokenize
from nltk.tokenize import RegexpTokenizer
from nltk.data import load


def to_json(tag:list) -> str:
    json = "["
    for tagged_token in tag:
        json += "{\"word\":\"" + tagged_token[0] + "\",\"type\":\"" + tagged_token[1] + "\"},"
    json = json[:-1] + "]"
    return json

def syntax_analyze(text:str) -> str:
    sent_tokens = word_tokenize(text)
    print(sent_tokens)
    return to_json(nltk.pos_tag(sent_tokens))
