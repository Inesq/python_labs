#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      studentwsb
#
# Created:     14-10-2018
# Copyright:   (c) studentwsb 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import random
slowa = ("farfocel","kaszanka","kurnik","halabarda","nutella")
word = random.choice(slowa)
#print (word)
poprawnie = word
pomie =""
while word:
    position = random.randrange(len(word))
    pomie += word[position]
    word = word[:position] + word[(position + 1):]
print (pomie)

print(
"""

Witaj w grze 'Wymieszane litery'!
Uporządkuj litery, aby odtworzyć prawidłowe słowo.
(Aby zakończyć zgadywanie, naciśnij klawisz Enter bez
podawania odpowiedzi.)
"""
)
print("Zgadnij, jakie to słowo:", pomie)
zgaduj = input("\nTwoja odpowiedź: ")
i=0
while zgaduj != poprawnie and zgaduj != "" and i<=3:


    print("Niestety, to nie to słowo.")
    a=input("Czy za koszt 1 punktu podpowiedziec pierwsze slowo - mozesz zebrac maksymalnie 3? T / N ?")

    if a.upper()=="T":
            print(poprawnie[i])
            zgaduj = input("Twoja odpowiedź: ")
            i=i+1
    else:
        zgaduj = input("Twoja odpowiedź: ")
if zgaduj == poprawnie:
    print("Zgadza się! Zgadłeś!\n")
    print(3-i)
print("Dziękuję za udział w grze.")