#! /bin/bash

videodir=/home/ilya/video/

mplayer -dumpstream $(cat "$1" | grep 'rtsp://') -dumpfile ${videodir}"$2"

