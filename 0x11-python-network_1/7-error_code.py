#!/usr/bin/python3
"""
Script that takesa URL, sends a request to the URL and displays the body
of the redecoded in utf-8). Only used requests and sys packages
"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]

    r = requests.get(url)
    if r.status_code >= 400:
        print('Error code: {}'.format(r.status_code))
    else:
        print(r.text)
