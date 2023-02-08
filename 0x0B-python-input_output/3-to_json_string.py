#!/usr/bin/python3
"""Defines a string to JSON converter"""
import json


def to_json_string(my_obj):
    """Returns JSON format of my_obj"""
    return json.dumps(my_obj)
