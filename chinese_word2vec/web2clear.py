import os
import re

inputfolder = "./web_utf8"
outputfolder = "./training_data"

def clear(in_filename, out_filename):
	in_file = open(in_filename, 'r',encoding='utf-8')
	out_file = open(out_filename,'a',encoding='utf-8')
	#topicword = in_filename.split("/")[-1].split(".")[0]

	while True:
		line = in_file.readline()
		if not line:
			break
		line = line.strip()
		if not line:
			continue
		pattern_1 = re.compile(r'^\s*\d+\s*:')
		pattern_2 = re.compile(r'【文件名.*】')
		pattern_3 = re.compile(r'\[(.*)\]')
		line = re.sub(pattern_1,'',line)
		line = re.sub(pattern_2,'',line)
		line = re.sub(pattern_3,r'\1',line)
		new_line = line.strip()
		out_file.write(new_line+'\n')

	in_file.close()
	out_file.close()	


def web2clear(level):
	files = os.listdir(os.path.join(inputfolder,level))	
	for filename in files:
		print('Clearing...:', filename)
		clear(os.path.join(inputfolder,level,filename), os.path.join(outputfolder, level, filename))

web2clear("word")
web2clear("character")
