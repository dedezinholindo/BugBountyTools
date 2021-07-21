#!/usr/bin/python3

import requests
import re
import http
import sys
import threading


http.client.HTTPConnection.debuglevel = 0 #nao derrubar o seu ip para muitas requisicoes
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

def opr_lfi(vuln, url, payload):
    try:
        s = requests.Session()
        newUrl = f"{url.strip() + payload.strip()}"
        req = s.get(newUrl, verify=True, headers=headers)
        if (vuln == "lfi"):
            key = re.search('root:x', req.text, re.IGNORECASE)
            if key:
                print(f"Found possible LFI at {newUrl}")
        elif (vuln == "opr"):
            key = re.search('This domain is for use in illustrative examples in documents.', req.text)
            if key:
                print(f"Found Open Redirect at {newUrl}")
    except:
        pass  

def initSearch(vuln, url, redirectPayload):
    threads = []
    with open(redirectPayload, 'r') as payloadFile: 
        for payload in payloadFile:
            t = threading.Thread(target=opr_lfi, args=(vuln, url, payload,))
            threads.append(t)
            t.start()
        for thread in threads:
            thread.join()

def urls(vuln, archive, redirectPayload):
    with open(archive, 'r') as urlsFile:
        for url in urlsFile:
            initSearch(vuln, url, redirectPayload)
  
      
def main():
    vuln, archive, redirectPayload = sys.argv[1:]
    urls(vuln, archive, redirectPayload)
    
    
main()