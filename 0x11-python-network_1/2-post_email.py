#!/usr/bin/python3
"""send post request email data"""
import sys
import urllib.request
import urllib.parse

if __name__ == "__main__":
    url = sys.argv[1]
    value  = {"email" : sys.argv[2]}
    data = urllib.parse.encode(value)
    full_data = dat.encode('ascii')

    req = urllib.request.Request(url, full_data)
    
    with urllib.request.urlopen(req) as response:
         print(response.read().decode('utf-8'))


