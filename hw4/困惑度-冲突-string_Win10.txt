import math
import collections

def calculate_perplexity(text, n):
    # 将文本拆分成单词列表
    words = text.split()
    
    # 创建n-gram列表
    ngrams = []
    for i in range(len(words)-n+1):
        ngrams.append(tuple(words[i:i+n]))
    
    # 统计n-gram频率
    freqs = collections.Counter(ngrams)
    
    # 计算困惑度
    sum_log_prob = 0
    for ngram, count in freqs.items():
        context = ngram[:-1]
        context_freq = freqs[context] if context else len(words)
        prob = count / context_freq
        sum_log_prob += math.log(prob)
    entropy = -sum_log_prob / len(ngrams)
    perplexity = math.exp(entropy)
    
    return perplexity


text = "the quick brown fox jumps over the lazy dog"
perplexity = calculate_perplexity(text, 2)
print(perplexity)