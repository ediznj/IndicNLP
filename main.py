from models.Embedding import Embed


def main():
    tamil_skipgram_embed = Embed('SG').get_embed()
    tamil_cbow_embed = Embed('CBOW').get_embed()
    print(tamil_skipgram_embed.wv.similar_by_word('ஆய்வாளர்', topn=10))
    print(tamil_cbow_embed.wv.similar_by_word('ஆய்வாளர்', topn=10))


if __name__ == '__main__':
    main()

