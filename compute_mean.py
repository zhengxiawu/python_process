# -*- coding:utf-8 -*-
import pprint
import os,sys
import cv2
txt_dir = sys.argv[1]
f=open(txt_dir)
line=f.readline()
n=0
r_value=0
g_value=0
b_value=0
while line:
  tmp = line.split(' ')
  image_file_name = tmp[0]
  image = cv2.imread(image_file_name)
  r_value+=image[:,:,0].mean()
  g_value+=image[:,:,1].mean()
  b_value+=image[:,:,2].mean()
  n+=1
  line=f.readline()
  pprint.pprint(n)
r_value/=n
g_value/=n
b_value/=n
print(str(r_value)+':'+str(g_value)+":"+str(b_value))

