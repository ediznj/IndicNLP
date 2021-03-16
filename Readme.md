# NLP for Indian Language (initial draft)

An initiative to experiment various nlp tasks for tamil
language.

As a first step towards it, I started with text embeddings.

Here I used character based ngram embeddings to represent the vocab in syntatic space.
These embeddings will be useful in capturing NER, WordSense Disambuigation kind of tasks.

## Why Char-Based?
In general we know that char-based model is very effective in identifying the sub-words pattern 
and even un-trained word can be handled/scored by this pattern learning. By this learning process
our model tends to learn the syntatic structure of the language. Tamil grammatical structure also follows 
complex syntatic pattern and which is explained with an example below:

Vanthaan (வந்தான்)
which is equivalent to "He Came" in english

So this word **Vanthaan** has 3 attributes:
- Gender (he)
- Tense (past)
- Verb (Come)

similar word but variations in gender, plural form ...  
(vanthaar, vanthaal, vanthathu, vanthaargal)
 
 So it is clear that capturing char-based model for tamil 
 is more suitable than word-based. Also
 this is applicable for all indian languages
 
 ## tSNE Visualization of embeddings:
 
 ![NearestNeigbhorEmbeddingViz](https://github.com/njedison1984/TamilNLP/blob/master/images/NearestNeigbhorEmbeddingViz.PNG)
 
 In the above visualization, I searched a word called Team (ani) which returns the closest neighbors based on cosine similarity are
 Team's, Teams, T20, Jadeja, india and etc. Which shows our embedding learns these information from our training.

 ## Results supporting our claim to identify the named entities
 Here I searched for word analyst and it returns the closest embedding words
 which are mostly associated with some roles like Manager, Accountant, Researchers, Worker, Engineer ... 
 
 word similarity check: ஆய்வாளர (Analyst) which is Noun represents job role
 my test output returns all other roles
 
 Embed('SG').get_embed().wv.similar_by_word('ஆய்வாளர்', topn=10) 
 
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
 
 

