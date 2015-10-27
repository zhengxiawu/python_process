#!/bin/bash
cd /video
post='.avi'
for i in `ls`
do 
length=${#i}
#获取后缀起始位置
postfix_start=`expr $length - 3`
#剔除后缀
name=${i:0:`expr $length - 4`}
#获取后缀
postfix=${i:$postfix_start:$length}
#判断文件类型
if [ "$postfix" = "avi" ]
then
#合成新的文件名
   name="/video/mp4/${name}.mp4"
#进行可是转换
   `ffmpeg -i ${i} ${name}`
#判断文件是否存在然后删除源文件
if [ -f "$name" ]
then
  `rm ${i}`
else
  echo 'error'
  exit 0
fi

fi
done

