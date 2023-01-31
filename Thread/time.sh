#!/bin/bash
timeVal=0
for i in {1..100}
do
  start=$(date +%s.%6N)
  python3 $1 -n $2 -l $3
  end=$(date +%s.%6N)
  timeVal=`echo $timeVal+$end-$start | bc`
done
echo "scale=6; $timeVal/100" | bc >> time.log
