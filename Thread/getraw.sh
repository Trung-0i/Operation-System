#!bin/bash
avail=1
count=0
while ((avail==1)) && ((count<=10))
do
 raw=$(top -b -d 3 -n 1 | grep gk_hdh.py | awk '{print $1 " " $6 " " $9}')
 if [[ $ram ]]; then
  echo "$ram" >> data.txt
  count=0
 else
  echo "done"
  i=1
  let "count+=1"
 fi
done