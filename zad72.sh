#!/bin/bash
# 
# Zadanie 72
# MegaKruk
# 19.04.2018 11:15 TN 
# 
# Skrypt najpierw wyswietli ilosc uzytkownikow, a nastepnie jesli w argumencie podano nazwe katalogu
# skrypt wyswietli ile jest w nim plikow nalezacych do kazdego uzytkownika. Nastepnie wyswietli
# na ktorych uzytkownikow mozna sie zalogowac
#

# a)
echo "number of users: $(wc -l < /etc/passwd)"

argc=$#
if [ "$argc" -gt 0 ]
then
	# b)
	find "$1" -printf '%u\n' | sort | uniq -c
fi

# d)
for _iter in /etc/passwd 
do
	echo "users you can log on: $(grep -n "bin/bash" /etc/passwd | cut -d':' -f2)"
done 
