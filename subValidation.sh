########################################################################################################################
#############################################validando subdominios######################################################

echo "Validando subdominios " | notify;
cat $1 | httpx -threads 200 -random-agent -o 200;
cat 200 | anew "$1200"; rm 200;
cat $1 | httprobe -p http:81 -p http:3000 -p https:3000 -p http:3001 -p https:3001 -p http:8000 -p http:8080 -p https:8443 -p https:10000 -p http:9000 -p https:9443 -c 50 | anew "$1200";
