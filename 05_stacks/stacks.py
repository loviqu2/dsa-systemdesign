# stack = []
# stack.append(1)
# stack.append(2)
# stack.append(3)
# stack.append(4)
# print(stack.pop())


# to find whether the bracket are all resolved or there are openings
# loop through the characters and find if it is an opening bracket, append into stack
# if the next bracket is an open closed bracket, pop the "(" from the stack to remove it from waiting
# if the next bracket is an open bracket, just return as false

def is_balanced(s):
    stack = []

    for char in s:
        if char == "(":
            stack.append(char)
        if char == ")":
            if stack:
                stack.pop()
            else:
                return False

    return len(stack) == 0  # if the stack is 0 then return True, else false


print(is_balanced("(()"))
print(is_balanced("(())"))
print(is_balanced("()()"))


