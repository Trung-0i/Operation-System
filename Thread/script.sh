#!/bin/bash
for i in `seq 10000 10000 100000`
do
  ./time.sh $1 $i $2 #& ./raw.sh $1
  echo 'done'
done