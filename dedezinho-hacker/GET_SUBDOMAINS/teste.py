import subprocess, concurrent.futures
from time import sleep


def f1():
    print("oi")
    sleep(10)
    
    
def f2():
    print("tachu")


def main():
    with concurrent.futures.ThreadPoolExecutor() as executor:
        for i in range(2):
            r= executor.submit(f1)
            s= executor.submit(f2)
            oi = r.result()
            
        
main()