#!/usr/bin/python3
for i in range(97, 123):
    letter = chr(i)
    if(chr(i) != 'q') or (chr(i) != 'e'):
        print("{}".format(letter), end='')
