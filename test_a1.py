import pytest
from a1 import *

def test_multiply_nums():
    assert multiply_nums(3, 4) == 12
    assert multiply_nums(-9, -4) == 36
    assert multiply_nums(6, -3) == -18
    assert multiply_nums(-4, 0) == 0
    assert multiply_nums(0, 4) == 0
    assert multiply_nums("abc", "xyz") == None
pytest.main()