# Zadanie R2
# Filip Mazur
# 16.05.2018 11:15 TN
#
# Skrypt przechwytuje wyjście polecenia "cat sensors.txt" w formie binarnej, po czym iteruje
# po wierszach tak otrzymanego wyjścia. Każdy wiersz dzieli na tablicę wyrazów i wtedy iteruje
# po nich, jeśli dany wyraz zawiera w sobie znak "+" (zapewne jest to temperatura), to zapisuje
# ten wyraz do pliku "logfile"
#

import subprocess

logfile = open('logfile', 'wb')
proc=subprocess.Popen(['cat', 'sensors.txt'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
for line in proc.stdout:
    words = line.split()
    for word in words:
        if b"+" in word:
            logfile.write(word)
            logfile.write(b"\n")
proc.wait()
