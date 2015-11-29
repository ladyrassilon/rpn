from exceptions import NotPositiveInteger


def get_number_of_items(operator_function):
    def new_operator_function(stack):
        number_of_items_in_list = stack.pop()
        if (int(number_of_items_in_list) != number_of_items_in_list) or \
            number_of_items_in_list < 1:
                raise NotPositiveInteger(number_of_items_in_list)
        operator_function(stack, number_of_items_in_list)
    return new_operator_function
