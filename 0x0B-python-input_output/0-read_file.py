#!/usr/bin/python3
"""Defines a .txt file reading function"""


def read_file(filename=""):
    """Prints the files contents to standard output"""
    with open(filename, mode='r', encoding="utf-8") as f:
        print(f.read(), end="")
