import unittest

from rpn.extended import ExtendedEvaluator
from slugify import UniqueSlugify


from utils import TemplateTestCase, Call, template


class TestExtendedEvaluator(unittest.TestCase):

    __metaclass__ = TemplateTestCase

    evaluator = ExtendedEvaluator()

    good_parameters = {
        "good_1": Call('32 56 56 - 0.00 ?', 1),
        "good_2": Call('32 61 61 - 0.00 ?', 1),
        "good_3": Call('32 100 98 + 0.00 ?', 1),
        "good_4": Call('50 98 35 ? 0.00 ?', 1),
        "good_5": Call('160 160 160 / - 1.00 * 100.00 0.00 ?', 1),
        "good_6": Call('160 18 18 18 / 1.00 - 100.00 * 0.00 ? 0.00 ?', 1),
        "good_7": Call('19 160 / 100.00 *', 11.875),
        "good_8": Call('160 19 19 19 / 1.00 - 100.00 * 0.00 ? 0.00 ?', 1),
    }

    bad_parameters = {
        "bad_1": Call("1", 2)
    }

    error_parameters = {
        "error_1": Call("Cheese", 42)
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
    def _test_evaluate_error_expression(self, expression, result):
        """
            Tests evaluation of: {}
        """.format(expression)
        self.assertRaises(ValueError, self.evaluator.evaluate, expression=expression)
