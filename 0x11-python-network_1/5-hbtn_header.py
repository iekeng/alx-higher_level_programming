#!/usr/bin/python3
"""Get the value of X-Request-Id header"""


if __name__ == "__main__":
    import sys
    import requests

    r = requests.get(sys.argv[1])
    res = r.headers.get('X-Request-Id')
    print(res)
