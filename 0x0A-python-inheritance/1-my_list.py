#!/usr/bin/python3
"""It Defines an inherited list class MyList."""


class MyList(list):
    """It Implements sorted printing for the built-in list class."""

    def print_sorted(self):
        """It's Print a list in sorted ascending order."""
        print(sorted(self))
