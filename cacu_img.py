import glob
import pprint
import os
import sys
root_image_dir='/video/filtervideo/image/'
string_in = sys.argv[1]
string_not_in = sys.argv[2]
count=0
for image_file_name in glob.iglob(os.path.join(root_image_dir,'*.*')):
  if string_in in image_file_name and not(string_not_in in image_file_name):
    count+=1
pprint.pprint(count)
