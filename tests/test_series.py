from math_series import __version__
from  math_series.series import *

def test_version():
    assert __version__ == '0.1.0'

# Test case for fibonaci

def test_zero():
    actual = fibonaci(0)
    expected = 0
    assert actual == expected

def test_one():
    actual = fibonaci(1)
    expected = 1
    assert actual == expected

def test_not_zero_or_one():
    actual = fibonaci(8)
    expected = 21
    assert actual == expected


# Test cases for Lucas 

def test_zero_lucas():
    actual = lucas(0)
    expected = 2
    assert actual == expected

def test_one_lucas():
    actual = lucas(1)
    expected = 1
    assert actual == expected

def test_not_zero_or_one_lucas():
    actual = lucas(11)
    expected = 199
    assert actual == expected