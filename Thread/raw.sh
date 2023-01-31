#!/bin/bash
avail=1
count=0
while ((avail==1)) && ((count<=10))
do
  echo $1
  echo $(top -b -d 0,01 -n 1 | grep $1 | awk '{print $1 " " $6 " " $9}')
  # if [[ $ram>0 ]]; then
  #   echo "$ram" >> raw.txt
  #   count=0
  # else
  #   echo "done"
    let "count+=1"
  # fi
done
