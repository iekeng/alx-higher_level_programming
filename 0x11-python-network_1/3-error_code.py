#!/usr/bin/python3
"""Sends url request"""


if __name__ == "__main__":
    import urllib.request
    import sys

    url = sys.argv[1]

    try:
        with urllib.request.urlopen(url) as response:
            print(response.read().decode('UTF-8'))
    except urllib.error.HTTPError as e:
        print('Error code: ', e.code)
