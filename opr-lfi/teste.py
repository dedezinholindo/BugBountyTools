#!/usr/bin/python3

import asyncio
import aiohttp
import re
import http
import sys


result = []

def get_urls(archive):
    urls = []
    with open(archive, 'r') as urlsFile:
        for url in urlsFile:
            urls.append(url.strip())
    return urls

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

def get_tasks(session, urls):
    tasks = []
    for url in urls:
        tasks.append(asyncio.create_task(session.get(url, ssl=False)))
    return tasks

async def get_symbols(urls):
    #results = []
    async with aiohttp.ClientSession() as session:
        tasks = get_tasks(session, urls)
        responses = await asyncio.gather(*tasks)
        for response in responses:
            result.append(await response.json())

def opr_lfi(vuln, url, redirectPayload):
    urls = get_urls_with_payloads(url, redirectPayload)
    asyncio.run(get_symbols(urls))
    """for i in resp:
        if (i != None):
            print(i.url)
            if (vuln == "lfi"):
                key = re.search('root:x', i.text, re.IGNORECASE)
                if key:
                    print(f"Found possible LFI at {i.url}")
            elif (vuln == "opr"):
                key = re.search('This domain is for use in illustrative examples in documents.', i.text, re.IGNORECASE)
                if key:
                    print(f"Found Open Redirect at {i.url}")"""
                    
def search(vuln, urls, payloads):
    for url in urls:
        opr_lfi(vuln, url, payloads)

def main():
    vuln, archive, payloadFile = sys.argv[1:]
    urls = get_urls(archive)
    payloads = get_payloads(payloadFile)
    search(vuln, urls, payloads)
    
main()