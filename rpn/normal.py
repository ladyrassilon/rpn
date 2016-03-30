# pylint: disable=too-few-public-methods
from rpn.abstract import AbstractEvaluator
from rpn.functions import add, subtract, multiply, divide


class NormalEvaluator(AbstractEvaluator):
    """
    Provides the standard set of operators for 
    reverse polish notation.
    """
    operators = {
        "-": subtract,
        "+": add,
        "*": multiply,
        "/": divide,
    }
