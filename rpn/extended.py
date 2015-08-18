from .abstract import AbstractEvaluator
from .functions import add, subtract, multiply, divide, if_

class ExtendedEvaluator(AbstractEvaluator):
    operators = {
        "-": subtract,
        "+": add,
        "*": multiply,
        "/": divide,
        "?": if_,
    }