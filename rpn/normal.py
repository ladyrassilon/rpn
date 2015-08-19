from .abstract import AbstractEvaluator
from .functions import add, subtract, multiply, divide


class NormalEvaluator(AbstractEvaluator):
    operators = {
        "-": subtract,
        "+": add,
        "*": multiply,
        "/": divide,
    }
