#!/bin/bash
# 
# Zadanie 86 
# Filip Mazur
# 27.04.2018 11:15 TN 
# 
# Skrypt przekazuje jako plik tekstowy wynik polecenia ps aux, przekazuje do awka,
# nastepnie sumuje zawartosci fieldow 3 i 4 odpowiadajacych kolejno zuzyciu cpu
# oraz pamieci wszystkich aktywnych procesow i na koncu drukuje obliczone sumy.
#

ps aux | awk '{ sumcpu+=$3; summem+=$4 } END {print "CPU: ", sumcpu, "MEMORY: ", summem}'