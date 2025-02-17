#!/bin/bash

n=2
for i in {1..10}
do
re=$((i * n))
echo "$re"
done

for i in {2..20}
do 
re=$((i % 2))
if [ $re -eq 0 ];
then 
echo "$i"
fi
done
