from .model_factory import ECbow, ESkipGram


class Embed(object):
    model_dict = {'SG': ESkipGram(), 'CBOW': ECbow()}

    def __init__(self, approach=None):
        '''Usage:   approach= 'SG'(Default) options['SG','CBOW']'''
        if approach:
            self.model = Embed.model_dict.get(approach, None)
        else:
            self.model = ESkipGram()

    def __call__(self):
        return self.model
