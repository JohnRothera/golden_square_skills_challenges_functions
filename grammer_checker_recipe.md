# {{PROBLEM}} Function Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

As a user
So that I can improve my grammar
I want to verify that a text starts with a capital letter and ends with a suitable sentence-ending punctuation mark.

## 2. Design the Function Signature

_Include the name of the function, its parameters, return value, and side effects._

```python
# EXAMPLE

def grammer_checker(text):
    """Checks that the first letter in some given text starts with a capital.
       Also checks that the entered text ends with an appropriate sentence ending 
       punctuation mark.

    Parameters: (list all parameters and their types)
        String. Depending on how deep we want to go with this, we could 
        split the string and check to see if the final char in a word is a 
        punctuation mark already indicating multiple sentences.


    Returns: (state the return value and its type)
        I think a bool would be most appropriate and probably the first and last words 
        including if any alterations were made. 

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

# Initially check if first char in given string conforms to the user story.
def test_check_first_and_last_char():
    first_char = grammer_checker("these are some words that don't conform")
    assert first_char == False


_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

Ensure all test function names are unique, otherwise pytest will ignore them!
