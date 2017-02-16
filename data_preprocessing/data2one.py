import os
input_folder_1 = '../clean/fbjc'
input_folder_2 = '../clean/fbzl'
output_folder= '../clean'

def prepare_data(input_folder):
	fb_dict = {}
	for roots, dirs, files in os.walk(input_folder):
		for filename in files:
			inputfile = os.path.join(roots, filename)
			outputfile = os.path.join(output_folder,'real_text.txt')
			print('Prepare: ', inputfile)
			input_open = open(inputfile,'r')
			output_open = open(outputfile,'a')
			line = input_open.readline()
			output = output_open.write(line)
			input_open.close()
			output_open.close()

prepare_data(input_folder_1)
prepare_data(input_folder_2)

print("Done")