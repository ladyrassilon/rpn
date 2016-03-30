# pylint: disable=too-many-ancestors
from decimal import InvalidOperation


class RPyNError(Exception):
    """
    Abstract RPyN error that all errors inherit from.
    """
    pass


class BadExpressionError(RPyNError):
    """
    Abstract expression specifying faulty expressions.
    """
    pass


class TooShortBadExpression(BadExpressionError, IndexError):
    """
    The operator calls for more items than are available on the stack.
    """
    pass


class NoneOperatorBadExpression(BadExpressionError, TypeError):
    """
    Trying to do an operation on an item that is none, when the
    operator doesn't support an operator at that point.
    """
    pass


class RealNumberError(RPyNError):
    """
    Abstract error describing some situation where a number outside the real
    plane is being dealt with.
    """
    pass


class MathDomainError(RealNumberError, ValueError):
    """
    The number cannot be represented in the real plane (for example "i")
    """
    pass


class DivideByZeroError(RealNumberError, InvalidOperation): # pylint: disable=too-many-ancestors
    """
    A number divided by zero has occured.
    """
    pass


class UnacceptableToken(RPyNError, ValueError):
    """
    The token specified, is not supported by the evaluator.
    """
    pass


class NotPositiveInteger(BadExpressionError):
    """
    The operator called for a positive integer, but one was not supplied.
    """
    pass
