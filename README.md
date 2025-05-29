# ghauri_muhammadmustafa21856831_ISErepo

## Title: Colour Analysis Software
**ISE Assignment 2025**

## Overview:
This project implements a modular Python application for analysing electromagnetic (EM) spectrum frequencies and associating them with visible light colours, gemstones, musical notes, and emotions. The program is designed using clean modular code principles and follows a **test-driven development** approach with **version control** via GitHub.

## Repository Structure:
ISErepo/
├── code/
│ ├── colour_analysis.py # Main CLI program
│ ├── frequency.txt # Sample input file (single frequency)
│ ├── frequency_visible.txt # Visible range frequency (e.g., 600)
│ ├── frequency_ultraviolet.txt # UV frequency (e.g., 800)
│ ├── frequency_edge_visible.txt # Boundary frequency (e.g., 790)
│ ├── frequency_outofrange.txt # Out-of-range frequency (e.g., 31000)
│
├── tests/
│ └── test_colour_analysis.py # Unit tests using unittest (EP testing)
│
└── README.md # Repository overview and usage guide


## Key Features
- Converts frequency to wavelength and vice versa.
- Identifies colours from THz frequency values.
- Categorizes input into spectral ranges: Visible, Infrared, Ultraviolet.
- Provides mappings of colours to:
  - Gemstones (e.g., violet → Amethyst)
  - Musical notes (e.g., blue → A)
  - Emotions (e.g., yellow → Happy)
- Command-line interface with both manual input and file-based operations.
- Modular programming structure and test-driven development.

## Unit Testing (Version 1)
Unit testing is implemented using the `unittest` framework with a focus on Equivalence Partitioning (EP). Test cases include:
- Valid input case: e.g., "green"
- Invalid input case: e.g., "pink"

To execute the test suite:
```bash
python -m unittest discover -s tests

