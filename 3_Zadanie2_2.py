#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      InesQ
#
# Created:     26.12.2018
# Copyright:   (c) InesQ 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------



import pylab

x = pylab.arange(-10, 10.5, 0.5)  # lista argumentów x
a = int(input("Podaj współczynnik a: "))
y1 = [i / -3 + a for i in x if i <= 0]

print(x, len(x))
print(y1, len(y1))

pylab.plot(x, y1)
pylab.title('Wykres f(x)')
pylab.grid(True)
pylab.show()