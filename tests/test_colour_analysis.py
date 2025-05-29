# File: test_colour_analysis.py
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../code')))

import unittest
import os
from colour_analysis import (
    get_frequency_range,
)

class TestColourAnalysis(unittest.TestCase):
    """Unit tests for colour_analysis module."""

    # -----------------------
    # Black-Box: Equivalence Partitioning (EP)
    # -----------------------

    def test_get_frequency_range_valid(self):
        self.assertEqual(get_frequency_range("green"), (530, 599))

    def test_get_frequency_range_invalid(self):
        self.assertIsNone(get_frequency_range("pink"))


    
if __name__ == "__main__":
    unittest.main()

