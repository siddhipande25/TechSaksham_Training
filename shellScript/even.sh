#!/bin/bash

read -p "enter the number " num

res=$(( num % 2 ))
if [ $res -eq 0 ];
then 
echo "$num is and even number"
else
echo "$num is an odd number"
fi
