#!/usr/bin/python3
"""
Scriptakes in a URL and an email, sends a POST request to the passed
URL with the ail as a parameter, and displays the body of the response
(decoded in utf). Only uses request and sys packages
"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    value = {'email': sys.argv[2]}

    r = requests.post(url, data=value)
    print(r.text)
