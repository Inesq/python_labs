#-------------------------------------------------------------------------------
# Name:        module4
# Purpose:
#
# Author:      InesQ
#
# Created:     26.12.2018
# Copyright:   (c) InesQ 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

a = int(input('Podaj współczynnik a: '))
b = int(input('Podaj współczynnik b: '))
x = range(-10, 11)  # lista argumentów x

# wyrażenie listowe wylicza dziedzinę y
y = [a * i + b for i in x]  # lista wartości