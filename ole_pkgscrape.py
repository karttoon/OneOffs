#!/usr/bin/env python
import re, sys

__author__  = "Jeff White [karttoon] @noottrak"
__email__   = "karttoon@gmail.com"
__version__ = "1.0.0"
__date__    = "27JUL2018"

with open(sys.argv[1], "r") as fh:
    file = fh.read()

# Validate OLE Package exists
oleCheck = re.search("\x4F\x4C\x45\x20\x50\x61\x63\x6B\x61\x67\x65\x00\x00\x00\x00\x00", file)

if oleCheck:

    olePackages = re.findall("\x00\x02\x00[\x01-\x99]+\x00[\x01-\x99]+\x00\x00\x00\x03\x00[\x01-\x99]\x00\x00\x00[\x01-\x99]+", file[oleCheck.start():])
    for entry in olePackages:
        # OLE Package Anchor
        entry = re.escape(entry)
        fileInfo = re.search(entry, file)
        print "[+] Found OLE Package:" 

        # Embedded File Name
        fileName = re.search("\x00\x02\x00[\x01-\x99]+\x00", fileInfo.group(0)).group(0)[3:-1]
        print "\t%-20s: %s" % ("Embedded File Name", fileName)

        # Original File Path
        filePath = re.search("\x00[\x01-\x99]+\x00\x00\x00\x03", fileInfo.group(0)).group(0)[1:-4]
        print "\t%-20s: %s" % ("Original File Path", filePath)

        # %TEMP% Save Path
        tempPath = re.search("\x00\x00\x00\x03\x00[\x01-\x99]\x00\x00\x00[\x01-\x99]+", fileInfo.group(0)).group(0)[9:]
        print "\t%-20s: %s" % ("%TEMP% Save Path", tempPath)

        # WIDE Vars (removes BOM as well)
        nameWide = fileName.encode('utf-16')[2:-1]
        pathWide = filePath.encode('utf-16')[2:-1]
        tempWide = tempPath.encode('utf-16')[2:-1]

        # Content start/stop offsets
        endAnchor = "\x00\x00\x00" + re.escape(tempWide)
        strPos = fileInfo.end() + 5
        endPos = re.search(endAnchor, file).start() - 1
        print "\t%-20s: %s" % ("Length of Object", endPos - strPos)

        # Save File
        fh = open(fileName + "_extracted", "w")
        fh.write(file[strPos:endPos])
        fh.close()
        print "[!] Saved file %s" % (fileName + "_extracted")
