#!/usr/bin/env python
import re, base64, ast, sys

__author__  = "Jeff White [karttoon] @noottrak"
__email__   = "karttoon@gmail.com"
__version__ = "1.0.0"
__date__    = "18AUG2017"

inputString = sys.argv[1]

# Strip NULL bytes from Windows B64 encoded CP
inputString = (base64.b64decode(inputString)).replace("\x00","")

def charReplace(inputString):

    # Find group of obfuscated string
    obfGroup = re.search("(\"|\')(\{[0-9]{1,2}\})+(\"|\')[ -fF]+(\'.+?\'\))",inputString).group()

    # Build index and string lists
    indexList  = [int(x) for x in re.findall("\d+",obfGroup.split("-")[0])]
    stringList = ast.literal_eval("[" + re.search("(\"|\').+","-".join(obfGroup.split("-")[1:])[:-1]).group() + "]")

    # Build output string
    stringOutput = ""
    for value in indexList:
        stringOutput += stringList[value]

    # Replace original input with obfuscated group replaced
    return inputString.replace(obfGroup, stringOutput)

# Iterate over each group until all replaced
while re.search("(\"|\')(\{[0-9]{1,2}\})+(\"|\')[ -fF]+(\'.+?\'\))",inputString):

    inputString = charReplace(inputString)

print "\n%s" % inputString