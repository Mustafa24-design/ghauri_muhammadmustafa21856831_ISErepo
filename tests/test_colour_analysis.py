# File: test_colour_analysis.py
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../code')))

import unittest
import os
from colour_analysis import (
    get_frequency_range,
    frequency_to_wavelength,
    wavelength_to_frequency,
    get_spectrum_range,
    frequency_to_colour,
    compare_frequencies,
    get_stone,
    get_music_note,
    get_emotion,
    read_frequency_from_file
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

    # -----------------------
    # Black-Box: Boundary Value Analysis (BVA)
    # -----------------------

    def test_get_spectrum_range_boundaries(self):
        self.assertEqual(get_spectrum_range(400), "Visible")
        self.assertEqual(get_spectrum_range(790), "Visible")
        self.assertEqual(get_spectrum_range(399), "Infrared")
        self.assertEqual(get_spectrum_range(791), "Ultraviolet")
        self.assertEqual(get_spectrum_range(0), "Out of Range")
        self.assertEqual(get_spectrum_range(45000), "Out of Range")

    # -----------------------
    # White-Box: frequency_to_colour logic (loop + if-else)
    # -----------------------

    def test_frequency_to_colour_visible(self):
        self.assertEqual(frequency_to_colour(600), "cyan")

    def test_frequency_to_colour_outside_range(self):
        self.assertEqual(frequency_to_colour(350), "Below Red (Infrared)")
        self.assertEqual(frequency_to_colour(850), "Above Violet (Ultraviolet)")
        self.assertEqual(frequency_to_colour(45000), "Above Violet (Ultraviolet)")

    # -----------------------
    # White-Box: compare_frequencies logic (conditional)
    # -----------------------

    def test_compare_same_colour(self):
        self.assertIn("same colour", compare_frequencies(670, 680).lower())

    def test_compare_different_colours(self):
        self.assertIn("different colours", compare_frequencies(420, 650).lower())

    def test_compare_with_nonvisible(self):
        self.assertIn("outside the visible range", compare_frequencies(200, 850).lower())

    # -----------------------
    # Utility Conversions
    # -----------------------

    def test_frequency_to_wavelength(self):
        self.assertEqual(frequency_to_wavelength(600), 500.0)

    def test_wavelength_to_frequency(self):
        self.assertEqual(wavelength_to_frequency(500), 600.0)

    # -----------------------
    # File-based Input
    # -----------------------

    def test_read_frequency_from_file(self):
        filename = "test_input.txt"
        with open(filename, "w") as f:
            f.write("675\n")
        result = read_frequency_from_file(filename)
        os.remove(filename)
        self.assertEqual(result, 675)

    def test_file_with_multiple_lines(self):
        filename = "multi_line.txt"
        with open(filename, "w") as f:
            f.write("600\n450\n700\n")
        result = read_frequency_from_file(filename)
        os.remove(filename)
        self.assertEqual(result, 600)  # Only the first line should be read

    # -----------------------
    # Student ID / Last Name Test (Assignment Requirement)
    # -----------------------

    def test_student_identifier_data(self):
        # Assume last name: Mustafa, ID ends in 831
        self.assertEqual(get_emotion("Mustafa"), "Invalid colour")  # last name
        self.assertEqual(get_spectrum_range(831), "Ultraviolet")  # student ID digits

if __name__ == "__main__":
    unittest.main()

