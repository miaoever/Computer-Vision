#!/usr/bin/env python
#Face detect and resize by OpenCV
#Author:	miaoever
#Email:		leo.miao.ever@gmail.com
#Date:		2012.11.28

import cv
import os

def isImage(image):
    ext_image = [".jpeg", ".bmp", ".jpg", ".png", ".gif"]
    ext = os.path.splitext(image.lower())[1]	#get extension name
    if ext in ext_image :
        return True
    else:
        return False

def resize_image(source, size) :				#size[0], size[1] represent the new height and width respectively
	#size = cv.GetSize(source)
#	print size[0], size[1]
	thumbnail = cv.CreateImage( ( size[0] , size[1]), source.depth, source.nChannels)
	cv.Resize(source, thumbnail, interpolation = cv.CV_INTER_CUBIC)
	return thumbnail

def facedetect(source, target, isResized = False, size=(0,0)) :
	hc = cv.Load("haarcascade_frontalface_alt.xml")
	img = cv.LoadImage(source, 0)
	#faces = cv.HaarDetectObjects(img, hc, cv.CreateMemStorage(),1.2, 2,cv.CV_HAAR_DO_CANNY_PRUNING, (37,50))
	faces = cv.HaarDetectObjects(img, hc, cv.CreateMemStorage(), 1.03, -1, 0, (10, 10))

	for (x,y,w,h),n in faces:
		if  (x,y,w,h) is None :
			return -1 
		cropped = cv.CreateImage((w, h), img.depth, img.nChannels)
		src_region = cv.GetSubRect(img, (x, y, w, h))	#Get the face region rectangle
		cv.Copy(src_region, cropped)			#Cropped out the face region 
		if isResized :
			cropped = resize_image(cropped, size)
		cv.SaveImage(target, cropped)
	return 0;



source = "/Users/miaoever/Documents/MATLAB/scface/front_100_100/"
target = "/Users/miaoever/Documents/MATLAB/scface/front_16_16/"
target_size = [16, 16]; 	#the size(in pixel) for target image.

if  not os.path.exists(source) :
    print "The source directory doesn't exit."
    exit()	

if  not os.path.exists(target) :	#Create target folder if it doesn't exist.
    os.mkdir(target)

list_files = os.walk(source)
for files in list_files :
	dataset =  files[2]
	
for image in dataset :
	if isImage(source + image) : 
		facedetect(source + image, target + image, True, target_size)
		print image + " Done!"
	else :
		print image, "is not image file!"

