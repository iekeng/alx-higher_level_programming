#!/usr/bin/python3
"""Sends url request"""
if __name__ == "__main__":
    import urllib.request
    import sys

    url = sys.argv[1]

    req = urllib.request.Request(url)

    with urllib.request.urlopen(req) as response:
        try:
            response
        except urllib.error.HTTPError as e:
            print('Error code: ', e.code)
