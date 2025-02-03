from lib.count_words import *


def test_number_of_words_in_string():
    result = count_words("How many words in this string?")
    assert result == 6
