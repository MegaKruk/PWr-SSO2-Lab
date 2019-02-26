#!/bin/bash

#Laboratorium 1

#Zadanie 0A: Porównanie zawartości 2 katalogów (argumenty skryptu). 
#Przy porównaniu należy ignorować podkatalogi.
#W wyniku wyświetlić na ekranie listę plików o identycznych
#nazwach w obu katalogach.

#Filip Mazur 226018
#16.03.18 11:15

find "$1" "$2" -printf '%P\n' | sort | uniq -d

#Przepraszam bardzo za opóźnienie w dostarczeniu zadania.
#To już się nie powtórzy. 
#Udało mi się za to rozwiązać zadanie w 1 linijce tak jak chciałem