from data_process1 import data_process
from wordcloud import WordCloud
import matplotlib.pyplot as plt

adata, data_after_stop, labels = data_process()

word_fre1 = {}
word_fre2 = {}
word_fre3 = {}
word_fre4 = {}
word_fre5 = {}
word_fre6 = {}
word_fre7 = {}
data_key1 = data_after_stop[data_after_stop['labels'] == '城乡建设']
data_key2 = data_after_stop[data_after_stop['labels'] == '环境保护']
data_key3 = data_after_stop[data_after_stop['labels'] == '交通运输']
data_key4 = data_after_stop[data_after_stop['labels'] == '教育文体']
data_key5 = data_after_stop[data_after_stop['labels'] == '劳动和社会保障']
data_key6 = data_after_stop[data_after_stop['labels'] == '商贸旅游']
data_key7 = data_after_stop[data_after_stop['labels'] == '卫生计生']

for i in data_key1['key']:
    for j in i:
        if j not in word_fre1.keys():
            word_fre1[j] = 1
        else:
            word_fre1[j] += 1
wc1 = WordCloud(scale=16,background_color='white',
                        font_path=r'C:\Windows\Fonts\simhei.ttf',max_words = 100,max_font_size = 60)
wc1.fit_words(word_fre1)
#绘制词云图
#plt.imshow(wc1)
#plt.axis("off") 
#plt.show() 

for i in data_key2['key']:
    for j in i:
        if j not in word_fre2.keys():
            word_fre2[j] = 1
        else:
            word_fre2[j] += 1
wc2 = WordCloud(scale=16,background_color='white',
                        font_path=r'C:\Windows\Fonts\simhei.ttf',max_words = 100,max_font_size = 60)
wc2.fit_words(word_fre2)
#plt.imshow(wc2)
#plt.axis("off") 
#plt.show() 

for i in data_key3['key']:
    for j in i:
        if j not in word_fre3.keys():
            word_fre3[j] = 1
        else:
            word_fre3[j] += 1
wc3 = WordCloud(scale=16,background_color='white',
                        font_path=r'C:\Windows\Fonts\simhei.ttf',max_words = 100,max_font_size = 60)
wc3.fit_words(word_fre3)
#plt.imshow(wc3)
#plt.axis("off") 
#plt.show() 

for i in data_key4['key']:
    for j in i:
        if j not in word_fre4.keys():
            word_fre4[j] = 1
        else:
            word_fre4[j] += 1
wc4 = WordCloud(scale=16,background_color='white',
                        font_path=r'C:\Windows\Fonts\simhei.ttf',max_words = 100,max_font_size = 60)
wc4.fit_words(word_fre4)
#plt.imshow(wc4)
#plt.axis("off") 
#plt.show() 

for i in data_key5['key']:
    for j in i:
        if j not in word_fre5.keys():
            word_fre5[j] = 1
        else:
            word_fre5[j] += 1
wc5 = WordCloud(scale=16,background_color='white',
                        font_path=r'C:\Windows\Fonts\simhei.ttf',max_words = 100,max_font_size = 60)
wc5.fit_words(word_fre5)
#plt.imshow(wc5)
#plt.axis("off") 
#plt.show() 

for i in data_key6['key']:
    for j in i:
        if j not in word_fre6.keys():
            word_fre6[j] = 1
        else:
            word_fre6[j] += 1
wc6 = WordCloud(scale=16,background_color='white',
                        font_path=r'C:\Windows\Fonts\simhei.ttf',max_words = 100,max_font_size = 60)
wc6.fit_words(word_fre6)
#plt.imshow(wc6)
#plt.axis("off") 
#plt.show() 

for i in data_key7['key']:
    for j in i:
        if j not in word_fre7.keys():
            word_fre7[j] = 1
        else:
            word_fre7[j] += 1     
wc7 = WordCloud(scale=16,background_color='white',
                        font_path=r'C:\Windows\Fonts\simhei.ttf',max_words = 100,max_font_size = 60)
wc7.fit_words(word_fre7)
#plt.imshow(wc7)
#plt.axis("off") 
#plt.show() 
