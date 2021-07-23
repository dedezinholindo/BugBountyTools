import grequests
import re

def get_urls():
    urls = []
    for x in range(1):
        urls.append(f'http://pisuite.sensedia.com')
    return urls

def get_data(urls):
    reqs = [grequests.get(link) for link in urls]
    resp = grequests.map(reqs)
    return resp


def parse_data(resp):
   for i in resp:
       if (i != None):
            #print((i.text).strip())
            print(i.status_code)

def main():
    urls = get_urls()
    resp = get_data(urls)
    parse_data(resp)    
main()