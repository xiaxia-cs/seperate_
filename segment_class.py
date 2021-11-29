# encoding = utf-8
import jieba,csv
import os
#import collections
import paddle
from collections import defaultdict
import jieba.posseg as pseg
class Segmenter():
	paddle.enable_static()
	jieba.enable_paddle()

	#功能：读取停用词
	def __init__(self):
		self.stopwords = self.read_stopwords("stopwords_cn.txt")

		#读取停用词
	def read_stopwords(self,filename):
		with open(filename,'r',encoding='utf-8') as f:
			return [sw.strip() for sw in f.readlines()]

	def read_into_list(self,filename):
		filepath="C:\\Users\\HP\\Desktop\\seperate_write\\chinesetext"
		real_filename=filepath+"\\"+filename
		with open(real_filename,'r',encoding='utf-8') as f:
			return [sw.strip() for sw in f.readlines()]

	def wirte_out_file(self,filename,seglist):
		with open(filename,'w',encoding='utf-8-sig') as f:
			for sl in seglist:
				f.write(sl+'\n')



	def write_list_file(self,filename,sorted_list):
		with open(filename,'w',newline="",encoding='utf-8-sig') as f:
			writer = csv.writer(f)
			for i in sorted_list: #i --> (w,f)
				writer.writerow(i)

	def read_dir_name(self,filepath="C:\\Users\\HP\\Desktop\\seperate_write\\chinesetext"):
		
		list_file=os.listdir(filepath)
		
		return list_file
		#file=open("file_name.txt","w+")

		#for i in list_file:
			#print(i)
			


		


	def segment(self,fq=0):
		
		temp=[]
		temp_list=[]
		psegdict={}
		#停用词性
		stoppseg=["m","c","s","xc","w","p","d"]
		count_dict=defaultdict(int)
		list_file=self.read_dir_name()
		print("文本名称为：" , list_file)
		for file_name in list_file:
			doc_list=self.read_into_list(file_name)
			
			#print(doc_list)
			for doc in doc_list:
					#seg_list=jieba.cut(doc,use_paddle=True)
					words = pseg.cut(doc,use_paddle=True)
					for word,flag in words:
						print('%s %s' % (word, flag))
						psegdict[word] = flag 

					#print(psegdict)

					#temp_list=(list(seg_list))
					#temp.append("".join(temp_list))   #将词重新组成句子
					for key,value in psegdict.items():
						if value in stoppseg:
							continue
						elif key in self.stopwords:
							continue
						else:
							count_dict[key]+=1



					# 复原 for seg in temp_list:
				#改进2：根据词性过滤词汇
						# 复原 if seg in self.stopwords:
							# 复原 continue
			#https://github.com/fxsjy/jieba
				#if flag not in ["n","v","ad","a"]:
					#continue
						# 复原 else:
							# 复原 count_dict[seg]+=1


						#elif seg in count_dict:
							#count_dict[seg] += 1
						#else:
							#count_dict[seg] = 1


				
			#count_dict[seg]+=1
				
		print("done")
		print(count_dict,"countdict")
		print(temp)

		self.wirte_out_file("chinese_text_seg.txt", temp)
		word_freq = [(w,c) for w,c in sorted(count_dict.items(),\
					reverse=True,key=lambda item: item[1]) if c > fq]
		self.write_list_file("word_freq.csv",word_freq)