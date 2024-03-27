#!/bin/bash
# Sends a GET request tosplay the response status code.
curl -s -o /dev/null -w "%{http_code}" "$1"
