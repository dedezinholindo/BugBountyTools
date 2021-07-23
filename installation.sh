#!/bin/bash

#go por wget
apt-get update;
apt-get upgrade -y;
apt-get install python3-pip -y;
apt install snapd -y;
apt-get install jq -y;
apt-get install git -y;
apt-get install host -y;
go mod init puppy;
apt-get install wget -y;
apt-get install tmux -y; 
go get -u github.com/tomnomnom/anew
go get -u github.com/hiddengearz/jsubfinder
GO111MODULE=on go get -v github.com/projectdiscovery/shuffledns/cmd/shuffledns;
pip3 install faster_than_requests;
go get -u github.com/tomnomnom/assetfinder;
GO111MODULE=on go get -v github.com/projectdiscovery/subfinder/v2/cmd/subfinder;
go get github.com/003random/getJS;
wget https://github.com/findomain/findomain/releases/latest/download/findomain-linux;
chmod +x findomain-linux;
mv findomain-linux findomain; mv findomain /usr/bin;
mkdir tools;
cd ~/lists; wget https://raw.githubusercontent.com/s0md3v/Arjun/master/arjun/db/params.txt
cd ~/tools; git clone https://github.com/s0md3v/XSStrike.git; pip3 install -r XSStrike/requirements.txt 
cd ~/tools; git clone https://github.com/aboul3la/Sublist3r.git; pip3 install -r Sublist3r/requirements.txt
cd ~/tools; git clone https://github.com/gwen001/github-search.git;
cd ~/tools; git clone https://github.com/m4ll0k/takeover.git;
cd ~/tools; git clone https://github.com/devanshbatham/ParamSpider.git; pip3 install -r ParamSpider/requirements.txt;
cd ~/tools; git clone https://github.com/GerbenJavado/LinkFinder.git; pip3 install -r LinkFinder/requirements.txt;
cd ~/tools; git clone https://github.com/m4ll0k/SecretFinder.git; pip3 install -r SecretFinder/requirements.txt;
cd ~/tools; git clone https://github.com/KingOfBugbounty/Bug-Bounty-Toolz.git
cd ~/tools; git clone https://github.com/dedezinholindo/BugBountyTools.git;
cd ~; git clone https://github.com/projectdiscovery/nuclei-templates.git;
cd ~/tools; git clone https://github.com/0x240x23elu/JSScanner.git; pip3 install -r JSScanner/requirements.txt
cd ~/tools; git clone https://github.com/s0md3v/Arjun.git; cd Arjun; python3 setup.py install;
cd ~/tools; git clone https://github.com/blechschmidt/massdns.git; cd massdns; make; mv bin/massdns /usr/bin/;
GO111MODULE=on go get -v github.com/projectdiscovery/chaos-client/cmd/chaos;
GO111MODULE=on go get -v github.com/projectdiscovery/httpx/cmd/httpx;
GO111MODULE=on go get -u -v github.com/lc/subjs;
go get -v github.com/OWASP/Amass/v3/...; #configuracoes
go get -u github.com/tomnomnom/httprobe;
go get github.com/tomnomnom/waybackurls;
GO111MODULE=on go get -u -v github.com/bp0lr/gauplus;
GO111MODULE=on go get -v github.com/projectdiscovery/nuclei/v2/cmd/nuclei;
cd ~/tools; git clone https://github.com/hahwul/dalfox; cd dalfox; git pull -v; go install; go build;  ; #editar payloads
go get -u github.com/KathanP19/Gxss;
go get -u github.com/tomnomnom/gf; 
go get -u github.com/ffuf/ffuf;
cd ~/tools; git clone https://github.com/1ndianl33t/Gf-Patterns;
cd ~; mkdir .gf;
mv /root/tools/Gf-Patterns/*.json ~/.gf;
GO111MODULE=on go get -v github.com/projectdiscovery/notify/cmd/notify; #configurar

mv /root/go/bin/* /usr/bin/;
