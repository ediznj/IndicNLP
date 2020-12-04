import pandas as pd
import re

from gensim.models.fasttext import FastText

# import nltk

data_csv = 'data/tamil.csv'
tamil_df = pd.read_csv(data_csv)


def clean_text(text):
    text = re.sub(r'[\s]+', ' ', text, flags=re.I)
    text = re.sub(r'\s.{1}\s', ' ', text)
    text = re.sub(r'\s[0-9,.]+\s', ' ', text)
    text = re.sub(r'\’|\‘|\"|\“|\”|\?|\-|\.|\!|\'|[...]{1}', '', text)
    return text


# sample = tamil_df.iloc[:100,1]
# tokens = [(clean_text(text)).split() for text in sample]

all_txt = tamil_df.iloc[:, 1]
all_tokens = [(clean_text(text)).split() for text in all_txt]

embed_size = 512
window_size = 5
min_freq = 3
down_sampling = 1e-2

fast_text_embed = FastText(
    # tokens,
    all_tokens,
    size=embed_size,
    window=window_size,
    min_count=min_freq,
    sample=down_sampling,
    workers=4,  #
    sg=1,  # enabled skip-gram
    iter=100  # could be epoch ***
)


class TaEmbedding(object):
    def __init__(self):
        pass

    def vocab(self):
        pass

    def itos(self):
        pass

    def stoi(self):
        pass

    def similarity(self, word1, word2):
        pass

    def similar_words(self, word, topn):
        pass
