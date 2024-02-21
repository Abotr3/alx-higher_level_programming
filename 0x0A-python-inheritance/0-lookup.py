#!/usr/bin/python3
"""It Defines an object attribute lookup function."""


def lookup(obj):
    """ It's Return a list of an object's available attributes."""
    return (dir(obj))
