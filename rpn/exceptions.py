from decimal import InvalidOperation


class RPyNError(Exception):
    pass


class BadExpressionError(RPyNError):
    pass


class TooShortBadExpression(BadExpressionError, IndexError):
    pass


class NoneOperatorBadExpression(BadExpressionError, TypeError):
    pass


class RealNumberError(RPyNError):
    pass


class MathDomainError(RealNumberError, ValueError):
    pass


class DivideByZeroError(RealNumberError, InvalidOperation):
    pass


class UnacceptableToken(RPyNError, ValueError):
    pass


class NotPositiveInteger(BadExpressionError):
    pass
