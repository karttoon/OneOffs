#!/usr/bin/env python
import urllib, sys, argparse

__author__  = "Jeff White [karttoon] @noottrak"
__email__   = "karttoon@gmail.com"
__version__ = "1.0.0"
__date__    = "10APR2017"

def main():
    parser = argparse.ArgumentParser(description="Percent encode or decode strings for URLs.")
    parser.add_argument("-e", "--encode", help="Percent encode.", metavar="<string>")
    parser.add_argument("-d", "--decode", help="Percent decode", metavar="<string>")
    args = parser.parse_args()

    if args.encode:
        print urllib.quote(args.encode, safe='')

    if args.decode:
        print urllib.unquote(args.decode)

if __name__ == '__main__':
    main()
