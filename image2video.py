import cv2
import os
import numpy as np
import pprint 
import glob
import sys
def detect_shape(shape):
  if(shape[0]!=600 or shape[1]!=800 or shape[2]!=3):
    print 'error'  
def convert2video(outputvdeo,per_video_pic_name,video_width,video_height,fourcc):
  for image_path in per_video_pic_name:
    img = cv2.imread(image_path)
    image_height,image_width,layers = img.shape
    center = (image_width/2,image_height/2)
    #rotat image by 180 
    M = cv2.getRotationMatrix2D(center, 180, 1.0)
    img = cv2.warpAffine(img,M,(image_width,image_height))
    if video_width == image_width and video_height==image_height:
      img = cv2.flip(img,0)
      detect_shape(img.shape)
      outputvideo.write(img)
    elif float(video_width)/float(video_height)==float(image_width)/float(image_height):
      img = cv2.resize(img,(video_width,video_height))
      img = cv2.flip(img,0)
      detect_shape(img.shape)
      outputvideo.write(img)
    elif  float(video_width)/float(video_height)>float(image_width)/float(image_height):
      temp = np.zeros((video_height,video_width,3),np.uint8)
      new_width = float(image_width)*(float(video_height)/float(image_height))
      new_width = int(new_width)
      img = cv2.resize(img,(int(new_width),video_height))
      start_width = (video_width-new_width)/2
      temp[:,start_width:(start_width+int(new_width)),:]=img
      img = temp
      img = cv2.flip(img,0)
      detect_shape(img.shape)
      outputvideo.write(img)
    elif  float(video_width)/float(video_height)<float(image_width)/float(image_height):
      temp = np.zeros((video_height,video_width,3),np.uint8)
      new_height = float(image_height)*(float(video_width)/float(image_width))
      new_height = int(new_height)
      img = cv2.resize(img,(video_width,int(new_height)))
      start_height = (video_height-new_height)/2
      temp[start_height:(start_height+int(new_height)),:,:]=img
      img = temp
      img = cv2.flip(img,0)
      detect_shape(img.shape)
      outputvideo.write(img)
rootimagedir = '/home/shenyunhang/Documents/dataset/allcapture_square/'+sys.argv[1]+'/'
if not os.path.isdir(rootimagedir):
  print 'input arg error'
  pprint.pprint(rootimagedir)
rootvideodir = '/home/shenyunhang/Documents/dataset/allcapture_square/video/'
pprint.pprint(sys.argv[1])
rootimage_array = rootimagedir.split('/')
video_width = 800
video_height = 600
path = rootimage_array[len(rootimage_array)-2]
#count how many video
fourcc = cv2.VideoWriter_fourcc(*'XVID')
video_num = 0
i=0
pic_num_in_video=10000
per_video_pic_name=[]
for imagefile in glob.iglob(os.path.join(rootimagedir,'*.*')):
  if 'jpg'in imagefile or 'png' in imagefile:
    #storage in a list
    per_video_pic_name.append(imagefile)
    #set the num
    i+=1
    if i==pic_num_in_video:
      #make a video
      outputvideo = cv2.VideoWriter(rootvideodir+path+str(video_num)+'.avi',fourcc,10.0,(video_width,video_height))
      convert2video(outputvideo,per_video_pic_name,video_width,video_height,fourcc)
      i=0
      per_video_pic_name=[]
      pprint.pprint(per_video_pic_name)
      video_num+=1
#lat images to video
if len(per_video_pic_name)>0:
  outputvideo = cv2.VideoWriter(rootvideodir+path+str(video_num)+'.avi',fourcc,10.0,(video_width,video_height))
  convert2video(outputvideo,per_video_pic_name,video_width,video_height,fourcc)
