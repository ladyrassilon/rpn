from collections import deque

import re

from decimal import Decimal

from exceptions import (BadExpressionError, MathDomainError,
                        DivideByZeroError, UnacceptableToken,
                        TooShortBadExpression,
                        MathDomainError,
                        DivideByZeroError
                        )


class AbstractEvaluator:
    operators = {}
    is_number = re.compile(r"[-+]?(\d+(\.\d*)?|\.\d+)([eE][-+]?\d+)?")

    def _evaluate_tokens(self, tokens):
        stack = deque()
        try:
            for token in tokens:
                if callable(token):
                    token(stack)
                else:
                    stack.append(token)
            return stack.pop()
        except IndexError as e:
            raise TooShortBadExpression(e)
        except ValueError as e:
            raise MathDomainError(e)
        except ZeroDivisionError as e:
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
            elif (
                isinstance(token, int) or
                isinstance(token, float) or
                isinstance(token, Decimal)
            ):
                processed_tokens.append(token)
            elif token is None or token == "None":
                processed_tokens.append(None)
            elif self.is_number.match(token):
                processed_tokens.append(Decimal(token))
            else:
                raise UnacceptableToken(
                    "{} is not a valid operator or number".format(token))
        return processed_tokens
