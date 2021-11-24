# Type() is a built-in function that returns the data-type of the specified value.


x = 5
print(type(x))  # <class 'int'>

y = 3.5
print(type(y))  # <class 'float'>

z = "Zero"
print(type(z))  # <class 'str'>
# in python, there is no character data type.

xyz = True
print(type(xyz))  # <class 'bool'>

complex_unka_panka = 1+2j
print(type(complex_unka_panka))  # <class 'complex'>

none = None  # kind of null in c++/java
print(type(none))  # <class 'NoneType'>

list = [1, 2, 3, True, "abc"]
print(type(list))  # <class 'list'>

"""
    list is a mutable sequence of objects.
    list is like array, like other programming languages.
    difference between list and array is that list is mutable and array is immutable.
    we can dynamically add and remove elements from list & don't have to worry about size of list.
    in list memory can be allocated dynamically and in array memory is allocated statically.
    similar to vector in c++. and arrayList in java.
"""

tuple = (1, 2, 5, True, "abc")
print(type(tuple))  # <class 'Tuple'>

"""
    tuple is also like a list.
    difference between tuple and list is that tuple is immutable and list is mutable.
    that means we can't modify once we created tuple.
    if we try to modify tuple, we will get an error.
"""

s = set([1, 2, 4, 'Set', True])
print(type(s))  # <class 'Set'>

se_t = {10, 20, 30, 40, 50}
print(type(se_t)) # <class 'Set'>

"""
    Set is a collection of unique elements (distinct keys).
    Set is like a hash table in c++.
    Set itself is a mutable and can be modified.
    Set is unordered.
    Set is iterable.
    Set has it's own internal different way of storing it's elements.
    Set internally using hashing to implement all the keys. and these keys can't not be repeated.
    Mathmetical Set operations like union, intersection, symmetric difference, etc. are really fast.
"""

"""
    [] => list
    () => tuple
    {} => set

    Sequence Types: list, tuple, String, Set, dictionary
"""

d = dict(a=1, b=2, c=3)
print(type(d)) # <class 'Dict'>

dic = {'a':1, 'b':2, 'c':3}
print(type(dic)) # <class 'Dict'>

"""
    Dictionary is a collection of key-value pairs.
    Dictionary is used to store mapping of keys to values.
    Difference between Set and Dictionary is that Set is collection of keys and Dictionary is collection of key-value pairs.
    Set is unordered and Dictionary is ordered.
    Dictionary also mutable.
    Dictionary and Set both internally using hashing.
    Dictionary is used to storing collection of key-value pairs.
"""
