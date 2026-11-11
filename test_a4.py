import pytest
from a4 import *

def test_calculate_ticket_price():
    assert calculate_ticket_price(0, 1, 0, 10) == 14.25
    assert calculate_ticket_price(2, 2, 0, 17) == 30
    assert calculate_ticket_price(2, 2, 0, 13) == 28.50
    assert calculate_ticket_price(2, 1, 1, 13) == 30.40
    assert calculate_ticket_price(3, 2, 1, 14) == 38.95
    assert calculate_ticket_price(3, 1, 2, 15) == 49
    assert calculate_ticket_price(4, 3, 2, 11) == 69.35
    assert calculate_ticket_price(-2, 5, 6, 2) == None
    assert calculate_ticket_price(2, -5, 6, 2) == None
    assert calculate_ticket_price(2, 5, -6, 2) == None
pytest.main()