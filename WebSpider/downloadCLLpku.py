import os
import urllib.parse
import requests
import shutil

inputfolder = os.path.join(os.path.pardir,"cut2word")
inputfilename_word = os.path.join(inputfolder,"wordlist.txt")
inputfilename_char = os.path.join(inputfolder,"characterlist.txt")
outputfolder = "./CLLdownload/"

if os.path.exists(outputfolder):
	shutil.rmtree(outputfolder)

def downloadsearch(search,level):
	value_1 = {"download_serarch_result":search}
	searchstring_1 = urllib.parse.urlencode(value_1)
	value_2 = {"q":search}
	searchstring_2 = urllib.parse.urlencode(value_2)
	print(search)
  
	link = "http://ccl.pku.edu.cn:8080/ccl_corpus/search?"+searchstring_1+"&UserMaxHits=50000&dir=xiandai&"+searchstring_2+"&LastQuery=&num=50&index=FullIndex&outputFormat=TEXT&encoding=UTF-8&orderStyle=score&maxLeftLength=3000&maxRightLength=3000&scopestr="   
	targetDir = os.path.join(outputfolder,level)

	r = requests.get(link, stream=True)
	if r.status_code == 200:
		with open(os.path.join(targetDir,search+".txt"), 'wb') as f:
			r.raw.decode_content = True
			shutil.copyfileobj(r.raw, f)
	else:
		print(search," Error!")
		with open(targetDir+"Error.txt", 'a') as f:
			f.write(search+'\n')

inputfile_word = open(inputfilename_word,"r")
inputfile_char = open(inputfilename_char,"r")

os.makedirs(os.path.join(outputfolder,"word"))
for word in inputfile_word.readlines():
	search = word.strip()
	downloadsearch(search,"word")

os.makedirs(os.path.join(outputfolder,"character"))
for character in inputfile_char.readlines():
	search = character.strip()
	downloadsearch(search,"character")