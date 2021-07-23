#!/usr/bin/python3

import grequests
import re
import http
import sys
import threading
import requests


http.client.HTTPConnection.debuglevel = 0 #nao derrubar o seu ip para muitas requisicoes
#headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

threads = threading.Semaphore(10)

def get_payloads(payloadFile):
    pay = []
    with open(payloadFile, 'r') as payloads: 
        for payload in payloads:
            pay.append(payload.strip())
    return pay

def get_urls_with_payloads(url, payloads):
    urls = []
    for payload in payloads:
        url = f"{url.strip() + payload}"
        urls.append(url.strip())
    return urls   

def opr_lfi(vuln, u, payloads):
    urls = get_urls_with_payloads(u, payloads)
    s = requests.Session()
    for url in urls:
        resp = s.get(url, verify=True)
        if (resp != None):
            print(resp.url)
            if (vuln == "lfi"):
                key = re.search('root:x', resp.text, re.IGNORECASE)
                if key:
                    print(f"Found possible LFI at {resp.url}")
            elif (vuln == "opr"):
                key = re.search('This domain is for use in illustrative examples in documents.', resp.text, re.IGNORECASE)
                if key:
                    print(f"Found Open Redirect at {resp.url}")
            
"""def urls(vuln, archive, redirectPayload):
    threads = []
    with open(archive, 'r') as urlsFile:
        for url in urlsFile:
            t = threading.Thread(target=opr_lfi, args=(vuln, url, redirectPayload,))
            threads.append(t)
            t.start()
        for thread in threads:
            thread.join() """
            
def urls(vuln, archive, payloads):
    threads = []
    with open(archive, 'r') as urlsFile:
        for url in urlsFile:
            opr_lfi(vuln, url, payloads)
            
def main():
    vuln, archive, payloadFile = sys.argv[1:]
    payloads = get_payloads(payloadFile)
    urls(vuln, archive, payloads)
    
    
main()