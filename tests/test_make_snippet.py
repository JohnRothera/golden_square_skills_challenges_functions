from lib.make_snippet import *


# The first test simply checks we get a returned string
def test_string_returns():
    result = make_snippet("Hello")
    assert result == "Hello"


def test_string_less_than_5_words():
    result = make_snippet("Hello world")
    assert result == "Hello world"


def test_string_more_than_5_words_ends_with_ellipses():
    result = make_snippet("Hello world what a pleasure to be here")
    assert result == "Hello world what a pleasure..."


def test_string_longer_than_5_with_special_chars():
    result = make_snippet("Hello, world! What a pleasure to be here!!")
    assert result == "Hello, world! What a pleasure..."
