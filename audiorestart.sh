#!/bin/bash

killall -9 pulseaudio
killall mpd
pulseaudio -D
mpd