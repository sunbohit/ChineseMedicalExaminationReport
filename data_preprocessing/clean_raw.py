import os
import shutil

#print(os.path.pardir)
#print(os.path.join(os.path.pardir,"raw","fbzl"))

inputfolder = os.path.join(os.path.pardir,"raw")
outputfolder = os.path.join(os.path.pardir,"clean")

if not os.path.exists(inputfolder):
	print("Raw data do not exist !")

if os.path.exists(outputfolder):
	shutil.rmtree(outputfolder)

def clean_text(foldername):
	os.makedirs(os.path.join(outputfolder,foldername))
	for roots, dirs, files in os.walk(os.path.join(inputfolder,foldername)):
		for filename in files:
			inputfile = os.path.join(roots, filename)
			outputfile = os.path.join(os.path.join(outputfolder,foldername),filename)
			input_f = open(inputfile,"r")
			
			lines = input_f.readlines()
			# print(len(lines)) #10
			if len(lines[5].strip()) == 0 :
				continue
			
			output_f = open(outputfile, "a")
			output_f.write(lines[5])
			output_f.write(lines[7])
			output_f.write(lines[9])

clean_text("fbjc")
clean_text("fbzl")

print("Clean Done")