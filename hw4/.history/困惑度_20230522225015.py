import math

def calculate_perplexity(corpus, test_sentence, n, alpha=0.1):
    # 构建n-gram模型
    ngrams = []
    for i in range(len(corpus) - n + 1):
        ngrams.append(tuple(corpus[i:i+n]))

    # 统计n-gram出现的次数
    ngram_counts = {}
    for gram in ngrams:
        if gram in ngram_counts:
            ngram_counts[gram] += 1
        else:
            ngram_counts[gram] = 1

    # 计算概率和困惑度（使用加性平滑）
    sentence_probability = 1.0
    total_ngrams = len(ngrams)
    for i in range(len(test_sentence) - n + 1):
        ngram = tuple(test_sentence[i:i+n])
        ngram_probability = (ngram_counts.get(ngram, 0) + alpha) / (total_ngrams + alpha * len(ngram_counts))
        sentence_probability *= ngram_probability

    perplexity = math.pow(sentence_probability, -1/len(test_sentence))

    return perplexity

# 测试文本
test_sentence = '欧阳锋道：「你用绳子拖我。」'

# 设置n-gram的n值
n = 2

# 计算困惑度
perplexity = calculate_perplexity(test_sentence, test_sentence, n)
print("Perplexity:", perplexity)
