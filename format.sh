#!/bin/sh

awk 'BEGIN {maxl = 28}
     { l = 0
       for ( i=1; i<=NF; ++i ){
           if (l > maxl){
	      printf "\n"
	      l = 0
	   }
	   printf $i" "
	   l = l + length ($i)
      }
      printf "\n" }'