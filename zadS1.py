# Zadanie S1
# Filip Mazur
# 16.05.2018 11:15 TN
#
# Skrypt przechwytuje wyjście polecenia "netstat -tulpn" w formie binarnej, po czym  iteruje po kolejnych
# wierszach wyjścia (ignorując wiersze 0-4). Dla każdego kolejnego wiersza rozdziela go na tablice słow
# (domyślny separator to spacja, więc zadziała też dla tabulacji) i drukuje czwarte słowo każdego wiersza
#

import subprocess

def function():
    proc=subprocess.Popen(['netstat', '-tulpn'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    i = 0
    for line in proc.stdout:
        i += 1
        if i < 5:
            continue
        words = line.split()
        print(words[3])
    proc.wait()


function()
