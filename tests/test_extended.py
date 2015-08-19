import unittest

from rpn.extended import ExtendedEvaluator
from utils import TemplateTestCase, Call, template


class TestExtendedEvaluator(unittest.TestCase):

    __metaclass__ = TemplateTestCase

    evaluator = ExtendedEvaluator()

    good_parameters = {
        "good_if_1": Call('1 27 38 ?', 27),
        "good_if_2": Call('0 27 38 ?', 38),
        "good_1_item": Call("1", 1),
        "good_add": Call("1 2 +", 3),
        "good_subtract": Call("1 2 -", -1),
        "good_divide": Call("1 2 /", 0.5),
        "good_multiply": Call("1 2 *", 2),
        "good_if": Call("1 2 3 ?", 2),
        "good_1": Call('32 56 57 - 0.00 ?', -1),
        "good_2": Call('32 71 61 - 0.00 ?', 10),
        "good_3": Call('32 100 98 + 0.00 ?', 198),
        "good_4": Call('0 50 98 35 ? 0.00 ?', 0),
        "good_5": Call('19 160 / 100.00 *', 11.875),
    }

    bad_parameters = {
        "bad_1_item": Call("1", 2),
        "bad_add": Call("1 2 +", 2),
        "bad_subtract": Call("1 2 -", 2),
        "bad_divide": Call("1 2 /", 2),
        "bad_multiply": Call("1 2 *", 0.5),
        "bad_if": Call("1 2 3 ?", 3),
    }

    error_parameters = {
        "error_cheese": Call("Cheese", ValueError),
        "error_empty": Call("", IndexError),
        "error_add_one_number": Call("1 +", IndexError),
        "error_if_not_enough_vars": Call("1 2 ?", IndexError),
    }

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
