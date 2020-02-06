import os
import sys
from PIL import Image

def compressMe(file, verbose=False):
	filepath = os.path.join(os.getcwd(), file)
	oldsize = os.stat(filepath).st_size
	picture = Image.open(filepath)
	dim = picture.size
	ext = os.path.splitext(file)[1][1:]
	if ext == "jpg" or ext == "JPG":
		ext = "JPEG"
	#set quality= to the preferred quality. 
	#I found that 85 has no difference in my 6-10mb files and that 65 is the lowest reasonable number
	picture.save(file,ext,optimize=True,quality=85) 
	

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
		if os.path.splitext(file)[1].lower() in ('.jpg', '.jpeg', '.png'):
			num += 1
			compressMe(file, verbose)

if __name__ == "__main__":
	main()