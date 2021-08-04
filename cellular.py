# This will configure the mobile network.
# Can also trigger disable hostpot wifi script
# Use tmobile card instead


# https://toddhayton.com/2014/12/08/form-handling-with-mechanize-and-beautifulsoup/



# POST /goform/goform_set_cmd_process HTTP/1.1
# Host: 192.168.0.1
# Content-Length: 59
# Accept: application/json, text/javascript, */*; q=0.01
# X-Requested-With: XMLHttpRequest
# User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36
# Content-Type: application/x-www-form-urlencoded; charset=UTF-8
# Origin: http://192.168.0.1
# Referer: http://192.168.0.1/index.html
# Accept-Encoding: gzip, deflate
# Accept-Language: en-US,en;q=0.9
# Connection: close

# isTest=false&goformId=LOGIN&password=YWRtaW4%3D&save_login=

from bs4 import BeautifulSoup