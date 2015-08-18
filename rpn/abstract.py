from collections import deque


from operator import add, sub, or_, mul, div

import re

class AbstractEvaluator:
	operators = {}
	is_number = re.compile(r"[-+]?(\d+(\.\d*)?|\.\d+)([eE][-+]?\d+)?")
	def __init__(self, *args, **kwargs):
		super(AbstractEvaluator, self).__init__(*args, **kwargs)
		self.stack = deque()
	
	def evaluate(self, expression):
		tokens = self.tokenize(expression)
		for token in tokens:
			if type(token) == builtin_function_or_method:
				token(self.stack)
			else:
				self.stack.append(token)
		return stack.pop()			


	def tokenize(self, expression):
		processed_tokens = []
		for token in expression.split():
			if token in self.operators:
				processed_tokens.append(self.operators[token])
			elif is_number.match(token):
				processed_tokens.append(float(token))
			else:
				raise ValueError("{} is not a valid operator or number")
		return processed_tokens
