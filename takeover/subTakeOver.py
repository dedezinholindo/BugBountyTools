#!/usr/bin/python

import requests
import re
import http
import sys
import urllib
import threading
import subprocess
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

http.client.HTTPConnection.debuglevel = 0 #nao derrubar o seu ip para muitas requisicoes
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

    
def reqTakeOver(req, str1, str2, str3):
    s1 = re.search(str1, req.text, re.IGNORECASE)
    s2 = re.search(str2, req.text, re.IGNORECASE)
    s3 = re.search(str3, req.text, re.IGNORECASE)
    if (s1 and s2 and s3):
        return True
    return False

def testRequest(subdomain):
    try:
        s = requests.Session()
        req = s.get(subdomain, verify=False, timeout=10, headers=headers)
        tko = reqTakeOver(req, "nosuchbucket", "not exist", "bucketname") 
        if (tko):
            return True
        return False
    except requests.exceptions.ConnectTimeout:
        return False

def takeover(subdomain):
    tReq = testRequest(subdomain)
    if (tReq):
        print(f"Found possible Subdomain TakeOver at {subdomain}")
   
def initSearch(archive):
    threads = []
    with open(archive, 'r') as subsFile:
        for sub in subsFile:
            t = threading.Thread(target=takeover, args=(sub.strip(),))
            threads.append(t)
            t.start()
        for thread in threads:
            thread.join()   
        
def main():
    archive = sys.argv[1]
    initSearch(archive)
 
    
main()