from .abstract import AbstractEvaluator
from .functions import add, subtract, multiply, divide, if_, exists, equals,\
    greater_than, less_than


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
    }
