#!/bin/sh
# xmonad use with a pipe talking to an external program
PIPE=$HOME/.xmonad/status
rm -f $PIPE
PATH=${PATH}:/sbin mkfifo -m 600 $PIPE
[ -p $PIPE ] || exit

xmonad > $PIPE &
xmpid=$!
xmobar &
sleep 1
conky 
conky -c ~/.conkyrc1
stalonetray &
klipper &
~/.dropbox-dist/dropboxd &

# wait for xmonad
wait $xmpid

killall xmobar
