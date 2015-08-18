import unittest

from rpn.abstract import AbstractEvaluator
from slugify import UniqueSlugify


from utils import TemplateTestCase, Call, template

class TestAbstractEvaluator(unittest.TestCase):

    __metaclass__ = TemplateTestCase

    good_parameters = {
        "good_1": Call("1", 1)
    }

    bad_parameters = {
        "bad_1": Call("1", 2)
    }

    error_parameters = {
        "error_1": Call("Cheese", 42)
    }

    evaluator = AbstractEvaluator()

    @template(good_parameters)
    def _test_evaluate_good_expression(self, expression, result):
        """
            Tests evaluation of: {}
        """.format(expression)
        output = self.evaluator.evaluate(expression)
        self.assertEqual(output, result)

    @template(bad_parameters)
    def _test_evaluate_bad_expression(self, expression, result):
        """
            Tests evaluation of: {}
        """.format(expression)
        output = self.evaluator.evaluate(expression)
        self.assertNotEqual(output, result)

    @template(error_parameters)
    def _test_evaluate_error_expression(self, expression, result):
        """
            Tests evaluation of: {}
        """.format(expression)
        self.assertRaises(ValueError, self.evaluator.evaluate, expression=expression)
