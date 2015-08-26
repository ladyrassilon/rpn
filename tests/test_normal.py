import unittest

from rpn.normal import NormalEvaluator
from rpn.exceptions import (TooShortBadExpression,
                            UnacceptableToken,
                            DivideByZeroError)
from utils import TemplateTestCase, Call, template
from decimal import Decimal

acc_dec = Decimal('43.07692307692307692307692308')

long_list_good = [
    Decimal('30000.00'),
    Decimal('30000.00'),
    u'+',
    Decimal('30000.00'),
    u'+',
    Decimal('30000.00'),
    u'+'
]


class TestNormalEvaluator(unittest.TestCase):

    __metaclass__ = TemplateTestCase

    evaluator = NormalEvaluator()

    good_parameters = {
        "good_1_item": Call("1", Decimal(1)),
        "good_add": Call("1 2 +", Decimal(3)),
        "good_subtract": Call("1 2 -", Decimal(-1)),
        "good_divide": Call("1 2 /", Decimal(0.5)),
        "good_multiply": Call("1 2 *", Decimal(2)),
        "good_1": Call("28.0 65.0 / 100.00 *", acc_dec),
        "good_2": Call("4 5 7 2 + - *", Decimal(-16)),
        "good_3": Call("3 4 + 2  * 7 /", Decimal(2)),
        "good_4": Call("5 7 + 6 2 -  *", Decimal(48)),
        "good_5": Call("4 2 3 5 1 - + * +", Decimal(18)),
        "good_6": Call("4 2 + 3 5 1 -  * +", Decimal(18)),
        "good_list_1": Call(long_list_good, Decimal(120000.00)),
        "good_list_2": Call(long_list_good[:-1], Decimal(30000.00)),
    }

    bad_parameters = {
        "bad_1_item": Call("1", Decimal(2)),
        "bad_add": Call("1 2 +", Decimal(2)),
        "bad_subtract": Call("1 2 -", Decimal(2)),
        "bad_divide": Call("1 2 /", Decimal(2)),
        "bad_multiply": Call("1 2 *", Decimal(0.5)),
    }

    error_parameters = {
        "error_cheese": Call("Cheese", UnacceptableToken),
        "error_empty_1": Call("", TooShortBadExpression),
        "error_empty_2": Call([], TooShortBadExpression),
        "error_add_one_number_1": Call("1 +", TooShortBadExpression),
        "error_add_one_number_2": Call("1 +", TooShortBadExpression),
        "illegal_char": Call("1 2 3 K", UnacceptableToken),
        # "add_add":
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
