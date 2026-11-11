import pytest
from a2 import *

def test_sort_word():
    assert sort_word("programming") == "aggimmnoprr"
    assert sort_word("civic") == "cciiv"
    assert sort_word("aabb") == "aabb"
    assert sort_word("PaBaBB") == "aaBBBP"
    assert sort_word("BaAaA") == "AAaaB"
pytest.main()