from decimal import InvalidOperation


class RPyNError(Exception):
    pass


class BadExpressionError(RPyNError, IndexError):
    pass


class TooShortBadExpression(BadExpressionError):
    pass


class RealNumberError(RPyNError):
    pass


class MathDomainError(RealNumberError, ValueError):
    pass


class DivideByZeroError(RealNumberError, InvalidOperation):
    pass


class UnacceptableToken(RPyNError, ValueError):
    pass
