#!/bin/bash

for i in $(cat $3); do
	cat $1 | qsreplace "$i" | anew replaced;
	ffuf -u FUZZ -H "User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36" -w replaced -mr $2 -of ecsv -o result;
	cat result | cut -d "," -f2 | sed '1d' | anew $4_results.txt;
	rm result replaced;
done
cat $4_results.txt | notify;
