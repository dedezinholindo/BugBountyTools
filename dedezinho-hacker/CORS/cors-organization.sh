#!/bin/bash

for i in $(seq 0 $(($(cat cors-results.json | jq '.[].severity' | wc -l)-1))) ;do
        s=$(($i + 1));
        if [ $(cat cors-results.json | jq '.[].severity' | sed -n "$s p") == "\"high\"" ]
        then
                echo $(cat cors-results.json | jq "keys[$i]") >> vulnerables-cors.txt;
        fi
done
