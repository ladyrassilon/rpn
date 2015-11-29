from exceptions import NotPositiveInteger


def get_items(operator_function):
    def new_operator_function(stack):
        number_of_items = stack.pop()

        if (int(number_of_items) != number_of_items) or \
            number_of_items < 1:
                raise NotPositiveInteger(number_of_items)
        items = []

        for _ in range(number_of_items):
            items.append(stack.pop())

        operator_function(stack, items)
    return new_operator_function
