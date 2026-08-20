# Text Statistics Analyzer

## Problem Statement
Developing a reliable utility to parse raw text and provide key statistical insights. Manually calculating word counts, sentence structures, and unique term frequencies is inefficient for large volumes of data.

## Objective
To build a functional Python application that automates the generation of text metrics, including:
- Character count
- Word count
- Sentence count
- Unique term count
- Top word frequencies

## Features
- **Flexible Input:** Supports both manual keyboard input and reading from local text files.
- **Robust Validation:** Includes error handling for empty inputs and missing files.
- **Data Normalization:** Automatically handles case-insensitivity and punctuation stripping for accurate frequency analysis.
- **Clean Output:** Provides structured, easy-to-read statistical reports.

## Technologies Used
- **Language:** Python 3.x
- **Standard Libraries:** `os` (for file path validation)

## Installation & Setup
1. Ensure Python 3.x is installed on your machine.
2. Clone this repository or download the `main.py` file to your local machine.
3. No external dependencies or packages are required.

## How to Run
1. Open your terminal or command prompt.
2. Navigate to the directory containing `main.py`.
3. Execute the command: `python main.py`
4. Follow the on-screen prompts to either enter text manually or provide a file path to analyze.

## Project Structure
- `main.py`: The main application script containing logic for analysis and I/O.
- `README.md`: Project documentation.
- `test_cases.md`: Documentation of test scenarios.

## Testing Details
The project was tested against the following scenarios:
- **Normal Input:** Standard paragraph analysis.
- **Empty Input:** Handled via `ValueError`.
- **File Input:** Validated via `FileNotFoundError`.
- **Duplicate/Punctuation Handling:** Verified using text with varying capitalization and punctuation.

## Limitations
- Currently optimized for English text.
- Large files may require additional memory handling if text exceeds available RAM.

## Future Improvements
- Add support for exporting reports to CSV/JSON files.
- Include graphical visualization (histograms) for word frequency data.
- Support for multiple language character encodings.
