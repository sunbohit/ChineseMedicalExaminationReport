import jieba
import os

inputfolder = "./training_data"
outputfolder = "./training_data"

def load_stopwords():
	print('Loading stopword')
	stopfile = open('stopword')
	stopwords_library = set([])
	while True:
		word = stopfile.readline()
		if not word:
			break
		stopwords_library.add(word)
	return stopwords_library

stopwords_library = load_stopwords()

def remove_stopwords(cut_origin):
	for i in cut_origin:
		if i in stopwords_library:
			cut_origin.remove(i)

def train_word(in_filename, out_filename, cut_all):
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
		cut_res = jieba.lcut(sentence, cut_all=cut_all)
		# remove_stopwords(cut_res)
		if not cut_res:
			continue
		new_line = ' '.join(cut_res)+'\n'
		out_file.write(new_line)

	in_file.close()
	out_file.close()	

def train_char(in_filename, out_filename):
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
		cut_res = list(sentence)
		# remove_stopwords(cut_res)
		if not cut_res:
			continue
		new_line = ' '.join(cut_res)+'\n'
		out_file.write(new_line)

	in_file.close()
	out_file.close()

def clear2train(level)
	files = os.listdir(os.path.join(inputfolder,level))	
	for filename in files:
		print('Cuting...:', filename)
		train_word(os.path.join(data_dir, level, filename), os.path.join(output,'train_word_cutall_true.txt'),True)
		train_word(os.path.join(data_dir, level, filename), os.path.join(output,'train_word_cutall_false.txt'),False)
		train_char(os.path.join(data_dir, level, filename), os.path.join(output,'train_character.txt'))
