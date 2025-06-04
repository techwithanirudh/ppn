import unittest
from prime_sieve import segmented_sieve

class PrimeSieveTests(unittest.TestCase):
    def test_small_list(self):
        self.assertEqual(list(segmented_sieve(30)), [2,3,5,7,11,13,17,19,23,29])

    def test_small_count(self):
        count = sum(1 for _ in segmented_sieve(100))
        self.assertEqual(count, 25)

    def test_million_count(self):
        count = sum(1 for _ in segmented_sieve(1_000_000))
        self.assertEqual(count, 78498)

if __name__ == '__main__':
    unittest.main()
