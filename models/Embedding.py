from .model_factory import ECbow, ESkipGram


class Embed(object):

    def __init__(self, approach='SG'):
        """Usage:   approach= 'SG'(Default) options['SG','CBOW']"""
        self.ft_embed = ECbow().train() if approach == 'CBOW' else ESkipGram().train()

    def get_embed(self):
        return self.ft_embed
