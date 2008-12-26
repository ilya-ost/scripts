#! /bin/bash

type=$(echo "$1" | awk -F. '{print $NF}')
echo $type > ~/.test.log

case $type in
    html|HTML|htm|HTM)
	iceweasel "$1" &> /dev/null &
	;;
    chm|CHM)
	okular "$1" &> /dev/null &
	;;
    pdf|PDF)
	evince "$1" &> /dev/null & 
	;;
    ps)
	evince "$1" &> /dev/null & 
	;;
    djvu|DjVu)
	evince "$1" &> /dev/null & 
	;;
    jpg|jpeg)
	gqview "$1" &> /dev/null & 
	;;
    psd|PSD)
	gimp "$1" &> /dev/null &
	;;
    svg)
	gimp "$1" &> /dev/null &
	;;
    ogv|mpg|mpeg|MPG|avi|AVI|flv|VOB|wmv|WMV|ogg|OGG|mp4|mov|wav|mkv|divx|ogm|m4v|asf)
	mplayer -fs "$1" &> /dev/null &
	;;
    rm|rmvb)
	realplayer "$1" &> /dev/null &
	;;
    m3u|mp3|MP3|ogg|OGG|flac)
	emacsclient -e '(emms-add-dired)'
	;;
    rar)
	newdir="$1"
	newdir=${newdir%".rar"}
	mkdir "$newdir"
	cd "$newdir"
	unrar e "$1" &> /dev/null &
	;;
    RAR)
	newdir="$1"
	newdir=${newdir%".RAR"}
	mkdir "$newdir"
	cd "$newdir"
	unrar e "$1" &> /dev/null &
	;;
    zip)
	newdir="$1"
	newdir=${newdir%".zip"}
	mkdir "$newdir"
	unzip "$1" -d "$newdir" &> /dev/null &
	;;
    tar)
	newdir="$1"
	newdir=${newdir%".tar"}
	mkdir "$newdir"
	cd "$newdir"
	tar -xf "$1" &> /dev/null
	;;
    doc|odt|rtf)
	oowriter "$1" &> /dev/null &
	;;
    odp|ppt)
	export OOO_FORCE_DESKTOP=kde; ooimpress "$1" &> /dev/null
	;;

esac

if [ "$1" == "/cdrom" ]
then
    mplayer -enqueue /cdrom/VIDEO_TS/* &> /dev/null 
fi

