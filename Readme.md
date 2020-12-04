# NLP for tamil (initial draft)

An initiative to experiment various nlp tasks for tamil
language.

As a first step towards it, I started with text embeddings.

Here I used character based ngram embeddings because of the language structure.

## Why Char-Based?
Vanthaan (வந்தான்)
which is equivalent to "He Came" in english

So this word **Vanthaan** has 3 attributes:
- Gender (he)
- Tense (past)
- Verb (Come)

similar word but variations in gender, plural form ...  
(vanthaar, vanthaal, vanthathu, vanthaargal)
 
 So it is clear that capturing word based model for tamil 
 is not suitable and hence I opted for char-based. Also
 this is applicable for all indian languages
 
 ## tSNE Visualization of embeddings:
 ![NearestNeigbhorEmbeddingViz](https://github.com/njedison1984/TamilNLP/blob/master/images/NearestNeigbhorEmbeddingViz.PNG)
 
 ## Word Similarity results:
 You can find the word similarity found by using this approach.
 
 word similarity check: ஆய்வாளர (Analyst) which is Noun represents job role
 my test output returns all other roles
 
 fast_text_embed.wv.similar_by_word('ஆய்வாளர்', topn=10) 
 
 [('ஆய்வாளர்', 0.9049257040023804),\
 ('தாளாளர்', 0.7836036682128906),\
 ('மேலாளர்', 0.764306902885437),\
 ('காசாளர்', 0.7459926605224609),\
 ('ஆய்வாளர்கள்', 0.7182431817054749),\
 ('பணியாளர்', 0.7180593609809875),\
 ('பொறியாளர்', 0.7125449776649475),\
 ('ஒளிப்பதிவாளர்', 0.7070046663284302),\
 ('உதவியாளர்', 0.706448495388031),\
 ('சாதனையாளர்', 0.6744421720504761)]\
 
 

