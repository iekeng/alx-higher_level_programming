#!/usr/bin/python3
"""Defines a string to JSON converter"""


def to_json_string(my_obj):
    """Returns JSON format of my_obj"""
    return json.dump(my_obj)
