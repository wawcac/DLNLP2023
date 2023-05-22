import re
import math
import glob

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


# stop_words=[
#     '\u3000',
#     '　',
#     ' ',
#     '\r',
#     '\n',
#     '本书来自www.cr173.com免费txt小说下载站更多更新免费电子书请关注www.cr173.com',
#     '----〖新语丝电子文库(www.xys.org)〗',
#     'K□⒃谀歉鲂∩角鹕希?远远汀酢鮺Hx?KHK5DUJEnV.<dIUVxR;6Q4s;p#,Rt~}',
#     '诹Ρ阆□跻淮危肺涔χK#,UfFxDZA&JG5ZR;R*~}',
#     '按蘖蔚毒投纾炝加玫锻弦挥扒亨ァ币簧魑蕉危允恰皣Ｒ啷啷',
#     '制台鹄矗岳砣袈！彼炖锼涫钦饷此担涫的茄皆缫雅踝潘掏玻谀抢锼藕蛄恕Ｄ歉鋈税盐胰玫娇妥铮约河眯渥臃魇昧艘巫樱胛易拢缓蠼庸掏玻鬃运蜕稀４耸币咽橇碛幸桓鲅剑萆喜枥戳恕Ｄ侨吮阄实溃骸澳銇薪纯瓷趺词榘。拷穸鲆焐趺词槟兀?',
#     '(金庸)',
#     '(na)',
#     '笑傲江湖３１',
#     '[完]',
#     '（end）',
#     '□',
#     '',
#     'doubleads（）;',
#     '返回目录',
#     '上一章',
#     '下一章',
#     '<图片>',
# ]
# replace_words=[
#     ('<<','《'),
#     ('>>','》'),
#     ('氵㸒','淫'), # 词向量没有'㸒'
# ]

# titles=[]
# novels=[]
# for i in glob.glob('../text/*.txt'): # 金庸全集
#     titles.append(i.split('\\')[-1].split('.')[0])
#     with open(i, 'r', encoding='gb18030') as f:
#         novel=f.read()
        
#     for stop_word in stop_words: # 过滤非小说内容
#         novel=novel.replace(stop_word,'')
#     for k,v in replace_words:
#         novel=novel.replace(k,v)
    
#     novel = re.sub("[a-zA-Z0-9"+ re.escape('@$&<>:.,;-()') +"]{5,}", "", novel) # 删除连续的字母+数字，较短的可能是章节编号
#     if len(novel)>=2000:
#         novels.append(novel)

# all_string=''.join(novels)

# # 测试文本作为语料库
# corpus =all_string

# 测试文本
test_sentence = '欧阳锋破口大骂。郭靖不再理他，纵马走开。奔出数十丈，听得他惨厉的呼声远远传来，心下终是不，忍叹了口气，回马过来，见泥沙已陷到他颈边。郭靖道：「我救你便是。但马上骑了两人，马身吃重，势必陷入泥沼。」'

# 设置n-gram的n值
n = 2

# 计算困惑度
perplexity = calculate_perplexity(test_sentence, test_sentence, n)
print("Perplexity:", perplexity)
