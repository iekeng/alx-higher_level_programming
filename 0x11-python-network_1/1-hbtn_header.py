#!/usr/bin/python3
"""Retrieves the value of X-Request-Id header"""
import urllib.request
import sys

if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as response:
        headers = response.headers
        print(headers['X-Request-Id'])
