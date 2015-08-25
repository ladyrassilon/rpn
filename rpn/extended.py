from .abstract import AbstractEvaluator
from .functions import add, subtract, multiply, divide, if_, exists


class ExtendedEvaluator(AbstractEvaluator):
    operators = {
        "-": subtract,
        "+": add,
        "*": multiply,
        "/": divide,
        "?": if_,
        "E": exists,
    }
