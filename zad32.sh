#!/bin/bash
# 
# Zadanie 32 
# Filip Mazur
# 26.03.2018 11:15 TN 
# 
# Przy drugim wywołaniu skryptu wpadamy w wariant <ln [OPTION]... TARGET... DIRECTORY (3rd form)>
# Wchodzimy w prawie nieskoczona petle. Pozostawiam kod dla potomnych.
# Ogolnie program wykonuje hardlinki na plikach, softlinki na folderach i rekurencyjnie wywoluje sam siebie
# dla kazdego takiego podfolderu.  
#
if [ $# != 2 ] ; then
	echo "wrong argument number"
	exit 1
fi

for file in $1/*
do
	name="$(basename $file)"
	
	#if a folder
	if [ -d "$file" ] ; then
		#if folder
		ln -sf --target-directory="/home/megakruk/workspace/SO2-Lab/zad32/$1/$name" "/home/megakruk/workspace/SO2-Lab/zad32/$2/symlink_$name"
		#echo "created soft link $name"
		echo "$file"
		/home/megakruk/workspace/SO2-Lab/zad32/zad32.sh "$file" "$2"

	else
		#if not folder
		ln -f --target-directory="/home/megakruk/workspace/SO2-Lab/zad32/$1/$name" "/home/megakruk/workspace/SO2-Lab/zad32/$2/hardlink_$name"
		#echo "created hard link $name"
	fi
done
#echo "Done"
