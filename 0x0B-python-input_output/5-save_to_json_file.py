#!/usr/bin/python3
"""Defines a JSON file writing function"""
import json


def save_to_json_file(my_obj, filename):
    """writes an object to a text file using JSON"""
    x = json.dumps(my_obj)

    with open(filename, mode='w', encoding="utf-8") as f:
        json.dumps(my_obj, f)
