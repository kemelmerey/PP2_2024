"""
The expression is the current item in the iteration, but it is also the outcome, which you can manipulate before it ends up like a list item in the new list
"""
#Set the values in the new list to upper case
newlist = [x.upper() for x in fruits]

#Set all values in the new list to 'hello'
newlist = ['hello' for x in fruits]

#Return "orange" instead of "banana
newlist = [x if x != "banana" else "orange" for x in fruits]
