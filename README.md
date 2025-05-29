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

## Module Descriptions

This section details how the original colour analysis module was divided into different tasks. All the modules were made according to the principles of modularity which stress high cohesion, low coupling, reuse, being clear and being tested. The design allows modules to be both used interactively and tested with automated methods.

---

### 1. `get_frequency_range(colour)`
- **Purpose:** Returns the frequency range (in THz) for a specified visible colour.
- **Inputs:** `colour` (string)
- **Outputs:** Tuple of lower and upper frequency bounds (e.g., `(530, 599)`) or `None` if invalid.
- **Input Method:** Parameter passing
- **Output Method:** Return value
- **Justification:** Essential for retrieving frequency ranges for valid colour names. Modular design allows isolation and reuse in multiple contexts, including test automation.

![Screenshot: Get frequency range for a colour](screenshots/Get%20frequency%20range%20for%20a%20colour.png)

*Figure 1: Output showing the frequency range for the colour 'green'.*

---

### 2. `frequency_to_wavelength(frequency_thz)`
- **Purpose:** Converts frequency (THz) to wavelength (nm) using the formula:  
  _wavelength (nm) = (3 × 10⁸ m/s) / (frequency × 10¹² Hz)_ → simplified to _300000 / frequency_
- **Inputs:** `frequency_thz` (float)
- **Outputs:** Wavelength in nanometres (float)
- **Input Method:** Parameter passing
- **Output Method:** Return value
- **Justification:** Physics-driven calculation needed for interpretation and translation of EM spectrum data.

![Function: Frequency to Wavelength](screenshots/Figure2.png) 

*Figure 2: `frequency_to_wavelength()` function and CLI output for 500 THz → 600.0 nm.*

---

### 3. `wavelength_to_frequency(wavelength_nm)`
- **Purpose:** Converts wavelength (nm) to frequency (THz).
- **Inputs:** `wavelength_nm` (float)
- **Outputs:** Frequency in THz (float)
- **Input Method:** Parameter passing
- **Output Method:** Return value
- **Justification:** Inverse operation of the previous module. Separated to respect the Single Responsibility Principle.

![Function: Convert wavelength to frequency](screenshots/Figure3.png)  

*Figure 3: wavelength_to_frequency()` function and CLI output for 500 nm → 600.0 THz.*

---

### 4. `get_spectrum_range(frequency_thz)`
- **Purpose:** Categorizes the input frequency into spectral ranges: `Infrared`, `Visible`, `Ultraviolet`, or `Out of Range`.
- **Inputs:** `frequency_thz` (float)
- **Outputs:** Category name (string)
- **Input Method:** Parameter passing
- **Output Method:** Return value
- **Justification:** Encapsulates logic for EM classification. Critical for validation and messaging.

![Function: Check spectral range](screenshots/Figure4.png)  

*Figure 4: `get_spectrum_range()` classification logic.*

---

### 5. `frequency_to_colour(frequency_thz)`
- **Purpose:** Maps a given frequency to its associated colour name if within the visible range. If outside, returns a contextual message.
- **Inputs:** `frequency_thz` (float)
- **Outputs:** Colour name or category message (string)
- **Input Method:** Parameter passing
- **Output Method:** Return value
- **Justification:** Central module of the application. Supports both analytical and user-facing functionality.
- 
![Function: Conversion of Frequency to Colour](screenshots/Figure5.png)  

*Figure 5: Function and Output: Conversion of Frequency to Colour*

---

### 6. `compare_frequencies(freq1, freq2)`
- **Purpose:** Compares two frequencies and determines if they map to the same colour, different colours, or are outside the visible range.
- **Inputs:** `freq1`, `freq2` (float)
- **Outputs:** Human-readable comparison message (string)
- **Input Method:** Parameter passing
- **Output Method:** Return value
- **Justification:** Provides comparative analysis logic, improving UX by handling edge and invalid cases robustly.

![Function: Comparing two Frequencies](screenshots/Figure6.png)  

*Figure 6: Function and Output: Comparing two Frequencies*

---

### 7. `get_stone(colour)`
- **Purpose:** Returns the gemstone linked to a valid colour.
- **Inputs:** `colour` (string)
- **Outputs:** Gemstone (string)
- **Input Method:** Parameter passing
- **Output Method:** Return value
- **Justification:** Implements factual mapping (from Figure 2) while supporting fun/educational use cases.

![Function: Get Stone Associated with a Colour](screenshots/Figure7.png)  

*Figure 7: Function and Output: Get Stone Associated with a Colour*

---

### 8. `get_music_note(colour)`
- **Purpose:** Returns the musical note associated with a colour.
- **Inputs:** `colour` (string)
- **Outputs:** Note (string)
- **Input Method:** Parameter passing
- **Output Method:** Return value
- **Justification:** Analogous to `get_stone()`, enriches the application with cross-disciplinary insight.

![Function: Get Music Note Associated with a Colour](screenshots/Figure8.png)  

*Figure 8: Function and Output: Get Music Note Associated with a Colour*

---

### 9. `get_emotion(colour)`
- **Purpose:** Returns the emotion associated with a given colour.
- **Inputs:** `colour` (string)
- **Outputs:** Emotion (string)
- **Input Method:** Parameter passing
- **Output Method:** Return value
- **Justification:** Provides emotional context, enhancing the user experience through psychological dimensions.

![Function: Get Emotion Associated with a Colour](screenshots/Figure9.png)  

*Figure 9: Function and Output: Get Emotion Associated with a Colour*

---

### 10. `read_frequency_from_file(filename)`
- **Purpose:** Reads a frequency value from the first line of a given text file.
- **Inputs:** `filename` (string)
- **Outputs:** Frequency (integer)
- **Input Method:** File input
- **Output Method:** Return value
- **Justification:** Enables file-based input testing and automation. Especially useful for batch processing.

![Function: Reading Data from Files](screenshots/Figure10.png)  

*Figure 10: Function and Output: Example of Reading Data from Files*

---

## Design Decisions and Assumptions

The modularization strategy was guided by the following design principles:

- **Single Responsibility Principle:** Each function handles a narrowly defined task.
- **Loose Coupling:** Minimal interdependencies between modules allow for isolated testing.
- **High Cohesion:** Modules focus exclusively on one conceptual task (e.g., conversion, lookup, classification).
- **Testability:** Functions are parameter-driven, facilitating clean unit tests without the need for mocking global state.

**Assumptions Made:**
- Only colour names listed in Figures 1 and 2 are considered valid.
- Frequency values are restricted to the range 1–40,000 THz, as per the assignment brief.
- File-based inputs will always contain an integer on the first line and be accessible at runtime.
- Edge values (e.g., 400 THz, 790 THz) fall inclusively within the visible range.

This decomposition enables future scalability (e.g., extending to RGB codes, audio outputs, web integration) while maintaining strong internal structure.

---

