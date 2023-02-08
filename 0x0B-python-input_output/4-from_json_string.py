#!/usr/bin/python3
"""Defines a JSON to object converter"""
import json


def from_json_string(my_str):
    """Returns python object """
    return json.loads(my_str)
