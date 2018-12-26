#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      InesQ
#
# Created:     26.12.2018
# Copyright:   (c) InesQ 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------


#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import pylab

x = pylab.arange(-10, 10.5, 0.5)
print(x)
len(x)
a = 3
y1 = [i / -3 + a for i in x if i <= 0]
len(y1)

x
x[0]
x[0:5]
x[:5]
x[:len(y1)]
len(x[:len(y1)])

len(x)
x[-10]
x[-10:]
len(y2)
x[-len(y2):]

pylab.plot(x[:len(y1)], y1)

y2 = [i**2 / 3 for i in x if i >= 0]

pylab.plot(x[:len(y1)], y1, x[-len(y2):], y2)