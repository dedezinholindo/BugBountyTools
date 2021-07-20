#!/usr/bin/python

import urllib.parse
import re
import http
import sys
from subprocess import check_output
import threading


def applyXSStrike(url, reflectedPayload):
    cmd = f"python3 /root/tools/XSStrike/xsstrike.py -u '{url}' --skip-dom -f {reflectedPayload} --file-log-level INFO --log-file output.log; cat output.log | grep -i 'info' | cut -d ']' -f2 | anew p; rm output.log;"
    modUrl = check_output(cmd, shell=True, executable='/bin/bash')
    payScape = urllib.parse.unquote(modUrl.decode().strip())
    return payScape

def reflectedXSS(url, payload):
    resultCommand = applyXSStrike(url, payload)
    

def urls(archive, reflectedPayload):
    threads = []
    with open(archive, 'r') as urlsFile:
        for url in urlsFile:
            t = threading.Thread(target=reflectedXSS, args=(url, reflectedPayload,))
            threads.append(t)
            t.start()
        for thread in threads:
            thread.join()

def main():
    archive, reflectedPayload = sys.argv[1:]
    urls(archive, reflectedPayload)
    
    
    
main()
