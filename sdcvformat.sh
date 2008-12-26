#! /bin/bash

a=$1
a=${a:0:1}
aplay ~/audio/WyabdcRealPeopleTTS/${a}/${1}.wav &> /dev/null &

fwfl.py $*

# wn $* -over | fold -w 40 -s

echo
echo "---------------------------------------"
echo

sdcv $* |
sed 's/\/\//\n\n/g' | fold -w 40 -s
