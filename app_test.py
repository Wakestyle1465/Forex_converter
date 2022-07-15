from unittest import TestCase
from app import app
from forex_python.converter import CurrencyRates, CurrencyCodes

class TestForex(TestCase):
    def test_conv(self):
        self.assertAlmostEqual()

# Comments
# I wasnt sure how to write a test for a function that is a part of the page?
# The way I would have run the tests was by making sure that the conversion_rate worked and the result would have worked. Multiplying the amount by the conversion. Just wasnt too sure how to write a test for a function that doesnt exist. Or run a function on the click of the button.