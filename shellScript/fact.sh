#!/bin/bash
read -p "which number factorial you want to find " n
fact=1
for((a=1;a<=$n;a++))
do
fact=$((fact * a))
done
echo "factorial of $n is $fact"
