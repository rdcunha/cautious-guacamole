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

def test_div():
    assert cg.div(20, 4) == 5
    assert cg.div(5, 2) == 2.5

def test_mod():
    assert cg.mod(4, 3) == 1
    assert cg.mod(23, 7) == 2

def test_sum():
    A = range(10)
    assert cg.sum(A) == 45

@pytest.mark.parametrize("in1, in2, expected", [ (3, 2, 9), (20, 2, 400), (1, 10, 1), ])

def test_pow(in1, in2, expected):
    assert cg.pow(in1, in2) == expected
