## Deque

- Deque stands for double-ended queue.
- It is a data structure that can be used to add and remove elements from both ends of the list.
- In python it is a part of the collections module.
- It can be use to implement a queue or a stack.
- In case of stack, list and deque both provide constant time performance for push and pop operations.
- But when we implement a queue using list, list does not have constant time performance for push and pop operations.
- But Deque allows us to do enqueue and dequeue operations in constant time.
- All the operations in deque are O(1) time complexity.
- Slicing is not supported in deque.

## Time Complexity and internal working of deque
- O(1)
    - append(x)
    - appendleft(x)
    - pop()
    - popleft()
- O(n)
    - d[i]
    - count(x)
    - insert(i,x)
- θ(abs(r))
    - rotate(r)
- θ(len(l))
    - extend(l)
    - extendleft(l)