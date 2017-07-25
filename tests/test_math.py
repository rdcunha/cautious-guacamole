"""
Testing for the math.py module.
"""

import cautious_guacamole as cg
import pytest

def test_add():
    assert cg.add(5, 2) == 7
    assert cg.add(2, 5) == 7

def test_mult():
    assert cg.mult(3, 4) == 12
    assert cg.mult(4, 5) == 20
