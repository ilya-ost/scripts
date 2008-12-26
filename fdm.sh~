#! /bin/bash

filetype=$(echo "$1" | awk -F. '{print $NF}')

torrentdir=~/downloads/torrents/session/
downdir=~/downloads/
textsdir=~/texts/
audiodir=~/audio/
videodir=~/video/

# usage: smartmv filename destdir
# moves filename to destdir changing its name if nessesary
smartmv () {
    filetype=$(echo "$1" | awk -F. '{print $NF}')
    name=$(basename "$1" .$filetype)
    dir=$2
    if [ -e ${dir}${name}'.'${filetype} ]
    then
	i=1
	while [ -e ${dir}${name}'('${i}')''.'${filetype} ]
	do
	    ((i+=1))
	done
	mv "$1" "${dir}${name}(${i}).${filetype}"
    else
	mv "$1" "${dir}${name}.${filetype}"
    fi

}

case $filetype in
    torrent|TORRENT)
	mv "$1" "$torrentdir"
	;;
    pdf|PDF|doc|DOC|djvu|DJVU|chm|CHM)
	mv "$1" "$textsdir"
	;;
    avi|AVI|mpg|MPG|wmv|WMV)
	smartmv "$1" "$videodir"
	;;
    mp3|MP3|wma|WMA|ogg|OGG)
	smartmv "$1" "$audiodir"
	;;
    rar)
	fn=$(basename "$1" .$filetype)
	smartmv "$1" "$downdir"
	cd "$downdir"
	mkdir "$fn"
	cd "$fn"
	unrar e "${downdir}/${fn}.$filetype" &> /dev/null &
	;;
    rm)
	smartmv "$1" "$videodir"
	;;
    esac
