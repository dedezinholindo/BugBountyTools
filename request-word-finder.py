import re
import sys
from subprocess import check_output


def get_response(url):
    cmd = f"curl -kL '{url}' 2>/dev/null"
    response = check_output(cmd, shell=True, executable='/bin/bash')
    return response.decode()

def search(text, word):
    return re.search(word, text, re.IGNORECASE)

def find_match(url, word):
    text = get_response(url)
    if search(text, word):
        print(f"Found the word {word} at {url}")
    
def main():
    url, word = sys.argv[1:]
    find_match(url, word)

main()