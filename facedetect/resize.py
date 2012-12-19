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
    thumbnail = cv.CreateImage((size[0], size[1]), source.depth, source.nChannels)
    cv.Resize(source, thumbnail, interpolation = cv.CV_INTER_CUBIC);
    return thumbnail

source = "/Users/miaoever/Documents/MATLAB/scface/front_36_36_new/"
target = "/Users/miaoever/Documents/MATLAB/scface/front_12_12/"

if  not os.path.exists(source) :
    print "The source directory doesn't exit."
    exit()	

if  not os.path.exists(target) :	#Create target folder if it doesn't exist.
    os.mkdir(target)

list_files = os.walk(source)

for files in list_files :
    dataset = files[2]

for image in dataset :
    if isImage(source + image) : 
        img = cv.LoadImage(source + image, 0)
        res = resize_image(img, (12, 12))
        cv.SaveImage(target + image, res)
        print image,"Done!"
    else:
        print image, "is not image file!"
