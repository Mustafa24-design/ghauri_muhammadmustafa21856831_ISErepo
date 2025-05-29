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

---

## Objectives

The primary objectives of this project are:

- **To design and develop a modular software solution** that adheres to sound principles of software engineering, using clearly defined and reusable functions.
- **To validate the correctness of the code** using structured black-box and white-box testing techniques, ensuring accurate handling of both valid and invalid inputs.
- **To document and manage the development lifecycle** using a version control system (Git) that maintains a traceable history of all changes made across the codebase and associated documents.
- **To generate a detailed markdown report** that outlines the development process, design decisions, testing strategies, and version control insights for the purpose of knowledge transfer and reproducibility.

---

## Repository Structure:
Repositories are kept simple and tidy, placing source code, scripts for tests, documentation material and example data into their own folders. This structure ensures maintainability, ease of navigation, and scalability for future enhancements.

```text
ISErepo/
├── code/
│   ├── colour_analysis.py              # Main CLI program implementing modular colour analysis
│   ├── frequency.txt                   # Sample input file with a single frequency value
│   ├── frequency_visible.txt           # Sample file containing a visible range frequency (e.g., 600 THz)
│   ├── frequency_ultraviolet.txt       # Sample file with ultraviolet frequency (e.g., 800 THz)
│   ├── frequency_edge_visible.txt      # File with boundary frequency (e.g., 790 THz)
│   ├── frequency_outofrange.txt        # File containing an out-of-range frequency (e.g., 31000 THz)
│
├── tests/
│   └── test_colour_analysis.py         # Unit tests using Python's unittest framework for all modules
│
├── documents/
│   └── MuhammadMustafa_21856831_ISEReport.pdf            # PDF version of the final assessment report
│
├── screenshots/
│   └── *.png                           # Screenshots capturing version control logs and test execution
│
└── README.md                           # Markdown report documenting the assessment work and outcomes
```
---

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

---
