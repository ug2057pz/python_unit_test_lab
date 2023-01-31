import unittest 
from unittest import TestCase
from price_discount import discount  

class TestDiscount(TestCase):

    def test_list_of_three_prices(self):
        prices = [10, 4, 20]
        expected_discount = 4
        self.assertEqual(expected_discount, discount(prices))

    
    # TODO more unit tests here. Each test should test one scenario

    def test_discount_less_than_three(self):

        """Test that discount returns the correct price when there are less than three items"""

        prices = [10,20]
        expected_discount = 4
        self.assertEqual(expected_discount, discount(prices))

    def test_discount_more_than_three(self):

        """Test that discount returns the correct price when there are four items"""

        prices = [10, 4,25,20]
        expected_discount = 4
        self.assertEqual(expected_discount, discount(prices))
        


if __name__ == '__main__':
    unittest.main()