import pandas as pd
import re
import jieba.analyse

def data_process(file='fj2.csv'):
    data = pd.read_csv(file, header=None, index_col=0, sep = ',', encoding = 'GB18030')
    data.columns = ['留言用户',	'留言主题',	'留言时间',	'留言详情',	'一级标签']
    n = 500

    #抽样
    a = data[data['一级标签'] == '城乡建设'].sample(n)
    b = data[data['一级标签'] == '环境保护'].sample(n)
    c = data[data['一级标签'] == '交通运输'].sample(n)
    d = data[data['一级标签'] == '教育文体'].sample(n)
    e = data[data['一级标签'] == '劳动和社会保障'].sample(n)
    f = data[data['一级标签'] == '商贸旅游'].sample(n)
    g = data[data['一级标签'] == '卫生计生'].sample(n)
    data_new = pd.concat([a, b, c, d, e, f, g], axis=0)

    data_dup = data_new['留言详情'].drop_duplicates()
    data_qumin = data_dup.apply(lambda x: re.sub('x', '', x))

    jieba.load_userdict('newdic1.txt')
    data_cut = data_qumin.apply(lambda x: jieba.lcut(x))

    stopWords = pd.read_csv('stopword1.txt', encoding='GB18030', sep='hahaha', header=None)
    stopWords = [' ', '\n', '\t', '\r\n', '\u3000', '＂', '–'] + list(stopWords.iloc[:, 0])
    data_after_stop = data_cut.apply(lambda x: [i for i in x if i not in stopWords])
    labels = data_new.loc[data_after_stop.index, '一级标签']
    adata = data_after_stop.apply(lambda x: ' '.join(x))
    data_after_stop = data_after_stop.to_frame()
    
	#提取关键词
    key=[]
    for i in adata:
        keywords=jieba.analyse.extract_tags(i,topK=20)
        key.append(keywords)
    data_after_stop['key']=key
    
	#去除城市乡镇以外的字母和0
    key=[]
    pattern = re.compile('[0-9]+')
    for x in data_after_stop['key']:
        temp=[]
        for i in x:
            match = pattern.findall(i)
            if match:
                pass
            else:
                temp.append(i)
        key.append(temp)
    data_after_stop['key']=key
    data_after_stop['labels']=labels
    return adata, data_after_stop, labels
#adata, data_after_stop, labels = data_process()

