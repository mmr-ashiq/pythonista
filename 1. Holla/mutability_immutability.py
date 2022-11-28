x = 1
y = x

id(x) == id(y) # True

y = 2

id(x) == id(y) # False

""" 
    A mutable object is an object whose state can be modified after it is created.
    An immutable object is an object whose state cannot be modified after it is created.

"""