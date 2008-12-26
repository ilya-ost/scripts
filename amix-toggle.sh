#! /bin/bash

if amixer get PCM | grep '\[on\]'
then
    amixer set PCM mute
else
    amixer set PCM unmute
fi