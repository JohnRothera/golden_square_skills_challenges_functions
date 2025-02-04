# {{PROBLEM}} Function Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

As a user
So that I can manage my time
I want to see an estimate of reading time for a text, assuming that I can read 200 words a minute.

## 2. Design the Function Signature

_Include the name of the function, its parameters, return value, and side effects._

```python
# EXAMPLE

def estimate_reading_time(text):
    """Finds number of words in a piece of text 
       and returns an estimate for how long 
       it should take to read.

    Parameters: (list all parameters and their types)
        string, or possibly a .txt file for lots of words.

    Returns: (state the return value and its type)
        probably a float representing an amount of minutes, wrapped in a string
        so it feels more interactive for the user.

    Side effects: (state any side effects)
        This function doesn't print anything or have any other side-effects
    """
    pass # Test-driving means _not_ writing any code here yet.
```

## 3. Create Examples as Tests

_Make a list of examples of what the function will take and return._

```python
# EXAMPLE

from lib.reading_time import *

# Initially check for the amount of words given as a parameter.
def test_amount_of_words():
    result = reading_time("This is an amount of words")
    assert result == 6

# Add functionality for the user stories request of a simple algorithm to estmate reading time. 
# They read 200 words a minute. That would be 3.33 words a second. My algorithm would be to 
# firstly check amount of words and then multiply them by 3.33 to get a tme in seconds.
def test_amount_of_words_time_equation():
    result = reading_time("This is an amount of words and they need to be put into a simple function that calculates how long it would take to read them all")
    assert result == 89.91



_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

Ensure all test function names are unique, otherwise pytest will ignore them!
