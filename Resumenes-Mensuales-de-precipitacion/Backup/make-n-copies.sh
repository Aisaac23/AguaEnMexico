#!/bin/sh

index=0
if [ -f "$1" ]
then
	while [ $index -lt $2 ] 
	do
		org="$1"
		new="-""$index"".txt"
		ext=".txt"
		dest=${org/$ext/$new}

		cp "$1" "$dest"
		index=`expr $index + 1`

	done
fi
