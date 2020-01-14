"""
date: 2020.1.14
author: wentao
python3.7
cpu:i7-8750H
Gpu:GTX-1050i
code:  fasttext工具在清华文本数据集的简单分类
fasttext安装包：https://www.lfd.uci.edu/~gohlke/pythonlibs/#fasttext  下载对应版本即可
清华大学的新闻分类文本数据集下载：https://thunlp.oss-cn-qingdao.aliyuncs.com/THUCNews.zip
下载后进行解压，把相应的中文目录替换成以下英文名，方便程序读取数据
['affairs','constellation','economic','edu','ent','fashion','game','home','house','lottery','science','sports','society','stock']

"""

import jieba
import os
import fasttext
basedir="D:\THUCNews\THUCNews/"#这是我的文件地址，需跟据文件夹位置进行更改
dir_list=['affairs','constellation','economic','edu','ent','fashion','game','home','house','lottery','science','sports','society','stock']
ftrain=open("news_fasttext_train.txt","w",encoding="utf-8")  #生成训练集和测试集，encoding编码需要加上，否则会出现报错
ftest=open("news_fasttext_test.txt","w",encoding="utf-8")

num=-1
for e in dir_list:
    num+=1
    indir=basedir+e+'/'
    files=os.listdir(indir)
    count=0
    for fileName in files:
        count+=1
        filepath=indir+fileName
        with open(filepath,'r',encoding="utf-8") as fr:
            text=fr.read()
        text=str(text.encode("utf-8"),'utf-8')
        seg_text=jieba.cut(text.replace("\t"," ").replace("\n"," "))
        outline=" ".join(seg_text)
        outline=outline+"\t_label_"+e+"\n"

        if count<10000:
            ftrain.write(outline)
            ftrain.flush()
            continue
        elif count<20000:
            ftest.write()
            ftest.flush()
            continue
        else:
            break
ftrain.close()
ftest.close()
print("---------dataset done--------")


classifier=fasttext.train_supervised("news_fasttext_train.txt",label_prefix="_label_")  #训练模型
classifier.save_model("Model.bin")   #保存模型
# classifier=fasttext.load_model('Model.bin')   #已经有训练好的模型的话，直接加载训练好的模型
print("---------train done----------")

#预测，输出准确率
result=classifier.test("news_fasttext_test.txt")
print('precision:   ',result[1])

print("---------输出各类的统计情况----------")
#以下模块可以统计不同分类的结果
labels_right = []
texts = []
with open("news_fasttext_test.txt",encoding="utf-8") as fr:
    for line in fr:
        line = str(line.encode("utf-8"), 'utf-8').rstrip()
        labels_right.append(line.split("\t")[1].replace("__label__",""))
        texts.append(line.split("\t")[0])
    #     print labels
    #     print texts
#     break
labels_predict = [term[0] for term in classifier.predict(texts)[0]] #预测输出结果为二维形式
# print labels_predict

text_labels = list(set(labels_right))
text_predict_labels = list(set(labels_predict))
print(text_predict_labels)
print(text_labels)
print()


A = dict.fromkeys(text_labels,0)  #预测正确的各个类的数目
B = dict.fromkeys(text_labels,0)   #测试数据集中各个类的数目
C = dict.fromkeys(text_predict_labels,0) #预测结果中各个类的数目
for i in range(0,len(labels_right)):
    B[labels_right[i]] += 1
    C[labels_predict[i]] += 1
    if labels_right[i] == labels_predict[i].replace('__label__', ''):
        A[labels_right[i]] += 1

print('预测正确的各个类的数目:', A)
print()
print('测试数据集中各个类的数目:', B)
print()
print('预测结果中各个类的数目:', C)
print()
#计算准确率，召回率，F值
for key in B:
    try:
        r = float(A[key]) / float(B[key])
        p = float(A[key]) / float(C['__label__' + key])
        f = p * r * 2 / (p + r)
        print("%s:\t p:%f\t r:%f\t f:%f" % (key,p,r,f))
    except:
        print("error:", key, "right:", A.get(key,0), "real:", B.get(key,0), "predict:",C.get(key,0))