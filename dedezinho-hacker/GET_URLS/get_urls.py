import subprocess, concurrent.futures


def waybackurl(arquivo):
    p = subprocess.Popen(f"cat {arquivo} | waybackurls | anew wayback", shell=True)
    p.communicate()
    
def gauplus(arquivo):
    p = subprocess.Popen(f"cat {arquivo} | gauplus -t 100 --random-agent -b jpg,png,svg,jpeg,gif | anew gaup", shell=True)
    p.communicate()
    
def paramspider(domains):
    p = subprocess.Popen(f"xargs -a {domains} -I@ bash -c 'python3 /root/tools/ParamSpider/paramspider.py -d @ --exclude jpg,png,svg,jpeg,gif --output param'", shell=True)
    p.communicate()
    
def get_all(domains, arquivo):
    results = []
    with concurrent.futures.ThreadPoolExecutor() as executor:
        with open(domains, "r") as arquivo:
            results.append(executor.submit(waybackurl, arquivo))
            results.append(executor.submit(gauplus, arquivo))
            results.append(executor.submit(paramspider, domains))
            for j in results:
                j.result()
