import os
import jieba

input_folder_1 = '../clean/fbjc'
input_folder_2 = '../clean/fbzl'
output_folder_1 = './clean_select/fbjc'
output_folder_2 = './clean_select/fbzl'

def cutchar_preprocess(in_filename, out_filename):
	in_file = open(in_filename, 'r')
	out_file = open(out_filename,'a')
	
	lines = in_file.readlines()
	
	if len(lines) != 3:
		return

	line = lines[0]
	line = line.strip()
	if len(line)<10:
		return
	sentence = line
	cut_res = list(sentence)

	new_line = ' '.join(cut_res)+'\n'
	out_file.write(new_line)

	tag = lines[1]
	tag = tag.strip()
	if len(tag)<5:
		return
	sentence = tag
	cut_res = list(sentence)
	new_line = ' '.join(cut_res)
	out_file.write(new_line)


	in_file.close()
	out_file.close()

def len_count(in_filename,filename,fb_dict):
	in_file = open(in_filename, 'r')
	
	lines = in_file.readlines()
	if len(lines) != 3:
		return

	line = lines[0]
	alen = len(line)
	#print(alen)
	fb_dict[filename] = alen

	in_file.close()

def prepare_data(input_folder):
	fb_dict = {}
	for roots, dirs, files in os.walk(input_folder):
		for filename in files:
			inputfile = os.path.join(roots, filename)
			outputfile = os.path.join(output_folder_1,filename)
			#print('Select: ', inputfile)
			len_count(inputfile,filename,fb_dict)
	print(fb_dict.values())
	fb_dict = sorted(fb_dict.items(), key=lambda x:x[1])
	print(fb_dict)
	print(len(fb_dict))


prepare_data(input_folder_1)
prepare_data(input_folder_2)

print("Done")
