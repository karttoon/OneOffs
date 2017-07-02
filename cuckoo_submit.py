#!/usr/bin/env python
import requests, json, sys, argparse

__author__  = "Jeff White [karttoon] @noottrak"
__email__   = "karttoon@gmail.com"
__version__ = "1.0.0"
__date__    = "31JAN2017"


def submit_file(args):

    SERVER_ADDR = "https://"

    if args.creds:
        SERVER_ADDR += "%s@" % args.creds

    SERVER_ADDR += "%s/api/tasks/create/file/" % args.server

    FILE_NAME = args.file

    files = dict(
        file=open(FILE_NAME, "rb"),
        filename=FILE_NAME
    )

    data = dict(
        priority=1
    )

    response = requests.post(SERVER_ADDR, files=files, data=data, verify=False)

    #print response.content

    json = response.json()
    task_ids = json["task_ids"]

    print "[+] Submitted %s : ID %s" % (FILE_NAME, task_ids)

def read_report(args):

    SERVER_ADDR = "https://"

    if args.creds:
        SERVER_ADDR += "%s@" % args.creds

    SERVER_ADDR += "%s/api/tasks/get/iocs/%s/" % (args.server, args.id)

    response = requests.get(SERVER_ADDR, verify=False)

    if args.write:
        FILE_NAME = "%s.report" % args.id
        FILE_HANDLE = open(FILE_NAME, "w")
        FILE_HANDLE.write(response.content)

    else:
        print response.content

def main():

    parser = argparse.ArgumentParser(description="Submit files and get reports from Cuckoo")
    parser.add_argument("-c", "--creds", help="Credentials used for Cuckoo authentication 'name:password'")
    parser.add_argument("-f", "--file", help="Specify file for submission.", metavar="<file_name>")
    parser.add_argument("-s", "--server", help="Server to submit to.", metavar="<hostname>", required=True)
    parser.add_argument("-i", "--id", help="Read task report ID", metavar="<number>", type=int)
    parser.add_argument("-w", "--write", help="Write task report output to a file", action="store_true")
    args = parser.parse_args()

    if args.file and args.id:
        print "[!] Error - Cannot read and submit at same time"
    elif args.file:
        submit_file(args)
    elif args.id:
        read_report(args)
    else:
        print "[!] No option selected"
        sys.exit(1)

if __name__ == '__main__':
    main()
