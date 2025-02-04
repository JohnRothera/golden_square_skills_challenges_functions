from lib.reading_time import *


# Initially check for the amount of words given as a parameter.
# Comment out when we get that passing.

# def test_amount_of_words():
#     result = reading_time("This is an amount of words")
#     assert result == 6


# def test_amount_of_words_time_equation():
#     result = reading_time(
#         """This is an amount of words and they need to be put
#         into a simple function that calculates how long
#         it would take to read them all"""
#     )
#     assert result == 89.91


def test_reading_time_with_feedback():
    result = reading_time(
        """This is an amount of words and they need to be put 
        into a simple function that calculates how long 
        it would take to read them all"""
    )
    assert (
        result
        == """It would take approximately 89.91 seconds or 1.50 minutes to read this piece of text."""
    )
