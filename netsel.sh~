#!/bin/bash

seleth () {
    sudo cp /home/ilya/scripts/ethconf /etc/network/interfaces
    sudo ifconfig eth0 up
    sudo ifconfig wlan0 down
    sudo /etc/init.d/networking restart
}

selwlan () {
    sudo cp /home/ilya/scripts/wlanconf /etc/network/interfaces
    sudo ifconfig eth0 down
    sudo ifconfig wlan0 up
    sudo /etc/init.d/networking restart
}

case $1 in
    "eth")
	seleth
	;;
    "wlan")
	selwlan
	;;
    *)
	echo "usage: netsel.sh eth | wlan"
	;;
esac

