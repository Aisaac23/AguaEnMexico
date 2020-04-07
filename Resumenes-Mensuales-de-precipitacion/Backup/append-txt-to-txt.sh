#!/bin/sh

index=0
to_append=`cat $1`
if [ -f "$1" ]
then
	while [ $index -lt $2 ] 
	do

		echo "$to_append" >> "$1"
		index=`expr $index + 1`
		echo $index
	done
fi
