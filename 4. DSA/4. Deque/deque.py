from collections import deque

d = deque() # create an empty deque
d.append(10) # add an element to the right side
d.append(20)
d.append(30)

d.appendleft(40) # add an element to the left side

print(d) # deque([40, 10, 20, 30])

print(d.pop()) # remove an element from the right side
print(d.popleft()) # remove an element from the left side
print(d) # deque([10, 20])

d.insert(2, 50) # insert an element at a given index (2)
d.insert(3, 10)

print(d.count(10)) # count the number of occurrences of an element (20)
d.remove(10) # remove first occurrence of an element (10)
print(d) # deque([20, 50, 10])

d.reverse() # reverse the order of the elements in the deque
print(d) # deque([10, 50, 20])

print(d.index(50)) # return the index of the first occurrence of an element

d.extend([60, 70]) # add a list of elements to the right side
print(d) # deque([10, 50, 20, 60, 70])

d.extendleft([80, 90]) # add a list of elements to the left side
print(d) # deque([90, 80, 10, 50, 20, 60, 70])
"""
extend & extendleft are the similar to the append and appendleft methods, but they add elements to the left or right side of the deque, respectively.
"""

d.rotate(1) # rotate clockwise by 1 element
print(d) # deque([70, 90, 80, 10, 50, 20, 60])
d.rotate(-2) # rotate counter-clockwise by 2 elements
print(d) # deque([80, 10, 50, 20, 60, 70, 90])

d.reverse() # reverse the order of the elements in the deque
print(d) # deque([90, 70, 60, 20, 50, 10, 80])

print(d[2]) # return the element at index 2
d[2] = 100 # replace an element at a given index (2)
print(d) # deque([90, 70, 100, 20, 50, 10, 80])