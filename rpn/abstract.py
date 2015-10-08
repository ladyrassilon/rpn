from collections import deque

import re

from decimal import Decimal, InvalidOperation

from .exceptions import (BadExpressionError, MathDomainError,
                         DivideByZeroError, UnacceptableToken,
                         TooShortBadExpression,
                         MathDomainError,
                         DivideByZeroError,
                         NoneOperatorBadExpression)

from sympy import symbols
from sympy.core.symbol import Symbol as SymPySymbol
none = symbols("none")

class AbstractEvaluator:
    operators = {}
    is_number = re.compile(r"[-+]?(\d+(\.\d*)?|\.\d+)([eE][-+]?\d+)?")

    def _evaluate_tokens(self, tokens):
        stack = deque()
        try:
            for token in tokens:
                if callable(token) and not type(token) == SymPySymbol:
                    token(stack)
                else:
                    stack.append(token)
            result = stack.pop()
            if type(result) == SymPySymbol:
                raise NoneOperatorBadExpression("{} is invalid exception".format(result))
            return result
        except TypeError as e:
            raise NoneOperatorBadExpression(e)
        except IndexError as e:
            raise TooShortBadExpression(e)
        except ValueError as e:
            raise MathDomainError(e)
        except (ZeroDivisionError, InvalidOperation) as e:
            raise DivideByZeroError(e)

    def evaluate(self, expression):
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
                processed_tokens.append(none)
            elif self.is_number.match(token):
                processed_tokens.append(Decimal(token))
            else:
                raise UnacceptableToken(
                    "{} is not a valid operator or number".format(token))
        return processed_tokens
