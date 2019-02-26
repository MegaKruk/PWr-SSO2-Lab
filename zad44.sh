#!/bin/bash
# 
# Zadanie 44
# MegaKruk
# 19.04.2018 11:15 TN 
# 
# Skrypt znajduje w katalogu podanym przez parametr ile jest
# folderow z podfolderem o nazwie ".git" nie starszym niz miesiac
#

argc=$#
if [ "$argc" -lt 1 ]
then
    echo "Podaj 1 argument!"
    exit
fi

currDirectory=$1
if [ ! -d $currDirectory ]
then
    echo "Argument nie jest katalogiem"
    exit
fi

find $currDirectory -name ".git" -newermt '1 month ago' | while read file
do
  realpath $file
done
