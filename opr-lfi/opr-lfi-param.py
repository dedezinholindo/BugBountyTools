#!/usr/bin/python

import requests
import re
import http
import sys
from subprocess import check_output
import urllib
import threading


http.client.HTTPConnection.debuglevel = 0 #nao derrubar o seu ip para muitas requisicoes
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}


def applyPayload(url, payload):
    payScape = payload.strip().replace("'", "dede").replace('"', "dezao")
    cmd = f"echo '{url.strip()}'| qsreplace '{payScape}'"
    modUrl = check_output(cmd, shell=True, executable='/bin/bash')
    payScape = urllib.parse.unquote(modUrl.decode().strip())
    payScape = payScape.replace("dede", "'").replace('dezao', '"')
    return payScape

def opr_lfi(vuln, url, payload):
    try:
        s = requests.Session()
        payScape = applyPayload(url, payload)
        req = s.get(payScape, verify=True, headers=headers)
        if (vuln == "lfi"):
            key = re.search('root:x', req.text, re.IGNORECASE)
            if key:
                print(f"Found possible LFI at {payScape}")
        elif (vuln == "opr"):
            key = re.search('This domain is for use in illustrative examples in documents.', req.text)
            if key:
                print(f"Found Open Redirect at {payScape}")
    except:
        pass
   
def initSearch(vuln, url, payloadList):
    threads = []
    with open(payloadList, 'r') as payloadFile: 
        for payload in payloadFile:
            t = threading.Thread(target=opr_lfi, args=(vuln, url, payload,))
            threads.append(t)
            t.start()
        for thread in threads:
            thread.join()   
   
def urls(vuln, archive, payloadList):                
    with open(archive, 'r') as urlsFile:
        for url in urlsFile:
            initSearch(vuln, url, payloadList)
        
def main():
    vuln, archive, payloadList = sys.argv[1:]
    urls(vuln, archive, payloadList)
 
    
main()