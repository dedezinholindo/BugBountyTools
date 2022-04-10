from re import sub
import subprocess, concurrent.futures


def search_domains(func, domains):
	for i in domains.readlines():
		i = i.strip().rstrip('\n')
		func(i)
  
def shuffledns(domain):
	p = subprocess.Popen(f"shuffledns -d {domain} /root/lists/subrecon.txt -r /root/lists/dns-resolvers.txt -o subsshuffledns", shell=True)
	p.communicate()

def assetfinder(domain):
	p = subprocess.Popen(f"assetfinder -subs-only {domain} | anew subsasset", shell=True)
	p.communicate()
    
def subfinders(domain):
	p = subprocess.Popen(f"subfinder -d {domain} | anew subssubf", shell=True)
	p.communicate()
    
def curls_domains(domain):
	comando = f"""
	curl -s 'https://crt.sh/?q=%25.{domain}&output=json' | jq -r '.[].name_value' | sed 's/\*\.//g' | anew subscrt;
	curl -s "https://rapiddns.io/subdomain/{domain}?full=1#result" | grep "<td><a" | cut -d '"' -f 2 | grep http | cut -d '/' -f3 | sed 's/#results//g' | anew subsrapid;
	curl -s https://dns.bufferover.run/dns?q=.$i |jq -r .FDNS_A[]|cut -d',' -f2| anew subsbuffer;
	curl -s "https://riddler.io/search/exportcsv?q=pld:{domain}" | grep -Po "(([\w.-]*)\.([\w]*)\.([A-z]))\w+" | anew subsriddle; 
	curl -s "http://web.archive.org/cdx/search/cdx?url=*.{domain}/*&output=text&fl=original&collapse=urlkey" | sed -e 's_https*://__' -e "s/\/.*//" | anew subsarchive;
	curl -s "https://jldc.me/anubis/subdomains/{domain}" | grep -Po "((http|https):\/\/)?(([\w.-]*)\.([\w]*)\.([A-z]))\w+" | anew subsjldc;
	curl --silent https://sonar.omnisint.io/subdomains/{domain} | grep -oE "[a-zA-Z0-9._-]+\.$i" | anew subssonar;"""
	p = subprocess.Popen(comando, shell=True)
	p.communicate()
    
def findomain(domain):
	p = subprocess.Popen(f"findomain -t {domain} -q | anew subsf", shell=True)
	p.communicate()
    
def sublist3r(domain):
	p = subprocess.Popen(f"python3 /root/tools/Sublist3r/sublist3r.py -d {domain} -o subslist3r", shell=True)
	p.communicate()
    
def chaos(domain):
	p = subprocess.Popen(f"chaos -d {domain} | anew subschaos", shell=True)
	p.communicate()
 
def github(domain):
	p = subprocess.Popen(f"python3 /root/tools/github-search/github-subdomains.py -t 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 -d {domain} >> tmp; cat tmp | grep -v '>' >> subsgit", shell=True)
	p.communicate()

def amass(domains):
	p = subprocess.Popen(f"amass enum -df {domains} -active -p 443,8080,80,81,8081,8443 -config /root/.config/amass/config.ini -o subsamass", shell=True)
	p.communicate()
 
def jsubfinder(arquivo):
    subprocess.Popen(f"jsubfinder -f {arquivo} | anew j200", shell=True)

def finalizar():
    subprocess.Popen(f"cat subs* | anew tudo; rm -rf subs* tmp;", shell=True)
    
    
def get_subdomain_collect(subdominios):
	results = []
	with concurrent.futures.ThreadPoolExecutor() as executor:
		with open(subdominios, "r") as arquivo:
			results.append(executor.submit(search_domains, assetfinder, arquivo))
			results.append(executor.submit(search_domains, shuffledns, arquivo))
			results.append(executor.submit(search_domains, subfinders, arquivo))
			results.append(executor.submit(search_domains, curls_domains, arquivo))
			results.append(executor.submit(search_domains, findomain, arquivo))
			results.append(executor.submit(search_domains, sublist3r, arquivo))
			results.append(executor.submit(search_domains, chaos, arquivo))
			results.append(executor.submit(search_domains, github, arquivo))
			for j in results:
				j.result()
	subprocess.Popen(f"echo 'Ta acabando recon... amass e jsub' | notify;", shell=True)
	amass(subdominios)
	finalizar()
	subprocess.Popen(f"cat subsamass tudo | anew tot", shell=True)
	jsubfinder("tot")
	subprocess.Popen(f"cat j200 tot | anew total;rm tudo subsamass j200 tot;", shell=True)
	
def validate_subdomains():
	subprocess.Popen(f"echo 'Validando subdominios' | notify", shell=True)
	p = subprocess.Popen(f"""
                cat total | httpx -threads 200 -random-agent -o 200;
				cat 200 | anew total200; rm 200;
				cat total | httprobe -p http:81 -p http:3000 -p https:3000 -p http:3001 -p https:3001 -p http:8000 -p http:8080 -p https:8443 -p https:10000 -p http:9000 -p https:9443 -c 50 | anew total200;""")
	p.communicate()

def main(subdominios):
    subprocess.Popen("echo Iniciando coleta de subdoomínios | notify", shell=True)
    get_subdomain_collect(subdominios)
    validate_subdomains()
    subprocess.Popen("echo Coleta e verificação de Subdomínios finalizada | notify", shell=True)
    
