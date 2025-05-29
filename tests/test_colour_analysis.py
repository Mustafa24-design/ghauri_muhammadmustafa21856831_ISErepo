# File: test_colour_analysis.py
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../code')))

import unittest
import os
from colour_analysis import (
    get_frequency_range,    
    get_stone,
    get_music_note,
    get_emotion
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
        
    def test_get_stone(self):
        self.assertEqual(get_stone("cyan"), "Turquoise")
        self.assertEqual(get_stone("black"), "Invalid colour")

    def test_get_music_note(self):
        self.assertEqual(get_music_note("red"), "C")
        self.assertEqual(get_music_note("brown"), "Invalid colour")

    def test_get_emotion(self):
        self.assertEqual(get_emotion("orange"), "Happy")
        self.assertEqual(get_emotion("silver"), "Invalid colour")

    
if __name__ == "__main__":
    unittest.main()