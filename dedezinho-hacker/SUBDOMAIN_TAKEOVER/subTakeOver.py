#!/usr/bin/python

import grequests
import re
import sys

    
def get_urls(archive):
    urls = []
    with open(archive, 'r') as subFile:
        for url in subFile:
            urls.append(url.strip())
    return urls    
    
def reqTakeOver(req, str1, str2, str3):
    s1 = re.search(str1, req.text, re.IGNORECASE)
    s2 = re.search(str2, req.text, re.IGNORECASE)
    s3 = re.search(str3, req.text, re.IGNORECASE)
    return (s1 and s2 and s3)

def get_data(urls):
    reqs = [grequests.get(link) for link in urls]
    resp = grequests.map(reqs)
    return resp

def takeOver(resp):
   for i in resp:
       if ((i != None) and (i.status_code == 404)):
            if(reqTakeOver(i, "nosuchbucket", "not exist", "bucketname")):
                print(f"Found possible Subdomain TakeOver at {i.url}")

def main():
    archive = sys.argv[1]
    urls = get_urls(archive)
    resp = get_data(urls)
    takeOver(resp)
        
main()