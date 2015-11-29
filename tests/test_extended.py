import unittest

from rpn.exceptions import (TooShortBadExpression,
                            UnacceptableToken,
                            DivideByZeroError)

from rpn.extended import ExtendedEvaluator
from .utils import TemplateTestCase, Call, template
from decimal import Decimal
from sympy import symbols
none = symbols("none")

long_list_good = [
    Decimal('30000.00'),
    Decimal('30000.00'),
    u'+',
    Decimal('30000.00'),
    u'+',
    Decimal('30000.00'),
    u'+'
]


class TestExtendedEvaluator(unittest.TestCase):

    __metaclass__ = TemplateTestCase

    evaluator = ExtendedEvaluator()

    good_parameters = {
        "good_if_1": Call('1 27 38 ?', Decimal(27)),
        "good_if_2": Call('0 27 38 ?', Decimal(38)),
        "good_1_item": Call("1", Decimal(1)),
        "good_add": Call("1 2 +", Decimal(3)),
        "good_subtract": Call("1 2 -", Decimal(-1)),
        "good_divide": Call("1 2 /", Decimal(0.5)),
        "good_multiply": Call("1 2 *", Decimal(2)),
        "good_if": Call("1 2 3 ?", Decimal(2)),
        "good_1": Call('32 56 57 - 0.00 ?', Decimal(-1)),
        "good_2": Call('32 71 61 - 0.00 ?', Decimal(10)),
        "good_3": Call('32 100 98 + 0.00 ?', Decimal(198)),
        "good_4": Call('0 50 98 35 ? 0.00 ?', Decimal(0)),
        "good_5": Call('19 160 / 100.00 *', Decimal(11.875)),
        "good_list_1": Call(long_list_good, Decimal(120000.00)),
        "good_list_2": Call(long_list_good[:-1], Decimal(30000.00)),
        "good_exists_1": Call("None 1 2 E", Decimal(2)),
        "good_exists_2": Call([None, 1, 2, "E"], Decimal(2)),
        "good_exists_3": Call("1 1 2 E", Decimal(1)),
        "good_exists_4": Call([1, 1, 2, "E"], Decimal(1)),
        "good_equals_1": Call([2, 2, 5, 10, "="], Decimal(10)),
        "good_equals_2": Call([2, 3, 5, 10, "="], Decimal(5)),
        "good_greater_than_1": Call([2, 3, 5, 10, ">"], Decimal(10)),
        "good_greater_than_2": Call([3, 3, 5, 10, ">"], Decimal(5)),
        "good_greater_than_3": Call([4, 3, 5, 10, ">"], Decimal(5)),
        "good_less_than_1": Call([2, 3, 5, 10, "<"], Decimal(5)),
        "good_less_than_2": Call([3, 3, 5, 10, "<"], Decimal(5)),
        "good_less_than_3": Call([4, 3, 5, 10, "<"], Decimal(10)),
        "good_absolute_1": Call([-4, "A"], Decimal(4)),
        "good_absolute_2": Call([0, "A"], Decimal(0)),
        "good_absolute_3": Call([4, "A"], Decimal(4)),
        "good_negative_1": Call([-4, "N"], Decimal(4)),
        "good_negative_2": Call([0, "N"], Decimal(0)),
        "good_negative_3": Call([4, "N"], Decimal(-4)),
        "good_sum_1": Call([4, 5, 2, "S"], Decimal(9)),
        "good_sum_2": Call([-10, 4, 5, 3, "S"], Decimal(-1)),
        "good_sum_3": Call([-10, 4, 5, 2, "S"], Decimal(9)),
        "good_sum_4": Call([27.5, -10, 4, 5, 2, "S"], Decimal(26.5)),
        #"real_world_good": Call([Decimal(1), Decimal('80000000.00'), Decimal('85000000.00'), u'/', u'-', Decimal('100.00'), u'*'], Decimal(6.25)),
        "real_world_good_2": Call([Decimal(398E5), None, None, Decimal(44169480), '+', Decimal(2E6), 'E', Decimal(0), '?'], Decimal(2E6))
    }

    bad_parameters = {
        "bad_1_item": Call("1", Decimal(2)),
        "bad_add": Call("1 2 +", Decimal(2)),
        "bad_subtract": Call("1 2 -", Decimal(2)),
        "bad_divide": Call("1 2 /", Decimal(2)),
        "bad_multiply": Call("1 2 *", Decimal(0.5)),
        "bad_if": Call("1 2 3 ?", Decimal(3)),
        "bad_exists_1": Call("None 1 2 E", Decimal(1)),
        "bad_exists_2": Call([None, 1, 2, "E"], Decimal(1)),
        "bad_exists_3": Call("1 1 2 E", Decimal(2)),
        "bad_exists_4": Call([1, 1, 2, "E"], Decimal(2)),
        "bad_equals_1": Call([5, 10, 2, 2, "="], Decimal(5)),
        "bad_equals_2": Call([5, 10, 2, 3, "="], Decimal(10)),
        "bad_greater_than_1": Call([2, 3, 5, 10, ">"], Decimal(5)),
        "bad_greater_than_2": Call([3, 3, 5, 10, ">"], Decimal(10)),
        "bad_greater_than_3": Call([4, 3, 5, 10, ">"], Decimal(10)),
        "bad_less_than_1": Call([2, 3, 5, 10, "<"], Decimal(10)),
        "bad_less_than_2": Call([3, 3, 5, 10, "<"], Decimal(10)),
        "bad_less_than_3": Call([4, 3, 5, 10, "<"], Decimal(5)),
        "bad_absolute_1": Call([-4, "A"], Decimal(-4)),
        "bad_absolute_2": Call([0, "A"], Decimal(4)),
        "bad_absolute_3": Call([4, "A"], Decimal(-4)),
        "bad_negative_1": Call([-4, "N"], Decimal(-4)),
        "bad_negative_2": Call([0, "N"], Decimal(-4)),
        "bad_negative_3": Call([4, "N"], Decimal(4)),
        "bad_sum_1": Call([4, 5, 2, "S"], Decimal(10)),
        "bad_sum_2": Call([-10, 4, 5, 3, "S"], Decimal(-3)),
        "bad_sum_3": Call([-10, 4, 5, 2, "S"], Decimal(-1)),
        "bad_sum_4": Call([27.5, -10, 4, 5, 2, "S"], Decimal(0)),
    }

    error_parameters = {
        "error_cheese": Call("Cheese", UnacceptableToken),
        "error_empty_1": Call("", TooShortBadExpression),
        "error_empty_2": Call([], TooShortBadExpression),
        "error_add_one_number_1": Call("1 +", TooShortBadExpression),
        "error_add_one_number_2": Call("1 +", TooShortBadExpression),
        "illegal_char": Call("1 2 3 K", UnacceptableToken),
        "divide_by_zero_1": Call("1 0 /", DivideByZeroError),
        "divide_by_zero_2": Call([Decimal(1), Decimal(0), "/"], DivideByZeroError),
        "too_many_sum_parameters": Call([1, 2, 3, "S"], TooShortBadExpression)
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
