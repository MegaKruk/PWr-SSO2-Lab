#!/bin/bash 
# 
# Zadanie 23 
# Filip Mazur
# 26.03.2018 11:15 TN 
# 
# W komentarzu napisałem jak stworzyłem linki
# Pętla for przechodzi po wszystkich plikach w folderze $1
# i jeśli natknie się na dowiązanie zepsute (wskazujące na 
# nieistniejący plik - "! -e") to usuwa to dowiązanie
# 
#
for file in $1/*
do
	name="$(basename $file)"
	if [ ! -e "$file" ] ; then
		rm $file
		echo "deleted link $name"
	fi
	#ln -sf "$(pwd)/$1/$name" "$(pwd)/symlink_$name"
	#echo "created link $name"
done
echo "Done"
