from .abstract import AbstractEvaluator
from .functions import add, subtract, multiply, divide, if_, exists, equals,\
    greater_than, less_than, absolute, negative, sum_list, mean_list


class ExtendedEvaluator(AbstractEvaluator):
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
        "-": mean_list,
    }
