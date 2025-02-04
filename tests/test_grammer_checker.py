from lib.grammer_checker import *


# def test_check_first_char_is_not_upper():
#     first_char = grammer_checker("these are some words that don't conform")
#     assert first_char == False


# def test_check_first_char_is_upper():
#     first_char = grammer_checker("These are some words that do conform")
#     assert first_char == True


def test_last_char_is_punctuation_mark():
    first_and_last_char = grammer_checker("These are some words that conform.")
    assert first_and_last_char == True
