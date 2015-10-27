import numpy as np
import cv2
import glob
import pprint
import os
root_video_dir='/video/filtervideo/MvTmp/temp/source/'
root_image_dir='/video/filtervideo/image/'
video_name_array=[]
for video_file in glob.iglob(os.path.join(root_video_dir,'*.*')):
  video_array = video_file.split('/')
  video_name = video_array[len(video_array)-1]
  video_name_spilt = video_name.split('.')
  if video_name_spilt[1]=='mp4':
    video_pro = video_name_spilt[0]
    video_pro_length = len(video_pro)
    while video_pro[video_pro_length-1].isdigit():
      video_pro_length-=1
    if video_pro[video_pro_length-1]=='o':
      video_pro_length+=1
    video_pro=video_pro[0:video_pro_length]
    #pprint.pprint(video_pro in video_name_array)
    #read the video
    pprint.pprint(video_pro)
    cap = cv2.VideoCapture(root_video_dir+video_name)
    i=0
    ret,frame = cap.read()
    while(ret):
      if not(frame==None):
        cv2.imwrite(root_image_dir+video_pro+str(i)+'.png',frame)
      ret,frame = cap.read()
      i+=1
    cap.release()
