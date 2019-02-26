#!/usr/bin/env python3
#
# Zadanie Q3
# MegaKruk
# 11.05.2018 11:15 TN
#
# Skrypt najpierw sprawdza, czy podano dwa argumenty (!= 3, bo "argumentem 0"
# jest wywołanie skryptu), następnie sprawdza, czy podane w argumentach
# katalogi mają uprawnienia rw konieczne do prawidłowego działania programu.
# W kolejnym kroku skrypt wywołuje funkcję, ktora tworzy listy plików obu
# podanych katalogów, a następnie na podstawie wyboru liczby pseudolosowej
# "decyduje" czy przenosić pliki z pierwszego katalogu do drugiego, czy
# z drugiego do pierwszego. Kolejno dla każdego pliku z odpowiedniej listy
# program "decyduje" na bazie kolejnego wyboru liczby pseudolosowej czy dany
# plik przenieść czy nie.
#

import os
import sys
import random

if len(sys.argv) != 3:
    print("Wrong arguments number")
    sys.exit(1)


src = sys.argv[1]
dst = sys.argv[2]


pcheck1 = os.access(src, os.R_OK)
pcheck2 = os.access(dst, os.W_OK)
pcheck3 = os.access(dst, os.R_OK)
pcheck4 = os.access(src, os.W_OK)

if(pcheck1 == False) or (pcheck2 == False) or (pcheck3 == False) or (pcheck4 == False):
        print("Wrong permissions")
        sys.exit(1)


def move(src, dst):
        filelist = os.listdir(src)
        filelist2 = os.listdir(dst)
        rand1 = random.randint(0, 99)
        if rand1 < 50:
                for i in filelist:
                        rand2 = random.randint(0, 99)
                        if rand2 < 50:
                                os.system("mv" + " " + src + "/" + i + " " + dst + "/" + i)
        else:
                for i in filelist2:
                        rand3 = random.randint(0, 99)
                        if rand3 < 50:
                                os.system("mv" + " " + dst + "/" + i + " " + src + "/" + i)


move(src, dst)
