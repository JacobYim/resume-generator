import json
import nltk
from nltk.corpus import stopwords 
from collections import Counter

keywords_list = [
    'dl', 'ml', 'rl', 'reinforcement learning', 'deep learning', 'machine learning', 
    'recommender system', 'information retrieval', 'natural language processing', 
    'computer vision', 'nlp', 'cv', 'search-engine', 'search engine', 
    'full-stack', 'full stack', 'fullstack'
]

def keyword_extract(file) :
    with open(file) as f:
        data = json.load(f)
    d = data['describtion']
    paragraphs = list(filter(lambda x : x!= '', d.split('\n')))
    nltk.download('stopwords')
    
    # keyword
    keywords = []
    for paragraph in paragraphs :
        for keyword in keywords_list :
            if keyword in paragraph.lower() :
                keywords.append(keyword)
    
    # word_stats
    paragraph_words_list = list(map(lambda paragraph : paragraph.lower().split(), paragraphs))
    meaningful_words = []
    for paragraph_words in paragraph_words_list :
        for paragraph_word in paragraph_words :
            if not paragraph_word in stopwords.words('english') :
                meaningful_words.append(paragraph_word)

    a = Counter(meaningful_words)
    a = list(a.items())
    return keywords, sorted(a, key=lambda x : x[1], reverse=True), paragraphs
    

        