#!/bin/bash

# create variable
count_request=0
count_ip=0
count_method_get=0
count_method_post=0
ip_arr=()
declare -A url_dict

echo "read logs"

# read file logs for line
while read -r line; do
        count_request=$((count_request + 1))

        # get method from line
        method=$(echo "$line" | awk '{print $6}')
        # add counter for method
        if [[ $method == "\"GET" ]]; then
                count_method_get=$((count_method_get + 1))
        elif [[ $method == "\"POST" ]]; then
                count_method_post=$((count_method_post + 1))
        fi

        # get ip from line
        ip=$(echo "$line" | awk '{print $1}')
        unique_ip=1
        # checking uniqueness ip
        for item in "${ip_arr[@]}"; do
                if [[ $ip == $item ]]; then
                        unique_ip=0
                        break
                fi
        done
        # add unique ip in array
        if [[ $unique_ip -eq 1 ]]; then
                ip_arr+=($ip)
                count_ip=$((count_ip + 1))
        fi

        # get url from line
        url=$(echo "$line" | awk '{print $7}')
        # add url in dictionary
        if [[ -v url_dict[$url] ]]; then
                url_dict[$url]=$((url_dict[$url] + 1))
        else
                url_dict[$url]=1
        fi
        # find most famous url
        max_url=0
        for key in "${!url_dict[@]}"; do
                if [[ url_dict[$key] -gt $max_url ]]; then
                        max_url=${url_dict[$key]}
                        famous_url=$key
                fi
        done

done < access.log

echo "creating report.txt"

cat <<EOF > report.txt
--------------------------------------------------------------
REPORT

Count of requests: $count_request
Count of unique IP-adress: $count_ip

Count of method:
        GET  $count_method_get
        POST $count_method_post

Famous URL: $famous_url used $max_url times
--------------------------------------------------------------
EOF