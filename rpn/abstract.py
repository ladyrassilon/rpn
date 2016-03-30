from collections import deque

import re

from decimal import Decimal, InvalidOperation

from .exceptions import (UnacceptableToken,
                         TooShortBadExpression,
                         MathDomainError,
                         DivideByZeroError,
                         NoneOperatorBadExpression)

from sympy import symbols
from sympy.core.symbol import Symbol
from sympy.core.expr import Expr


class AbstractEvaluator:
    """
    Base evaluator, that when implemented you can add operators to.

    Override operators dictionary.
    """
    operators = {}
    none = symbols("none")
    is_number = re.compile(r"[-+]?(\d+(\.\d*)?|\.\d+)([eE][-+]?\d+)?")

    def _evaluate_tokens(self, tokens):
        """
        Pass in a list of tokens and process them through the specified
        operators.
        """
        stack = deque()
        try:
            for token in tokens:
                if callable(token) and not type(token) == Symbol:
                    token(stack)
                else:
                    stack.append(token)
            result = stack.pop()
            if isinstance(result, Expr):
                if result == self.none:
                    return None
                raise NoneOperatorBadExpression(
                    "{} is invalid expression".format(result))
            return result
        except TypeError as err:
            raise NoneOperatorBadExpression(err)
        except IndexError as err:
            raise TooShortBadExpression(err)
        except ValueError as err:
            raise MathDomainError(err)
        except (ZeroDivisionError, InvalidOperation) as err:
            raise DivideByZeroError(err)

    def evaluate(self, expression):
        """
        Pass a list or string of numbers and operators in reverse polish
        notation.
        """
        if isinstance(expression, str) or isinstance(expression, unicode):
            tokens = self._tokenize(expression.split())
        else:
            tokens = self._tokenize(expression)
        return self._evaluate_tokens(tokens)

    def _tokenize(self, expression):
        processed_tokens = []

        for token in expression:
            if token in self.operators:
                processed_tokens.append(self.operators[token])
            elif isinstance(token, int) or isinstance(token, float):
                processed_tokens.append(Decimal(token))
            elif isinstance(token, Decimal):
                processed_tokens.append(token)
            elif token is None or token == "None":
                processed_tokens.append(self.none)
            elif self.is_number.match(token):
                processed_tokens.append(Decimal(token))
            else:
                raise UnacceptableToken(
                    "{} is not a valid operator or number".format(token))
        return processed_tokens
