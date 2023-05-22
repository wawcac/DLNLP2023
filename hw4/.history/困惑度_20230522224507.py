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
test_sentence = '待得杨过再度攻上，他已乘这瞬息之间，将撕下的衣襟在左臂上一绕，包住了伤处，又觉伤口金是疼痛，并无麻□之感，看来剑上有毒多半是假，心中为之一宽。就在此时，只听得东南角上乒乒乓乓之声大作，兵刃相互撞击。杨过放眼望去，见小龙女手舞长剑，正自力战潇湘子与尼摩星两人。'

# 设置n-gram的n值
n = 2

# 计算困惑度
perplexity = calculate_perplexity(test_sentence, test_sentence, n)
print("Perplexity:", perplexity)
