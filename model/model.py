from .model_factory import ECbow, ESkipGram

model_dict = {'SG': ESkipGram(), 'CBOW': ECbow()}


class Model(object):
    def __init__(self, approach=None):
        if approach:
            self.model = model_dict.get(approach, None)
        else:
            self.model = ESkipGram()

    def __call__(self):
        return self.model
