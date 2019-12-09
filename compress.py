import os
import sys
from PIL import Image

def compressMe(file, verbose=False):
	filepath = os.path.join(os.getcwd(), file)
	oldsize = os.stat(filepath).st_size
	picture = Image.open(filepath)
	dim = picture.size
	
	#set quality= to the preferred quality.
	picture.save("Compressed_"+file,"JPEG",optimize=True,quality=50) 
	
	newsize = os.stat(os.path.join(os.getcwd(),"Compressed_"+file)).st_size
	percent = (oldsize-newsize)/float(oldsize)*100
	if (verbose):
		print ("File compressed from {0} to {1} or {2}%".format(oldsize,newsize,percent))
	return percent

def main():
	verbose = False
	#checks for verbose flag
	if (len(sys.argv)>1):
		if (sys.argv[1].lower()=="-v"):
			verbose = True

	#finds present working dir
	pwd = os.getcwd()

	tot = 0
	num = 0
	for file in os.listdir(pwd):
		if os.path.splitext(file)[1].lower() in ('.jpg', '.jpeg'):
			num += 1
			tot += compressMe(file, verbose)
	print ("Average Compression: %d" % (float(tot)/num))
	print ("Done")
	
if __name__ == "__main__":
	main()
'''
Compressed Image Sizes
1)6.81 KB (6,978 bytes)
2)6.73 KB (6,900 bytes)
3)4.01 KB (4,114 bytes)
'''