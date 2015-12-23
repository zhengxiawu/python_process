# -*- coding:utf-8 -*-
import glob
import pprint
import os,sys
root_txt_dir = sys.argv[1]
for i in range((len(sys.argv)-1)/2):
  image_dir =  sys.argv[i*2+2]
  image_label = sys.argv[i*2+3]
  read = file(root_txt_dir,'a+')
  for file_name in glob.iglob(os.path.join(image_dir,'*.*')):
    if 'jpg' in file_name:
      file_array = file_name.split('/')
      read.write(file_name)
      read.write('  ')
      read.write(image_label)
      read.write('\n')

