import unittest

from rpn.abstract import AbstractEvaluator
from .utils import TemplateTestCase, Call, template
from decimal import Decimal

class TestAbstractEvaluator(unittest.TestCase):

    __metaclass__ = TemplateTestCase

    good_parameters = {
        "good_1": Call("1", Decimal(1)),
        "good_list_1": Call([Decimal(3)], 3),
        "good_list_3": Call([Decimal(1), Decimal(7)], 7),
        "good_none_1": Call([None], None),
        "good_none_2": Call("None", None),
    }

    bad_parameters = {
        "bad_1_item": Call("1", Decimal(2)),
        "bad_2_items": Call("1 2", Decimal(1)),
    }

    error_parameters = {
        "error_cheese": Call("Cheese", ValueError)
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
    def _test_evaluate_error_expression(self, expression, error):
        """
            Tests evaluation of: {}
        """.format(expression)
        self.assertRaises(
            error, self.evaluator.evaluate, expression=expression)
