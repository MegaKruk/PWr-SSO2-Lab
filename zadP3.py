#!/usr/bin/env python3
#
# Zadanie P3
# MegaKruk
# 11.05.2018 11:15 TN
#
# Skrypt przyjmuje 2 katalogi jako argumenty, tworzy liste plikow z katalogu 1,
# oraz liste plikow z katalogu 2. Nastepnie iteruje po liscie 1 w petli
# i kopiuje elementy z katalogu 2. Jesli element z listy 1 powtarza sie w liscie 2,
# to nie jest on kopiowany
#

import os
import sys

src = sys.argv[1]
dst = sys.argv[2]


def move(src,dst):
        filelist = os.listdir(src)
        filelist2 = os.listdir(dst)
        check = 0
        for i in filelist:
                for j in filelist2:
                        if (src + "/" + i) == (dst + "/" + j):
                                check = 1
                if check == 1:
                        check = 0
                        print("file " + i + " omitted")
                        continue
                os.system("mv" + " " + src + "/" + i + " " + dst + "/" + i)


move(src, dst)
