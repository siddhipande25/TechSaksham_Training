#!/bin/bash

read -p "enter first value " n1
read -p "enter second values " n2

if [ $n1 -gt $n2 ];
then
echo " $n1 is greater than the $n2"
else
echo " $n2 is greater than the $n1 "
fi
