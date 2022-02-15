def isBalanced(string):
    stack = []
    for char in string:
        if char == '(' or char == '[' or char == '{':
            stack.append(char)
        elif char == ')':
            if len(stack) == 0:
                return False
            elif stack[-1] == '(':
                stack.pop()
            else:
                return False
        elif char == ']':
            if len(stack) == 0:
                return False
            elif stack[-1] == '[':
                stack.pop()
            else:
                return False
        elif char == '}':
            if len(stack) == 0:
                return False
            elif stack[-1] == '{':
                stack.pop()
            else:
                return False
    if len(stack) == 0:
        return True
    else:
        return False

    
print(isBalanced('[(])'))
print(isBalanced('[()]'))
print(isBalanced('[{})'))