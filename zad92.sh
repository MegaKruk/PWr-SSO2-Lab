#!/bin/bash
# 
# Zadanie 92 
# Filip Mazur
# 27.04.2018 11:15 TN 
# 
# Skrypt sprawdza, czy podany w argumencie plik ma rozszerzenie .json,
# a nastepnie (prawie poprawnie) zmienia formatowanie tekstu w nim zawartego
# na "xml-owa" i na koncu zapisuje tak edytowany plik z rozszerzeniem .xml
#

if [ $# != 1 ] ; then
	echo "wrong argument number"
	exit 1
fi

if [[ $1 =~ \.json$ ]] ; then

# a), prawie b)
awk '{
	gsub(/{/,"<"); \
	gsub(/:/,">"); \
	gsub(/}/,"</____>"); \
	gsub(/"/,""); \
	print $0 }' $1 > output.xml
	
else
	echo "wrong file format"
	exit 1
fi
