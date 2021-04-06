#!/usr/bin/env python
from datetime import datetime

__author__  = "Jeff White [karttoon] @noottrak"
__email__   = "karttoon@gmail.com"
__version__ = "1.0.0"
__date__    = "06APR2021"

# Template designed and provided by Netspooky
# https://gist.github.com/netspooky/882c8dc1f082c160157da2d73ac1f3d2

numArt = {
    "t1": "▀█ ",
    "m1": " █ ",
    "b1": "▀▀▀",
    "t2": "▀▀█",
    "m2": "█▀▀",
    "b2": "▀▀▀",
    "t3": "▀▀█",
    "m3": "▀▀█",
    "b3": "▀▀▀",
    "t4": "█ █",
    "m4": "▀▀█",
    "b4": "  ▀",
    "t5": "█▀▀",
    "m5": "▀▀█",
    "b5": "▀▀▀",
    "t6": "█▀▀",
    "m6": "█▀█",
    "b6": "▀▀▀",
    "t7": "▀▀█",
    "m7": "  █",
    "b7": "  ▀",
    "t8": "█▀█",
    "m8": "█▀█",
    "b8": "▀▀▀",
    "t9": "█▀█",
    "m9": "▀▀█",
    "b9": "▀▀▀",
    "t0": "█▀█",
    "m0": "█ █",
    "b0": "▀▀▀",
}

def printDate(dateStr, day):

    for i in ["t", "m", "b"]:
        rowStr = str()
        for x in dateStr:
            rowStr += "%s " % (numArt["%s%s" % (i,x)])
        print(rowStr + "────────────────────────────────────────────────")

    print("%s %s %s" % ("─" * (84 - len(day) - 8), day, "─" * 2))

    return

def printBody(dateStr):

    print("""
⚪ This is a task I have to do

⚫ This is a task I have completed

✖ Not important / disregard

☢ Important Info / PROTIP ☢

► Some bullet points...
  - These also work
  
□ Incomplete subtask
■ Completed subtask

○ This is an empty circle
● This is a filled circle

[ Dividers ]

────────────────────────────────────────────────────────────────────────────────
────────────────────────────────────────────────────────────────────────────//──
■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■

►►► %s ◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄    
    """ % dateStr)

    return


def main():

    now = datetime.now()

    dateStr = now.strftime("%Y%m%d")
    day = now.strftime("%A")

    printDate(dateStr, day)
    printBody(dateStr)

    return


if __name__ == '__main__':
    main()
