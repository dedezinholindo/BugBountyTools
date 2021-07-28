#!/bin/bash

ffuf -u FUZZ/PATH -H "User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36" -w $1:FUZZ -w $3:PATH -mr $2 -of ecsv -o result;
cat result | cut -d "," -f3 | sed '1d' | anew $4_results.txt;
rm result;
cat $4_results.txt | notify;
