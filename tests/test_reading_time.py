from lib.reading_time import *


# Initially check for the amount of words given as a parameter.
def test_amount_of_words():
    result = reading_time("This is an amount of words")
    assert result == 6
