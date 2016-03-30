from rpn.abstract import AbstractEvaluator
from rpn.functions import add, subtract, multiply, divide


class NormalEvaluator(AbstractEvaluator):
    operators = {
        "-": subtract,
        "+": add,
        "*": multiply,
        "/": divide,
    }
