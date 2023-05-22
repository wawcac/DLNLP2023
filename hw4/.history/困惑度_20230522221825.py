import math
import collections

def calculate_perplexity(text, n=2):
    # 创建n-gram列表
    ngrams = []
    for i in range(len(text)-n+1):
        ngrams.append(tuple(text[i:i+n]))
    print(ngrams)
    # 统计n-gram频率
    freqs = collections.Counter(ngrams)
    # print(freqs)
    # 计算困惑度
    sum_log_prob = 0
    for ngram, count in freqs.items():
        context = ngram
        context_freq = freqs[context] if context else len(text)
        # print(context,context_freq)
        prob = count / context_freq
        sum_log_prob += math.log(prob)
    entropy = -sum_log_prob / len(ngrams)
    perplexity = math.exp(entropy)
    
    return perplexity


text = "the quick brown fox jumps over the lazy dog"
perplexity = calculate_perplexity(text, 3)
print(perplexity)