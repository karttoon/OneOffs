#!/usr/bin/env python
import re, sys, hashlib, binascii, argparse

__author__  = "Jeff White [karttoon] @noottrak"
__email__   = "karttoon@gmail.com"
__version__ = "1.0.1"
__date__    = "24APR2018"

def xorDans(value):
    return ''.join(chr(ord(x) ^ ord(y)) for x, y in zip(value, "DanS"))

def getContent(file):
    fh = open(file, "r")
    content = ""
    for i in fh:
        content += i
    fh.close()
    return content

def xorDec(rhData, xorKey):
    # Decode every four bytes with XOR key
    clearData = ""
    for i in range(0, len(rhData)):
        clearData += chr(ord(rhData[i]) ^ ord(xorKey[i % len(xorKey)]))
    return clearData

def genFirst(content, richStart):
    # Clear out the e_lfanew field in the DOS header - this field gets set *after* the Rich Header is inserted
    content = content[0:0x3C] + "\x00\x00\x00\x00" + content[0x40:]
    # For some reason they start the sum with the offset of the Rich Header (usually 0x80)
    firstSum = richStart
    for i in range(richStart):
        firstSum += checkSum(ord(content[i]), i)
    return firstSum

def checkSum(value, usesValue):
    # Shift left by usesValue (count) and grab LOW byte
    # Keep 32 bits and then OR by same idKey OR idValue
    # Shift right by usesValue (count) and grab LOW byte
    return (value << (usesValue & 0x1F)) & 0xFFFFFFFF | value >> (0x20 - (usesValue & 0x1F))

def genYara(args, yaraRules):
    print """
[+] Yara Rule

import \"pe\""""
    if args.cleardata or args.all:
        print "import \"hash\""

    print """
rule richheader {
    meta:
        comment = \"%s\"
    condition:""" % (args.file)

    print "        %s" % ("\n        and ".join(yaraRules))
    print "}\n"
    return

def main():

    parser = argparse.ArgumentParser(description="Generate a YARA rule from Rich Header information found in PE.")
    parser.add_argument("-x", "--xorkey", help="Add XOR Key to YARA rule", action="store_true")
    parser.add_argument("-t", "--toolid", help="Add Tool ID to YARA rule", action="store_true")
    parser.add_argument("-c", "--cleardata", help="Add XOR'd clear data to YARA rule", action="store_true")
    parser.add_argument("-a", "--all", help="Add all fields to YARA rule (overkill)", action="store_true")
    parser.add_argument("-d", "--details", help="Print details from parsing Rich Header", action="store_true")
    parser.add_argument("-f", "--file", help="Specify file to parse", metavar="<filename>", required=True)
    args = parser.parse_args()

    if not args.xorkey and not args.toolid and not args.cleardata and not args.all:
        args.all = True

    content = getContent(args.file)

    yaraRules = []

    # Check for Rich Header structure and location
    try:
        # XOR Key follows "Rich" anchor
        xorKey = re.search("\x52\x69\x63\x68....\x00", content).group(0)[4:8]
        # Determine XOR encoded "DanS" anchor
        dansAnchor = xorDans(xorKey)
        # Grab offsets for entire encoded blob
        richStart = re.search(re.escape(dansAnchor), content).start(0)
        richEnd = re.search("Rich" + re.escape(xorKey), content).start(0)
        # Basic check to insure correct location for start
        if richStart < richEnd:
            rhData = content[richStart:richEnd]
        else:
            raise
    except:
        print "Unable to find Rich Header structure in file %s" % (sys.argv[1])
        sys.exit(1)

    firstSum = genFirst(content, richStart)

    clearData = xorDec(rhData, xorKey)

    # Skip "DanS" anchor and 3 8-byte pads to arrive at first array entry
    decData = clearData[16:]
    counter = 1

    if args.details:
        print "\n[+] Parsed Rich Header\n"
        print "Offset | Data        // Meaning"
        print "%s" % ("-" * 50)

    secondSum = 0

    # Determine ID Key, Value, and Usage for each entry
    for i in range(0,len(decData),8):

        value = decData[i:i+8]
        idKey = int(value[0:4][::-1][0:2].encode("hex"), 16)
        idValue = int(value[0:4][::-1][2:4].encode("hex"), 16)
        usesValue = int(value[4:][::-1].encode("hex"), 16)

        # Flip endian on idKey and OR with idValue
        secondSum += checkSum((idKey << 16 | idValue), usesValue)

        if args.details:
            print "0x%04X | 0x%08X  // entry %s" % (richStart + 16 + i,
                                                    int(value[0:4][::-1].encode("hex"), 16),
                                                    counter)
            print "0x%04X | 0x%08X  // id%s=%s, uses=%s" % (richStart + 16 + 4 + i,
                                                            int(value[4:][::-1].encode("hex"), 16),
                                                            idKey,
                                                            idValue,
                                                            usesValue)
        if args.toolid or args.all:
            yaraRules.append("pe.rich_signature.toolid(%s,%s)" % (idKey, idValue))

        counter += 1

    finalSum = binascii.unhexlify(hex((firstSum + secondSum) & 0xFFFFFFFF)[2:])
    sumMatch = True

    if finalSum != xorKey[::-1]:
        sumMatch = False
        print "Extracted XOR Key differs from Generated XOR Key!"
        print binascii.hexlify(finalSum), binascii.hexlify(xorKey)

    if args.xorkey or args.all:
        yaraRules.append("pe.rich_signature.key == 0x%s" % (binascii.hexlify(xorKey[::-1])))
    if args.cleardata or args.all:
        yaraRules.append("hash.sha256(pe.rich_signature.clear_data) == \"%s\"" % (hashlib.sha256(clearData).hexdigest()))

    if args.details:
        print "\n[+] Details\n"
        print "File:            %s" % (args.file)
        print "Clear Data:      %s" % (binascii.hexlify(clearData).upper())
        print "Clear Data Hash: %s" % (hashlib.sha256(clearData).hexdigest().upper())
        print "XOR Key:         0x%s" % (binascii.hexlify(xorKey[::-1]).upper())
        print "Checksum Match:  %s\n" % sumMatch

    if (args.xorkey or args.toolid or args.cleardata or args.all) and not args.details:
        genYara(args, yaraRules)

    return

if __name__ == '__main__':
    main()
