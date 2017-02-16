import nltk
import os
import jieba
import re


input_file= '../clean/real_text.txt'
output_file= '../clean/cut_text.txt'

def sentence_split(str_centence):
	list_ret = list()
	for s_str in str_centence.split('。'):
		if '?' in s_str:
			list_ret.extend(s_str.split('？'))
		elif '!' in s_str:
			list_ret.extend(s_str.split('！'))
		else:
			list_ret.append(s_str)
	return list_ret

def jieba_preprocess(in_filename, out_filename):
	in_file = open(in_filename, 'r')
	out_file = open(out_filename,'a')
	
	while True:
		line = in_file.readline()
		if not line:
			break
		line = line.strip()
		if not line:
			continue
		sentence = line
		cut_res = jieba.lcut(sentence, cut_all=True)
		remove_stopwords(cut_res)
		if not cut_res:
			continue
		new_line = ' '.join(cut_res)+'\n'
		out_file.write(new_line)

	in_file.close()
	out_file.close()

def cut2word(intputfilename,outputfilename):
	print('Jieba Preprocessing: ', inputfile)
	jieba_preprocess(intputfilename,outputfilename)

def line_cut(inputfile,outputfile):
	in_file = open(inputfile, 'r')
	out_file = open(outputfile,'a')

	for line in in_file.readlines():
		list_ret = sentence_split(line)
		for ret in list_ret:
			out_file.write(ret+'\n')
		out_file.write('\n')

line_cut(input_file,output_file)

print("Line Cut Done")




