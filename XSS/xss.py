#!/usr/bin/python

import urllib.parse
import re
import http
import sys
from subprocess import check_output
from selenium import webdriver
from selenium.common.exceptions import NoAlertPresentException
import threading


http.client.HTTPConnection.debuglevel = 0 #nao derrubar o seu ip para muitas requisicoes

def applyPayload(url, payload):
    payScape = payload.strip().replace("'", "dede").replace('"', "dezao")
    cmd = f"echo {url.strip()}| qsreplace '{payScape}'"
    modUrl = check_output(cmd, shell=True, executable='/bin/bash')
    payScape = urllib.parse.unquote(modUrl.decode().strip())
    payScape = payScape.replace("dede", "'").replace('dezao"', '"')
    return payScape

def testAlert(payScape):
    key = False
    try:
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        driver = webdriver.Chrome(options=options, executable_path=r'/usr/bin/chromedriver')
        driver.get(f"{payScape}")
        key = False
        try:
            alert = driver.switch_to.alert
            alert.text
            key = True
        except:
            key = False
        driver.quit()
    except:
        pass
    return key
    
def reflectedXSS(url, payload):
    # comando para aplicar payload
    payScape = applyPayload(url, payload)
    #testar alert
    key = testAlert(payScape)
    if key:
        print(f"Found XSS at {payScape}")
                
def initSearch(url, payload):
    threads = []
    with open(payload, 'r') as payloadFile: 
        for payload in payloadFile:
            t = threading.Thread(target=reflectedXSS, args=(url, payload,))
            threads.append(t)
            t.start()
        for thread in threads:
            thread.join()
                
def urls(archive, reflectedPayload):
    with open(archive, 'r') as urlsFile:
        for url in urlsFile:
            initSearch(url, reflectedPayload)
            
def main():
    archive, reflectedPayload = sys.argv[1:]
    urls(archive, reflectedPayload)
    
    
main()