
def add(stack):
    """
    Adds the two top numbers ontop of the stack
    """
    item_1 = stack.pop()
    item_2 = stack.pop()
    result = item_2 + item_1
    stack.append(result)


def subtract(stack):
    """
    Subtracts the second from the first top numbers ontop of the stack
    """
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


def exists(stack):
    """
    Take in a stack, pop off the interrogated value, and the two possible
    results

    If the interrogated value EXISTS (does not mean the same as is blank,
    then the first value is put on the top of the stack, otherwise the second
    value is returned.

    """
    item_2 = stack.pop()
    item_1 = stack.pop()
    evaluated = stack.pop()
    if evaluated is None:
        stack.append(item_2)
    else:
        stack.append(item_1)

#isBlank

#NaN

#FixMe: deal with an operation that contains a callable.
