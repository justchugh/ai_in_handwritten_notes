#!/bin/python3

import os
import shutil
import cv2
import warnings

warnings.filterwarnings("ignore")


INDIR = "/home/abhishek/ramdisk/testing/images/"
OUTDIR = "/home/abhishek/ramdisk/testing/Character_classification/"



def show_img(image_data,delay=1000):
	cv2.imshow("img",image_data)
	cv2.waitKey(delay)
	cv2.destroyWindow("img")



def ask_user(image_data,delay=1000):
	show_img(image_data,delay)
	answer = str(input("what is the image..."))
	if answer == "wanna":
		show_img(image_data = image_data, delay = delay+3000)
		return ask_user(image_data,delay+3000)
	elif answer == "going" or len(answer) == 0 or len(answer) > 1:
		print("Exception")
		exit(0)
	return answer


def main():
	print("program start")
	# parsing through input dir
	for folder in os.scandir(INDIR):
		if folder.is_dir():
			print("entered folder:: "+str(folder.name))
			for file in os.scandir(folder.path):
				if file.is_file():
					image = cv2.imread(file.path)
					foldertoput = ask_user(image_data = image)
					pathoutdir = OUTDIR + foldertoput + "/"
					shutil.move(file.path, pathoutdir)



if __name__ == '__main__':
	main()