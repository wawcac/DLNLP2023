import os
import jieba
import math
from collections import defaultdict

def calc_entropy(token):
    freq = defaultdict(int)
    for c in token:
        freq[c] += 1
    total = len(token)
    entropy = 0
    for c in freq:
        prob = freq[c] / total
        entropy -= prob * math.log2(prob)
    return entropy



if __name__=='__main__':
    # 读取小说
    str=''
    for filename in os.listdir('text'):
        print(filename)
        with open(os.path.join('text', filename), 'r', encoding='gb18030') as f:
            novel = f.read()
            str+=novel

    # 按字分
    with open('cn_punctuation.txt', 'r', encoding='utf8') as f:
        punctuation = set(f.read().splitlines())
    tokens = [c for c in str if c not in punctuation]
    character_entropy=calc_entropy(tokens)
    print('字模型的熵',character_entropy)
    
    # 按词分
    with open('cn_stopwords.txt', 'r', encoding='utf8') as f:
        stopwords = set(f.read().splitlines())
    tokens = [word for word in jieba.cut(str) if word not in stopwords]
    word_entropy=calc_entropy(tokens)
    print('词模型的熵',word_entropy)