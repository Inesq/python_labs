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

poczatek=float(input("podaj liczbe poczatkowa: "))
koniec=float(input("podaj liczbę koncowa: "))
krok=float(input("podaj wielkosc kroku co ile liczb odliczac: "))

while poczatek<koniec:
    poczatek+=krok #poczatek=poczatek+krok
    print(poczatek)