#-------------------------------------------------------------------------------
# Name:        module3
# Purpose:
#
# Author:      InesQ
#
# Created:     26.12.2018
# Copyright:   (c) InesQ 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

a = 2
x = range(11)
for i in x:
    print(a + i)
y = [a + i for i in range(11)]
print(y)