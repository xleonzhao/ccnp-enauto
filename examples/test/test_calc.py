import pytest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from calc import add_numbers

def test_add_numbers():
    test_data = [
        (1, 2, 3),
        (1, -5, -4),
        (-1, -1, -2),
        (0, 7, 7),
        (0, 0, 0),
        (1, -1, 0),
        (4, 5, 1)
    ]

    for a, b, expected in test_data:
        assert add_numbers(a, b) == expected
