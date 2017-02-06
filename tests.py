import unittest
from primenumbers import prime_numbers
class Prime_tests(unittest.TestCase):

	def test_prime_numbers_list(self):
		self.assertIs(type(prime_numbers(10), list ) )

	def test_prime_numbers_10(self):
		self.assertEqual(prime_numbers(10), [2,3,5,7] )

	def test_prime_numbers_int(self):
	    self.assertTrue(prime_numbers("b", "Try an integer "))

	def test_prime_numbers_zero(self):
	 	self.assertEqual(prime_numbers(0, "Error"))

	def test_prime_numbers_one(self):
		self.assertNotIn(1, prime_numbers(10)) 

	def test_prime_numbers_len(self):
		self.assertTrue(len(prime_numbers(10)<10 )

if __name__ == '__main__ ':
    unittest.main()