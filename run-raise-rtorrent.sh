#!/bin/bash

if pgrep rtorrent > /dev/null
then
    sakura -e 'screen -r rtorrent'
else
    sakura -e 'screen -S rtorrent rtorrent'
fi    