
def add(stack):
    item_1 = stack.pop()
    item_2 = stack.pop()
    result = item_2 + item_1
    stack.append(result)

def subtract(stack):
    item_1 = stack.pop()
    item_2 = stack.pop()
    result = item_2 - item_1
    stack.append(result)

def multiply(stack):
    item_1 = stack.pop()
    item_2 = stack.pop()
    result = item_2 * item_1
    stack.append(result)

def divide(stack):
    item_1 = stack.pop()
    item_2 = stack.pop()
    result = item_2 / item_1
    stack.append(result)

def if_(stack):
    item_2 = stack.pop()
    item_1 = stack.pop()
    evaluated = stack.pop()
    if evaluated:
        stack.append(item_1)
    else:
        stack.append(item_2)