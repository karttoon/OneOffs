#!/usr/bin/env python
import sys, pefile

__author__  = "Jeff White [karttoon]"
__email__   = "karttoon@gmail.com"
__version__ = "1.0.0"
__date__    = "10APR2017"

pe = pefile.PE(sys.argv[1])
try:
	print "%s,%s" % (sys.argv[1],pe.FileInfo[0].StringTable[0].entries.items())
except:
	pass
