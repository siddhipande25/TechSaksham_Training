#!/bin/bash

b=1
for((a=0;a<=10;a))
do
echo "$b"
t=$a
a=$b
b=$((b + t))
done
