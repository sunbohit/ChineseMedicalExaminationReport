import os
raw_dir = '../WebSpider/CLLdownload'
pure_dir = './web_utf8'


def gbk2u8(level):
	files = os.listdir(os.path.join(raw_dir,level))
	for file in files:
		print(file)
		in_file = open(os.path.join(raw_dir,level,file), "r", encoding='gbk', errors='ignore')
		try:
			in_file.readlines()
			in_file = open(os.path.join(raw_dir,level,file), "r", encoding='gbk', errors='ignore')
		except:
			in_file = open(os.path.join(raw_dir,level,file), "r", encoding='utf-8')
		out_file = open(os.path.join(pure_dir,level,file), 'w', encoding='utf-8')
		while True:
			line = in_file.readline()
			if not line:
				break
			out_file.write(line)
		in_file.close()
		out_file.close()

gbk2u8("character")
gbk2u8("word")
