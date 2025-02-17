#!/bin/bash

function Data(){

r=$1
r1=$2
res=$((r+r1))
echo "number of arguments $#"
return $res
}

Data 1 2
echo "$?"
echo "$0"

