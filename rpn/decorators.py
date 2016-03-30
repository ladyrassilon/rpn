from exceptions import NotPositiveInteger


def get_items(operator_function):
    """
    Pops the top item off the stack, and if its a positive
    integer, pulls that many items off the stack and returns them as a list.
    """
    def new_operator_function(stack):
        """
        The wrapped function will have items as well as the
        remaining stack passed in.
        """
        number_of_items = stack.pop()

        if (int(number_of_items) != number_of_items) or number_of_items < 1:
            raise NotPositiveInteger(number_of_items)
        items = []

        for _ in range(number_of_items):
            items.append(stack.pop())

        operator_function(stack, items)
    return new_operator_function
