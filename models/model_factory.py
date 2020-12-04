from data_loader import Data
from gensim.models.fasttext import FastText


class ESkipGram(object):
    def __init__(self, config=None, sg=True):
        if config is None:
            self.embed_size = 512
            self.window_size = 5
            self.min_freq = 3
            self.down_sampling = 1e-2
            self.sg = 1 if sg else 0

    def train(self):
        # d = Data()
        fast_text_embed = FastText(
            Data().get_tokens(),
            size=self.embed_size,
            window=self.window_size,
            min_count=self.min_freq,
            sample=self.down_sampling,
            workers=4,
            sg=self.sg,
            iter=100
        )
        return fast_text_embed


class ECbow(ESkipGram):
    def __init__(self, config=None):
        super().__init__(config, False)
