import unittest

from rpn.normal import NormalEvaluator
from slugify import UniqueSlugify


from utils import TemplateTestCase, Call, template

class TestNormalEvaluator(unittest.TestCase):

    __metaclass__ = TemplateTestCase

    evaluator = NormalEvaluator()

    good_parameters = {
        "good_1": Call("28 65 / 100.00 *", 43.07692307692308),
        "good_2": Call("4 5 7 2 + - *", -16),
        "good_3": Call("3 4 + 2  * 7 /", 2),
        "good_4": Call("5 7 + 6 2 -  *", 48),
        "good_5": Call("4 2 3 5 1 - + * +", 18),
        "good_6": Call("4 2 + 3 5 1 -  * +", 18),
    }

    bad_parameters = {
        "bad_1_item": Call("1", 2),
        "bad_add": Call("1 2 +", 2),
        "bad_subtract": Call("1 2 -", 2),
        "bad_divide": Call("1 2 /", 2),
        "bad_multiply": Call("1 2 *", 0.5),
    }

    error_parameters = {
        "error_cheese": Call("Cheese", ValueError),
        "error_empty": Call("", IndexError),
        "error_add_one_number": Call("1 +", IndexError),
        "illegal_char": Call("1 2 3 ?", ValueError)
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
        self.assertRaises(error, self.evaluator.evaluate, expression=expression)
