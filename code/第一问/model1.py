import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

from data_process1 import data_process
from sklearn.naive_bayes import GaussianNB, MultinomialNB
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import LinearSVC
from sklearn.model_selection import cross_val_score, train_test_split
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer, TfidfVectorizer
from sklearn.metrics import classification_report, accuracy_score, confusion_matrix

#朴素贝叶斯
adata, data_after_stop, labels = data_process()
data_tr, data_te, labels_tr, labels_te = train_test_split(adata, labels, test_size=0.2)

countVectorizer = CountVectorizer()
data_tr = countVectorizer.fit_transform(data_tr)
X_tr = TfidfTransformer().fit_transform(data_tr.toarray()).toarray()

data_te = CountVectorizer(vocabulary=countVectorizer.vocabulary_).fit_transform(data_te)
X_te = TfidfTransformer().fit_transform(data_te.toarray()).toarray()

model1 = GaussianNB()
model1.fit(X_tr, labels_tr)
print(model1.score(X_te, labels_te))

#其他四种模型
adata_key = data_after_stop['key']
adata_set = adata_key.apply(lambda x: ' '.join(x))

tfidf = TfidfVectorizer(norm='l2', ngram_range=(1, 2))
features = tfidf.fit_transform(adata_set)
models = [
   RandomForestClassifier(n_estimators=200, max_depth=3, random_state=0),
   LinearSVC(),
   MultinomialNB(),
   LogisticRegression(random_state=0),
]

#5折交叉验证
CV = 5
cv_df = pd.DataFrame(index=range(CV * len(models)))
entries = []
for model in models:
 model_name = model.__class__.__name__
 accuracies = cross_val_score(model, features, labels, scoring='accuracy', cv=CV)
 for fold_idx, accuracy in enumerate(accuracies):
   entries.append((model_name, fold_idx, accuracy))
cv_df = pd.DataFrame(entries, columns=['model_name', 'fold_idx', 'accuracy'])

#绘制箱线图
sns.boxplot(x='model_name', y='accuracy', data=cv_df)
sns.stripplot(x='model_name', y='accuracy', data=cv_df, 
              size=8, jitter=True, edgecolor="gray", linewidth=2)
plt.show()

#线性SVC模型调用
model = LinearSVC()
X_train, X_test, y_train, y_test, indices_train, indices_test = train_test_split(features, labels, data_after_stop.index, 
                                                                                 test_size=0.3, stratify=labels, random_state=0)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
 
#生成混淆矩阵
labelss = ['城乡建设','环境保护','交通运输','教育文体','劳动和社会保障','商贸旅游','卫生计生']
conf_mat = confusion_matrix(y_test, y_pred)
fig, ax = plt.subplots(figsize=(10,8))
sns.heatmap(conf_mat, annot=True, fmt='d',
            xticklabels=labelss, yticklabels=labelss)
plt.rcParams['font.sans-serif']='SimHei'
plt.ylabel('实际结果',fontsize=18)
plt.xlabel('预测结果',fontsize=18)
plt.show()
 
print('accuracy %s' % accuracy_score(y_pred, y_test))
print(classification_report(y_test, y_pred,target_names=labelss))
