import os

#string = '乙型肝炎患者'
#slist = list(string)
#print(slist) #['乙', '型', '肝', '炎', '患', '者']

inputfolder = os.path.join(os.path.pardir,"cut2word")
outputfolder = os.path.join(os.path.pardir,"cut2word")

inputfilename = 'clean2word.txt'
wordlistfilename = 'wordlist.txt'
charlistfilename = 'characterlist.txt'

wordset = set()
charset = set()

inputfile = open(os.path.join(inputfolder,inputfilename),'r')
lines = inputfile.readlines()

for line in lines:
	wordlist = line.strip().split()
	wordset.update(wordlist)
	for word in wordlist:
		charset.update(list(word))

inputfile.close()

wordlistfile = open(os.path.join(outputfolder,wordlistfilename),'a')
charlistfile = open(os.path.join(outputfolder,charlistfilename),'a')

for word in wordset :
	wordlistfile.write(word+'\n')
for character in charset :
	charlistfile.write(character+'\n') 

wordlistfile.close()
charlistfile.close()