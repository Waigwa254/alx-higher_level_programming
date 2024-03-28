#!/usr/bin/python3
"""
Takes yourthub credentials and uses the GitHub API
to dispaly yo
"""

import requests
from sys import argv

if __name__ == '__main__':
    url = 'https://api.github.com/user'
    response = requests.get(url, auth=(argv[1], argv[2]))
    try:
        print(response.json().get("id"))
    except ValueError:
        print("Not a valid JSON")
