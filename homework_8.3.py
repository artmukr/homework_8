# @ -0,0 +1,24 @@
# Write a function that takes a sentence (string) and any number of
# key-word arguments. All kwargs are filters for that question.
# These filters decide whether the function returns True or False
# Possible filters:
#   - max_length: integer !REQUIRED FILTER
#   - includes: list of strings (substring that the sentence must contain)
#   - has_spaces: boolean
#   etc
#
# max_length is required kwarg. If it hasn't been provided, the function
# must return None
#
# see asserts for better understanding


def is_valid(string, **filters):
    def is_valid(string, **filters):
        a = filters.get('max_length', None)
        b = filters.get('has_spaces', None)
        c = filters.get('includes', None)
        length = len(string)
        space_find = string.find(" ")
        inc = 0

        for el in c:
            if string.find(el) == -1:
                inc = 0
                break
            else:
                inc = 1

        if c is not None and a is not None and inc == 1:
            return True
        if c is not None and a is not None and inc == 0:
            return False

        if a is None:
            return None

        if length > a and a is not None:
            return False

        if a is not None and b is not None and b == True and space_find != -1:
            return True
        if a is not None and b is not None and space_find == -1:
            return False


assert is_valid('Hi! My name is Jim', max_length=30, has_spaces=True) is True
assert is_valid('RobertSteveJohn', max_length=10, has_spaces=False) is False
assert is_valid('Hey guys! Have you ever played football:)',
                includes=['?', '.'], max_length=100) is False
assert is_valid("What's up?", has_spaces=True) is None