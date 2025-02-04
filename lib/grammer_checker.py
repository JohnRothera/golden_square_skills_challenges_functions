def grammer_checker(string):
    first_char = string[0]
    last_char = string[-1]
    return first_char.isupper() and last_char in "!.?"
