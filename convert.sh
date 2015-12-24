dir=$1
for name in $dir; do
     echo $name
     convert -resize 256x256\! $name $name 
 done
