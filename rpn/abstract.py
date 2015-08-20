from collections import deque

import re

from decimal import Decimal

class AbstractEvaluator:
    operators = {}
    is_number = re.compile(r"[-+]?(\d+(\.\d*)?|\.\d+)([eE][-+]?\d+)?")

    def evaluate_tokens(self, tokens):
        stack = deque()
        for token in tokens:
            if callable(token):
                token(stack)
            else:
                stack.append(token)
        return stack.pop()

    def evaluate(self, expression):
        tokens = self.tokenize(expression)
        return self.evaluate_tokens(tokens)

    def tokenize(self, expression):
        processed_tokens = []
        for token in expression.split():
            if token in self.operators:
                processed_tokens.append(self.operators[token])
            elif self.is_number.match(token):
                processed_tokens.append(Decimal(token))
            else:
                raise ValueError("{} is not a valid operator or number")
        return processed_tokens
