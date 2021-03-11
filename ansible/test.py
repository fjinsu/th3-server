#!/bin/python3

import requests
url_for_version = "dns_for_aws_loadbalancer/version"
url = "dns_for_aws_loadbalancer"
version = requests.get(url_for_version)
phrases = ["Victory+or+Death","Lol","Okay","Hey","I+obey","By+my+Axe","Well+Met"]

while(version.content == 'v2'):
    for phrase in phrases:
        test = requests.get(url + '/api/v1/translate?phrase=' + phrase)
        print(test.content)
        version = requests.get(url_for_version)
