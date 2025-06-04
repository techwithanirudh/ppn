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

    def test_cli_million_runs(self):
        """Ensure the CLI works without the --count flag for one million."""
        import subprocess, sys
        result = subprocess.run(
            [sys.executable, "prime_sieve.py", "1000000"],
            stdout=subprocess.PIPE,
            check=True,
            text=True,
        )
        # ensure output ends with the last prime below one million
        self.assertTrue(result.stdout.strip().endswith("999983"))

if __name__ == '__main__':
    unittest.main()
