import pytest
from secret_word_game import *

def test_secret_word_game():
    assert game_start("hello", "goodbye", "yes", "no", "maybe", "happy", "sad", "angry", "hungry", "upset")
    assert score_keeping(1, 2, 3, 4, 5)
pytest.main()