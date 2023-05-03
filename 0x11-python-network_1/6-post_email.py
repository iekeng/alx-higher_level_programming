#!/usr/bin/python3
"""Send post request to a URL and email as a param"""
import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]
    data = {"email": sys.argv[2]}
    r = requests.post(url, data=data)
    print("{}".format(r.text))






