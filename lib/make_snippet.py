from lib.count_words import *


def make_snippet(string):
    if count_words(string) > 5:
        list_of_strings = string.split()
        result = list_of_strings[:5]
        return " ".join(result) + "..."
    if len(string.split()) < 5:
        return string
