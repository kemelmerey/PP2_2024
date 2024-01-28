"""
The iterable can be any iterable object, like a list, tuple, set etc
Example
You can use the range() function to create an iterable:
"""
newlist = [x for x in range(10)]
#Accept only numbers lower than 5:
newlist = [x for x in range(10) if x < 5]