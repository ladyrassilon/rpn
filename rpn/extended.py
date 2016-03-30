# pylint: disable=too-few-public-methods
from rpn.abstract import AbstractEvaluator
from rpn.functions import add, subtract, multiply, divide, if_, exists, equals,\
    greater_than, less_than, absolute, negative, sum_list, mean_list,\
    median_list


class ExtendedEvaluator(AbstractEvaluator):
    """
    Evaluator with an expanded set of operations
    """
    operators = {
        "-": subtract,
        "+": add,
        "*": multiply,
        "/": divide,
        "?": if_,
        "E": exists,
        "=": equals,
        ">": greater_than,
        "<": less_than,
        "A": absolute,
        "N": negative,
        "S": sum_list,
        "_": mean_list,
        "|": median_list,
    }
