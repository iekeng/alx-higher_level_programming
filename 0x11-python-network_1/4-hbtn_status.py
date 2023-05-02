#!/usr/bin/python3
"""retrieves data from url"""


if __name__ == "__main__":
    import requests

    r = requests.get('https://alx-intranet.hbtn.io/status')
    print('Body response:')
    print('\t - ', type(r.text))
    print('\t - content: ', r.text)

