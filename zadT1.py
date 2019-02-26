# Zadanie T1
# MegaKruk
# 15.06.2018 11:15 TN
#
# Skrypt na początku tworzy trzy wzorce potrzebne do zidentyfikowania numeru telefonu.
# Możliwe rodzaje numerów to:
# XXX-XXX-XXX
# +XX XXX XXX XXX
# Dzięki regex0 możemy łatwo zidentyfikować pierwszy rodzaj numeru.
# Jako, że program w kolejnym kroku iteruje po słowach w pliku tekstowym regex1 sprawdza,
# czy słowo "zaczyna się" jak drugi rodzaj numeru (+XX). Jeśli kolejne 3 słowa pasują do
# regex2 to możemy (trochę naiwnie!) założyc, że jest to numer telefonu.
# W wymienionej powyżej pętli iterującej po słowach w pliku na początku ustawiamy licznik
# informujący o tym, na jakim słowie w linijce się znajdujemy i dzielimy linię na słowa.
# Następnie ze słowa usuwamy nawiasy, które mogły się do niego "dokleić". Jeśli słowo okazało
# się być zgodne z pierwszym rodzajem numeru, jest drukowane. Jeśli słowo okazało się być zgodne
# z początkiem drugiego rodzaju numeru i trzy kolejne słowa mają długość 3, to z ostatniego
# z tych słów (words[i + 3]) usuwamy ewentualny nawias zamykający i drukujemy wszystkie 4 słowa.
#

import re

regex0= "\w{3}-\w{3}-\w{3}"
regex1= "\+\w{2}"
regex2= "\w{3}"

myFile = open("kant.txt", "r")
for line in myFile:
    i = 0
    words = line.split()
    for word in words:
        word = word.strip('(')
        word = word.strip(')')
        matchResult0 = re.match(regex0, word)
        if matchResult0:
            print(word)
        matchResult1 = re.match(regex1, word)
        if matchResult1:
            matchResult2 = re.match(regex2, words[i + 1])
            if matchResult2:
                matchResult3 = re.match(regex2, words[i + 2])
                if matchResult3:
                    matchResult4 = re.match(regex2, words[i + 3])
                    if matchResult4:
                        words[i + 3] = words[i + 3].strip(')')
                        print(word + " " + words[i + 1] + " " + words[i + 2] + " " + words[i + 3])
        i += 1
