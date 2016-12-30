import os
import shutil
import jieba
import re

inputfolder = os.path.join(os.path.pardir,"clean")
outputfolder = os.path.join(os.path.pardir,"cut2word")
outputfilename = 'clean2word.txt'

def load_stopwords():
	print('Load Stopword')
	stopfile = open('stopword')
	stopwords_library = set([])
	while True:
		word = stopfile.readline().strip()
		if not word:
			break
		stopwords_library.add(word)
	return stopwords_library

stopwords_library = load_stopwords()
print(stopwords_library)

if not os.path.exists(inputfolder):
	print("Clean data do not exist !")

if os.path.exists(outputfolder):
	shutil.rmtree(outputfolder)
os.mkdir(outputfolder)

def remove_stopwords(cut_origin=[]):
	for i in cut_origin:
		if i in stopwords_library:
			cut_origin.remove(i)
	


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

def cut2word(foldername):
	for roots, dirs, files in os.walk(os.path.join(inputfolder,foldername)):
		for filename in files:
			inputfile = os.path.join(roots, filename)
			outputfile = os.path.join(outputfolder,outputfilename)
			print('Jieba Preprocessing: ', inputfile)
			jieba_preprocess(inputfile, outputfile)

cut2word("fbjc")
cut2word("fbzl")

print("Cut2word Done")