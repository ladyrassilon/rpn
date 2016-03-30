"""
All the operators used by all the implemented operators in the library.
"""
from rpn.decorators import get_items


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
    Subtracts the second from the first top numbers ontop of the stack.
    """
    item_1 = stack.pop()
    item_2 = stack.pop()
    result = item_2 - item_1
    stack.append(result)


def multiply(stack):
    """
    Multiply the first two numbers on top of the stack.
    """
    item_1 = stack.pop()
    item_2 = stack.pop()
    result = item_2 * item_1
    stack.append(result)


def divide(stack):
    """
    Divides the second number by the first number on top of the stack.
    """
    item_1 = stack.pop()
    item_2 = stack.pop()
    result = item_2 / item_1
    stack.append(result)


def if_(stack):
    """
    Take in a stack, pop off the interrogated value, and the two possible
    results

    If the interrogated value evaluates to true then the first value is put
    on the top of the stack, otherwise the second value is returned.
    """
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
    from sympy import symbols
    none = symbols("none")
    item_2 = stack.pop()
    item_1 = stack.pop()
    evaluated = stack.pop()
    if evaluated is none:
        stack.append(item_2)
    else:
        stack.append(item_1)


def equals(stack):
    """
    Take the stack, pop off four items, if the two last items are equals
    append the first item to the stack, if they are unequal the second.
    """
    item_1 = stack.pop()
    item_2 = stack.pop()
    conditional_1 = stack.pop()
    conditional_2 = stack.pop()

    if conditional_1 == conditional_2:
        stack.append(item_1)
    else:
        stack.append(item_2)


def greater_than(stack):
    """
    Take the stack, pop off four items, if the first conditional is larger than
    the second conditional append the first item to the stack, otherwise,
    append the second.
    """
    item_1 = stack.pop()
    item_2 = stack.pop()
    conditional_1 = stack.pop()
    conditional_2 = stack.pop()

    if conditional_1 > conditional_2:
        stack.append(item_1)
    else:
        stack.append(item_2)


def less_than(stack):
    """
    Take the stack, pop off four items, if the first conditional is larger than
    the second conditional append the first item to the stack, otherwise,
    append the second.
    """
    item_1 = stack.pop()
    item_2 = stack.pop()
    conditional_1 = stack.pop()
    conditional_2 = stack.pop()

    if conditional_1 < conditional_2:
        stack.append(item_1)
    else:
        stack.append(item_2)


def absolute(stack):
    """
    Pop off the first item, and return its absolute value.
    """
    item = stack.pop()

    absolute_item = abs(item)

    stack.append(absolute_item)


def negative(stack):
    """
    Pop off the first item and return its negative.
    """
    item = stack.pop()

    negative_item = -item

    stack.append(negative_item)


@get_items
def sum_list(stack, items):
    """
    Pop off the first item, then if its a positive integer, pop that many items
    off the stack and return their sum.
    """
    total = sum(items)
    stack.append(total)


@get_items
def mean_list(stack, items):
    """
    Pop off the first item, then if its a positive integer, pop that many items
    off the stack and return their mean.
    """
    number_of_items = len(items)
    total = sum(items)
    average = total / number_of_items
    stack.append(average)


@get_items
def median_list(stack, items):
    """
    Pop off the first item, then if its a positive integer, pop that many items
    off the stack and return their median.
    """
    items.sort()
    number_of_items = len(items)
    mid = number_of_items / 2
    if number_of_items % 2:
        median = items[mid]
    else:
        item_1 = items[mid-1]
        item_2 = items[mid]
        median = (item_1 + item_2)/2
    stack.append(median)
