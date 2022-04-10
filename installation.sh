#!/bin/bash

#go por wget
apt-get update;
apt-get upgrade -y;
apt-get install python3-pip -y;
echo "set-option -g history-limit 99999" > ~/.tmux.conf;
apt-get install sqlmap -y;
apt install snapd -y;
apt-get install jq -y;
sudo apt-get install cargo -y;
cargo install x8;
apt-get install git -y;
apt-get install host -y;
go mod init puppy;
apt-get install wget -y;
apt-get install tmux -y; 
go install -v github.com/tomnomnom/anew@latest;
go install github.com/hiddengearz/jsubfinder@latest;
wget https://raw.githubusercontent.com/ThreatUnkown/jsubfinder/master/.jsf_signatures.yaml && mv .jsf_signatures.yaml ~/.jsf_signatures.yaml;
go install -v github.com/projectdiscovery/shuffledns/cmd/shuffledns@latest;
pip3 install requests;
go install -v github.com/tomnomnom/assetfinder@latest;
go install github.com/003random/getJS@latest;
wget https://github.com/findomain/findomain/releases/latest/download/findomain-linux;
chmod +x findomain-linux;
mv findomain-linux findomain; mv findomain /usr/bin;
mkdir tools;
mkdir lists;
cd ~/lists; wget https://raw.githubusercontent.com/s0md3v/Arjun/master/arjun/db/params.txt
cd ~/tools; git clone https://github.com/s0md3v/XSStrike.git; pip3 install -r XSStrike/requirements.txt
cd ~/tools; git clone https://github.com/s0md3v/Corsy.git;  
cd ~/tools; git clone https://github.com/aboul3la/Sublist3r.git; pip3 install -r Sublist3r/requirements.txt
cd ~/tools; git clone https://github.com/gwen001/github-search.git;
cd ~/tools; git clone https://github.com/m4ll0k/takeover.git;
cd ~/tools; git clone https://github.com/devanshbatham/ParamSpider.git; pip3 install -r ParamSpider/requirements.txt;
cd ~/tools; git clone https://github.com/GerbenJavado/LinkFinder.git; pip3 install -r LinkFinder/requirements.txt;
cd ~/tools; git clone https://github.com/m4ll0k/SecretFinder.git; pip3 install -r SecretFinder/requirements.txt;
cd ~/tools; git clone https://github.com/KingOfBugbounty/Bug-Bounty-Toolz.git;
cd ~; git clone https://github.com/projectdiscovery/nuclei-templates.git;
cd ~/tools; git clone https://github.com/0x240x23elu/JSScanner.git; pip3 install -r JSScanner/requirements.txt
cd ~/tools; git clone https://github.com/s0md3v/Arjun.git; cd Arjun; python3 setup.py install;
cd ~/tools; git clone https://github.com/blechschmidt/massdns.git; cd massdns; make; mv bin/massdns /usr/bin/;
go install -v github.com/projectdiscovery/chaos-client/cmd/chaos@latest;
go install -v github.com/projectdiscovery/httpx/cmd/httpx@latest;
GO111MODULE=off go get -u -v github.com/lc/subjs;
snap install amass; #configuracoes
go install github.com/tomnomnom/httprobe@latest;
go install github.com/tomnomnom/waybackurls@latest;
go install github.com/bp0lr/gauplus@latest;
go install -v github.com/projectdiscovery/nuclei/v2/cmd/nuclei@latest;
go install github.com/hahwul/dalfox/v2@latest;
#cd ~/tools; git clone https://github.com/hahwul/dalfox; cd dalfox; git pull -v; go install; go build; #editar payloads
go install github.com/KathanP19/Gxss@latest;
go install -v github.com/tomnomnom/gf@latest; 
go install github.com/ffuf/ffuf@latest;
cd ~/tools; git clone https://github.com/1ndianl33t/Gf-Patterns;
cd ~; mkdir .gf;
mv ~/tools/Gf-Patterns/*.json ~/.gf;
go install -v github.com/projectdiscovery/notify/cmd/notify@latest; #configurar

mv ~/go/bin/* /usr/bin/;
