#!/bin/sh

newdir="$1"
newdir=${newdir%".rar"}
mkdir "$newdir"
cd "$newdir"
unrar e "$1" &> /dev/null &
