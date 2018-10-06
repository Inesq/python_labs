#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      InesQ
#
# Created:     06.10.2018
# Copyright:   (c) InesQ 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
cena=float(input("wprowadź cenę samochodu. tylko liczby!"))
podatek=float(cena*0.10)
rejestracja=float(cena*0.15)
dealer=float(40)
dostarczenie=float(50)
suma=float(cena + rejestracja + dealer + dostarczenie)
print("cena auta: ", cena )
print("wysokość podatku: ", podatek )
print("rejestracja auta: ", rejestracja )
print("opłata dealera: ", dealer )
print("dostarczenie auta: ", dostarczenie )
print("razem: ", suma )