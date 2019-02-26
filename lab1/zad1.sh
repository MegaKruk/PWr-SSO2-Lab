#!/bin/bash

#Laboratorium 1

#Zadanie 0A: Porównanie zawartości 2 katalogów (argumenty skryptu). 
#Przy porównaniu należy ignorować podkatalogi.
#W wyniku wyświetlić na ekranie listę plików o identycznych
#nazwach w obu katalogach.
#Udało mi się rozwiązać zadanie w 1 linijce tak jak chciałem :)

#MegaKruk
#16.03.18 11:15

find "$1" "$2" -printf '%P\n' | sort | uniq -d
