# Title: Colour Analysis Software

**Assessment Name:** Introduction to Software Engineering (ISAD1000/5004) – ISE Assignment 2025 S1  
**Student Name:** Muhammad Mustafa Ghauri  
**Curtin Student ID:** 21856831  
**Practical Class:** Friday 12:00 PM – 2:00 PM 
**ISE Assignment 2025**

## Overview:

This project covers all the phases of working on a modular colour analysis tool as a software engineering project. Using the application, users can experiment with electromagnetic data enter with colour names, frequencies or wavelengths. As a result, the system gives important information about the colour, categorises it by its spectrum (seen as visible, ultraviolet, infrared) and connects it to musical notes, gemstones and emotions. The examples used in Figures 1 and 2 of the assignment brief formed the basis for these features.

I built the project using Python 3 on Linux and used good modularity principles as I programmed. Modules were each designed separately to have just one clear job, so they can be reused and leveraged as needed. With a command-line interface, interaction is easier and with file-based input, the software is suitable for different types of use.

In addition, the project performs thorough software testing through the use of black-box and white-box approaches. All core modules and edge cases were tested with the `unittest` library. Traceability, teamwork and adherence to software development best practices were achieved by using Git as our version control system.

This assignment produced a working tool while also proving that the student can modularize, review and improve code, test methods systematically and provide needed software documentation—all of which are important in real-life software projects.


## Objectives

The primary objectives of this project are:

- **To design and develop a modular software solution** that adheres to sound principles of software engineering, using clearly defined and reusable functions.
- **To validate the correctness of the code** using structured black-box and white-box testing techniques, ensuring accurate handling of both valid and invalid inputs.
- **To document and manage the development lifecycle** using a version control system (Git) that maintains a traceable history of all changes made across the codebase and associated documents.
- **To generate a detailed markdown report** that outlines the development process, design decisions, testing strategies, and version control insights for the purpose of knowledge transfer and reproducibility.

---

## Repository Structure:

```text
ISErepo/
├── code/
│   ├── colour_analysis.py              # Main CLI program
│   ├── frequency.txt                   # Sample input file (single frequency)
│   ├── frequency_visible.txt           # Visible range frequency (e.g., 600)
│   ├── frequency_ultraviolet.txt       # UV frequency (e.g., 800)
│   ├── frequency_edge_visible.txt      # Boundary frequency (e.g., 790)
│   ├── frequency_outofrange.txt        # Out-of-range frequency (e.g., 31000)
│
├── tests/
│   └── test_colour_analysis.py         # Unit tests using unittest (EP testing)
│
└── README.md                           # Repository overview and usage guide
```

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

