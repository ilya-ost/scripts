#!/bin/sh

#
# @(#) ape2flac 0.1b 23/01/2007 by BaBL
# Checking for mac & flac
# Checking for input directory
#
# @(#) ape2flac 0.1a 14/01/2007 by BaBL
# Fixed a bug identifying filenames with more then one "." symbol
#
# @(#) ape2flac 0.1 26/09/2003 by Peo Karlsson
#
# Recursively convert APE-files to FLAC.
# Directory recursion adapted from the 'tree' script by Jordi Sanfeliu (see below).
#

#
# @(#) tree 1.1 30/11/1995 by Jordi Sanfeliu (mikaku@fiwix.org)
#
# Initial version: 1.0 30/11/95
# Next version : 1.1 24/02/97 Now, with symbolic links
#

# which extension to look for when browsing the tree

myext="ape"
declare -a prog_needed=(mac flac)

search () {
    xx=0
    for dir in *
    do
	if [ -f "$dir" ]; then
	    ext=`echo "$dir" | sed -ne 's!^.*\.!!p' | tr '[:upper:]' '[:lower:]'` &> /dev/null
	    base=`echo "$dir" | sed -e 's!\.[^.]*$!!'` &> /dev/null
	    if [ "$ext" = "$myext" ]; then
		echo -n ".";
		mac "$dir" - -d | flac - -o "$base.flac" &> /dev/null
		rm -f "$dir" &> /dev/null
		xx=`expr $xx + 1`
		numfiles=`expr $numfiles + 1`
	    fi
	else
	    if [ $xx > 0 ]; then
		echo " -> [$xx files converted]"
		xx=0
	    fi
	fi

	if [ -d "$dir" ]; then
	    zz=0
	    while [ $zz != $deep ]
	    do
		echo -n "| "
		zz=`expr $zz + 1`

	    done
	    if [ -L "$dir" ]; then
		echo -n "+---$dir" `ls -l $dir | sed 's/^.*'$dir' //'`
	    else
		echo -n "+---$dir"
		if cd "$dir"; then
		    deep=`expr $deep + 1`
		    search
		    numdirs=`expr $numdirs + 1`
		fi
	    fi
	fi
    done
    cd ..
    if [ "$deep" ]; then
	swfi=1
    fi
    deep=`expr $deep - 1`
}

if [ $# = 0 ]; then
    cd `pwd`
elif [ -e "$1" ]; then
    cd $1
else
    echo "Path \"$1\" not found"
    exit 0
fi

for i in ${prog_needed[@]}
do
    echo -n "Checking for $i..... "
    if which "$i" &> /dev/null; then
	echo "Yes"
    else
	echo "No"
	echo "Programm $i is not installed. Please install $i first"
	exit 0
    fi
done

echo
echo "ape2flac 0.1b"
echo
echo "bash script to convert files compressed by Monkey's Audio into FLAC files."
echo
echo "Converting all files in directory = `pwd` and recurse indefinitely."
echo
swfi=0
deep=0
numdirs=0
numfiles=0
zz=0
xx=0

while [ "$swfi" != 1 ]
do
    search
done
echo
echo "Summary:"
echo
echo "Total directories = $numdirs"
echo "Total files converted = $numfiles"
echo
exit 0