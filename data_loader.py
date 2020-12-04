import pandas as pd
import re


class Data(object):
    def __init__(self, from_csv=None, df=None, col=None):
        if not (from_csv and col) and not df:
            from_csv = 'data/tamil.csv'
            col = 1
            df = pd.read_csv(from_csv).iloc[:, col]
        elif from_csv and col:
            df = pd.read_csv(from_csv).iloc[:, col]
        self.text_col = df
        self.tokens = None

    def get_tokens(self):
        self.tokens = [Data.clean_text(text).split() for text in self.text_col]
        return self.tokens

    @staticmethod
    def clean_text(text):
        text = re.sub(r'[\s]+', ' ', text, flags=re.I)
        text = re.sub(r'\s.{1}\s', ' ', text)
        text = re.sub(r'\s[0-9,.]+\s', ' ', text)
        text = re.sub(r'\’|\‘|\"|\“|\”|\?|\-|\.|\!|\'|[...]{1}', '', text)
        return text
