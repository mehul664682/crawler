#!/usr/bin/env python

import requests


def request(url):
    try:
        return requests.get("http://" + url)
    except requests.exceptions.ConnectionError:
        pass

# find sub domain
#target_url = "google.com"
#with open("/root/Downloads/subdomains.list", "r") as wordlist_file:
#    for line in wordlist_file:
#        word = line.strip()
#        test_url = word + "." + target_url
#        response = request(test_url)
#        if response:
#            print("[+] Discovered subdomain --> " + test_url)


# find Dir
target_url = "www.rajkotgurukul.org"

with open("/root/Downloads/common.txt", "r") as wordlist_file:
    for line in wordlist_file:
        word = line.strip()
        test_url = target_url + "/" + word
        response = request(test_url)
        if response:
            print("[+] Discovered URL --> " + test_url)

