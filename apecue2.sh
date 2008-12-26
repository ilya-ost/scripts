#!/bin/bash

file="$1"
cuebreakpoints "${file}.cue" | shnsplit -o wav "${file}.ape"
for wav in *.wav
do
    oggenc -q 8 "$wav"
done
cuetag "${file}.cue" *.ogg
rm *.wav
# rm CDImage.ape