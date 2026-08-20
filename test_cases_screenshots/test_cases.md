# Test Cases for Text Statistics Analyzer

This document outlines the test scenarios performed to ensure the robustness and correctness of the Text Statistics Analyzer application.

## Test Case 1: Normal Input (Manual String)
- **Scenario:** Processing a standard paragraph.
- **Input:** 
  - Choice: `1`
  - Text: `Machine learning is amazing. Machine learning powers data science!`
- **Expected Output:**
  - Characters: 64
  - Words: 10
  - Sentences: 2
  - Unique terms: 7
  - Frequency Check: `machine` (2), `learning` (2)

## Test Case 2: Empty Input Validation
- **Scenario:** Testing behavior when the user provides no text.
- **Input:** 
  - Choice: `1`
  - Text: `[Enter]`
- **Expected Output:**
  - Error: `Error: Input text cannot be empty.`

## Test Case 3: Boundary Input (Single Word)
- **Scenario:** Testing the application with minimal input.
- **Input:** 
  - Choice: `1`
  - Text: `Hello`
- **Expected Output:**
  - Characters: 5
  - Words: 1
  - Sentences: 1
  - Unique terms: 1

## Test Case 4: File Input Error Handling
- **Scenario:** Verifying handling of non-existent file paths.
- **Input:** 
  - Choice: `2`
  - File Path: `nonexistent_file.txt`
- **Expected Output:**
  - Error: `Error: The file 'nonexistent_file.txt' does not exist.`

## Test Case 5: Duplicate and Punctuation Handling
- **Scenario:** Ensuring punctuation is stripped and case is normalized.
- **Input:** 
  - Choice: `1`
  - Text: `Test, test! TEST? One, one, two.`
- **Expected Output:**
  - Characters: 31
  - Words: 6
  - Unique terms: 3
  - Frequency Check: `test` (3), `one` (2), `two` (1)

## Test Case 6: Valid File Processing (`test.txt`)
- **Scenario:** Reading and processing text correctly from an external local file using its absolute path.
- **Input:** 
  - Choice: `2`
  - File Path: `C:\Users\Pallavi\Downloads\test.txt`
- **Expected Output:**
  - Successful file read, accurate metrics calculation (e.g., character count, word count, sentence count, unique terms), and correct frequency summary output without throwing any exceptions.
