#1.传入csv文件分词
#2.分词
#3.写入excel
#4.处理excel文件 去除停用词中间的空格（定位 然后将单元格左移）
#5.再次读入excel （将dataframe 转化为list  此时的list是嵌套的list，需要展平）
#6.再次清理数据 去除nan \t等
#7.统计词频

from matplotlib.pylab import style


from matplotlib import font_manager

import xlwt
import warnings
warnings.filterwarnings("ignore")
import jieba
import pandas as pd
import collections
import matplotlib.pyplot as plt

#导入数据所在位置
data=pd.read_csv(open(r'E:\dor\111\total.csv'))
#print(data)
import wordcloud
from wordcloud import WordCloud

#创建一个新的xls准备写入分词后的数据
newb=xlwt.Workbook(encoding='utf-8') #创建新的工作簿
nws=newb.add_sheet('1') #添加工作表

#读取GitHub上下载的中文停用词库
stopwords = [line.strip() for line in
                 open(r'E:\dor\111\characters-master\characters-master\stt.txt', encoding='UTF-8').readlines()]


#遍历数据
for index,row in data.iterrows():
    for i in range(len(row)):
        #print(jieba.lcut(row[i]))
        list1=jieba.lcut(row[i])          #jieba分词
        len1=len(jieba.lcut(row[i]))      #分了多少个词
        for j in range(0,len1):           #写入excel文件
            if(list1[j] not in stopwords):
                nws.write(index, j, list1[j])     #分别为：行，列，数据

newb.save('result.xls')



# 读取定位处理后的数据
data2=pd.read_csv(open(r'E:/dor/111/total.csv'))
print(data2)



#dataframe转化为列表
list2=data2.values.tolist()

#print(list2)



#将列表展平

c = []
for i in list2:
    c.extend(i)                                                  #将list2展开 （嵌套的list展开为普普通的list）


                                                                #再次清理数据
datadd=[]
for word in c:
    if word is not '\n':
        if word is not '\t':
            if word is not ' ':
                datadd.append(word)


# 词频统计
word_counts = collections.Counter(datadd) # 对分词做词频统计
word_counts_top30 = word_counts.most_common(11) # 获取前30最高频的词
#去除nan
wordnoone=word_counts_top30[1:11]
print(wordnoone)


###解决中文乱码的问题
style.use('ggplot')
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

##要根据词频统计结果写入
value=[112,55,55,48,42,42,40,36,34,34]
xl=["高考","水平","测试","汇编","西藏","训练","数学","真题","模拟","对接"]



#绘制词云柱状图
#plt.bar(range(len(value)),value,color='grey', tick_label=xl)
#plt.title("2012")
#plt.text(s=value)
#plt.show()
