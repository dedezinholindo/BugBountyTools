#!/bin/bash

############################################subdomain enumaration########################################################
echo "Iniciando full recon " | notify;
for i in $(cat $1); do
	shuffledns -d $i -w /root/lists/subrecon.txt -r /root/lists/dns-resolvers.txt -o subsshuffledns;
	assetfinder -subs-only $i | anew subsasset;
	subfinder -d $i | anew subssubf;
	curl -s "https://crt.sh/?q=%25.$i&output=json" | jq -r '.[].name_value' | sed 's/\*\.//g' | anew subscrt;
	findomain -t $i -q | anew subsf;
	python3 /root/tools/Sublist3r/sublist3r.py -d $i -o subslist3r;
	curl -s "https://rapiddns.io/subdomain/$i?full=1#result" | grep "<td><a" | cut -d '"' -f 2 | grep http | cut -d '/' -f3 | sed 's/#results//g' | anew subsrapid;
	curl -s https://dns.bufferover.run/dns?q=.$i |jq -r .FDNS_A[]|cut -d',' -f2| anew subsbuffer;
	curl -s "https://riddler.io/search/exportcsv?q=pld:$i" | grep -Po "(([\w.-]*)\.([\w]*)\.([A-z]))\w+" | anew subsriddle; 
	curl -s "http://web.archive.org/cdx/search/cdx?url=*.$i/*&output=text&fl=original&collapse=urlkey" | sed -e 's_https*://__' -e "s/\/.*//" | anew subsarchive;
	curl -s "https://jldc.me/anubis/subdomains/$i" | grep -Po "((http|https):\/\/)?(([\w.-]*)\.([\w]*)\.([A-z]))\w+" | anew subsjldc;
	curl --silent https://sonar.omnisint.io/subdomains/$i | grep -oE "[a-zA-Z0-9._-]+\.$i" | anew subssonar;
	chaos -d $i | anew subschaos;
	python3 /root/tools/github-search/github-subdomains.py -t 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 -d $i >> tmp; cat tmp | grep -v ">" >> subsgit;
	cat subs* | anew tudo;
	rm -rf subs* tmp;
done
echo "Ta acabando recon... amass e jsub " | notify;
amass enum -df $1 -active -p 443,8080,80,81,8081,8443 -config /root/.config/amass/config.ini -o subsamass;
cat subsamass tudo | anew tot;
jsubfinder -f tot | anew j200;
cat j200 tot | anew total;
rm tudo subsamass j200 tot;

########################################################################################################################
#############################################validando subdominios######################################################

echo "Validando subdominios " | notify;
cat total | httpx -threads 200 -random-agent -o 300;
cat 200 | anew total200; rm 200;
cat total200 | sed 's/$/\//' | anew total200Barra;
cat total | httprobe -p http:81 -p http:3000 -p https:3000 -p http:3001 -p https:3001 -p http:8000 -p http:8080 -p https:8443 -p https:10000 -p http:9000 -p https:9443 -c 300 | anew total200;


########################################################################################################################
##################################################nuclei#################################################################

echo "Iniciando nuclei, bonitao " | notify;
nuclei -l total200 -t /root/tools/BugBountyTools/nuclei-template/ -severity low,medium,high,severe,critical -o nuclei | notify;
echo "Acabou o nuclei " | notify;
