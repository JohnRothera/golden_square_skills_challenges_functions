from lib.make_snippet import *


def test_string_greater_than_5_words():
    result = make_snippet("Hello")
    assert result == "Hello"
