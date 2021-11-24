# every object have a unique id
# id() is used to get the unique id of an object.
print(id(6))
a = 3
print(id(a))
b = a  # a and b both refer to the same object
print(id(b))


x = 9
y = 9
print(id(x))  # 1712033458736
print(id(y))  # 1712033458736
# in python, literals are store at same location if they are same value.


m = 69
n = 69
print (m is n)  # True
# is operator gives True if both the variables are pointing to same object.


u = m
print(u is n) # True
u = 2 # when we assign 2 into u, it will create a new object.
print(u is n) # False