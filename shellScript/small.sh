#!/bin/bash

read -p "first " n1
read -p "Second " n2
read -p "Third " n3
read -p "Fourth " n4

if [ $n1 -lt $n2 ] && [ $n1 -lt $n3 ] && [ $n1 -lt $n4 ];
then
echo "$n1 is smaller than other numbers"
elif [ $n2 -lt $n1 ] && [ $n2 -lt $n3 ] && [ $n2 -lt $n4 ];
then 
echo "$n2 is smaller than other number"
elif [ $n3 -lt $n1 ] && [ $n3 -lt $n2 ] && [ $n3 -lt $n4 ];
then
echo "$n3 is smaller than other numbers"
else
echo "$n4 is smaller than other numbers"
fi
