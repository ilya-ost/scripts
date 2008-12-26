#! /bin/bash

for i in "$*"
do
    mv "$i"/* ./
    rmdir "$i"
done