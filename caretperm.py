#!/usr/bin/env python
import random, sys

__author__  = "Jeff White [karttoon] @noottrak"
__email__   = "karttoon@gmail.com"
__version__ = "1.0.0"
__date__    = "10APR2017"

stringVal = sys.argv[1]
pValues = {}
newVal = [stringVal]

for i in stringVal:
    pValues[i] = [i, "^" + i]

while True:
    stringGen = stringVal[0]
    for i in stringVal[1:]:
        stringGen += pValues[i][random.randrange(2)]
    if stringGen not in newVal and stringVal not in stringGen:
        newVal.append(stringGen)
        print stringGen
