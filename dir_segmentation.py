import glob
import os
import pprint
import shutil
root_image_dir = '/video/filtervideo/image'
root_dst_dir = '/video/filtervideo/segmentation/'
dst_dir_pro = 'volume'
dst_dir_num = 0
dst_dir_name=''
file_count=0
for image_file in glob.iglob(os.path.join(root_image_dir,'*.*')):
  if file_count==0:
    dst_dir_name=dst_dir_pro+str(dst_dir_num)
    os.mkdir(root_dst_dir+dst_dir_name)
  if 'png' in image_file:
    shutil.move(image_file,root_dst_dir+dst_dir_name+'/')
    file_count+=1
  if file_count==30001:
    file_count=0
    dst_dir_num+=1

