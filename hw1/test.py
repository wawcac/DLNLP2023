import os
import numpy as np
import jieba
import math
from collections import defaultdict



if __name__=='__main__':
    pass












# Preprocess the text data
def preprocess(text):
    # 读取小说
    str=''
    for filename in os.listdir('../text'):
        print(filename)
        with open(os.path.join('../text', filename), 'r', encoding='gb18030') as f:
            novel = f.read()
            str+=novel

    # 按字分
    with open('cn_punctuation.txt', 'r', encoding='utf8') as f:
        punctuation = set(f.read().splitlines())
    tokens = [c for c in str if c not in punctuation]
    
    
    # 按词分
    with open('cn_stopwords.txt', 'r', encoding='utf8') as f:
        stopwords = set(f.read().splitlines())
    tokens = [word for word in jieba.cut(str) if word not in stopwords]
    return tokens

# Create a document-term matrix
def create_document_term_matrix(docs):
    vocab = sorted(set(word for doc in docs for word in doc))
    vocab_index = {word: i for i, word in enumerate(vocab)}
    doc_term_matrix = np.zeros((len(docs), len(vocab)))
    for i, doc in enumerate(docs):
        for word in doc:
            doc_term_matrix[i, vocab_index[word]] += 1
    return doc_term_matrix, vocab_index

# Initialize the parameters
def initialize(doc_term_matrix, n_topics):
    n_docs, n_words = doc_term_matrix.shape
    topic_word_dist = np.random.rand(n_topics, n_words)
    topic_word_dist /= np.sum(topic_word_dist, axis=1)[:, np.newaxis]
    doc_topic_dist = np.random.rand(n_docs, n_topics)
    doc_topic_dist /= np.sum(doc_topic_dist, axis=1)[:, np.newaxis]
    return topic_word_dist, doc_topic_dist

# Perform Gibbs sampling
def gibbs_sampling(doc_term_matrix, topic_word_dist, doc_topic_dist, n_iter=100):
    n_docs, n_words = doc_term_matrix.shape
    n_topics = topic_word_dist.shape[0]
    for _ in range(n_iter):
        for i in range(n_docs):
            for j in range(n_words):
                if doc_term_matrix[i, j] > 0:
                    p_z = topic_word_dist[:, j] * doc_topic_dist[i, :]
                    p_z /= np.sum(p_z)
                    topic = np.random.multinomial(doc_term_matrix[i, j], p_z).argmax()
                    topic_word_dist[topic, j] += 1
                    doc_topic_dist[i, topic] += 1
        topic_word_dist /= np.sum(topic_word_dist, axis=1)[:, np.newaxis]
        doc_topic_dist /= np.sum(doc_topic_dist, axis=1)[:, np.newaxis]
    return topic_word_dist, doc_topic_dist

# Example usage
docs = ["I love dogs and cats", "I hate spiders and snakes"]
docs = [preprocess(doc) for doc in docs]
doc_term_matrix, vocab_index = create_document_term_matrix(docs)
n_topics = 2
topic_word_dist, doc_topic_dist = initialize(doc_term_matrix, n_topics)
topic_word_dist, doc_topic_dist = gibbs_sampling(doc_term_matrix, topic_word_dist, doc_topic_dist)