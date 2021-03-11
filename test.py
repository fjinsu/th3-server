#!/bin/python3

import requests
import json

url_for_version = "dns_for_aws_loadbalancer/version"
url = "dns_for_aws_loadbalancer"
vers_resp = requests.get(url_for_version)
phrases = ["Victory+or+Death","Lol","Okay","Hey","I+obey","By+my+Axe","Well+Met"]

vers_json = json.loads(vers_resp.content)
while(vers_json["version"] != '0.0.2'):
    for phrase in phrases:
        test = requests.get(url + '/api/v1/translate?phrase=' + phrase)
        print(test.content)
        vers_resp = requests.get(url_for_version)
        vers_json = json.loads(vers_resp.content)
        print(vers_json["version"])