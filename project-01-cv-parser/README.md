# CV Parser

## Project Overview

CV Parser is a Python project that extracts candidate contact information from PDF CV files.

The current version extracts:

* Email address
* Phone number

The extracted information is saved as structured JSON output.

## Business Problem

Recruiters often spend time manually opening CVs and searching for contact information such as email addresses and phone numbers.

This process is repetitive, time-consuming, and prone to manual error.

## Solution

This project automates the first step of candidate information extraction.

The program reads PDF CV files from the `data` folder, extracts text, searches for email and phone patterns, and saves the results into a JSON file.

## Current Scope

Version 1 supports:

* Reading PDF files
* Extracting text from PDFs
* Extracting email addresses
* Extracting phone numbers
* Processing multiple CVs
* Handling missing email or phone values
* Saving results as JSON
* Writing basic logs

## Tools Used

* Python
* pdfplumber
* re
* json
* logging
* pathlib

## Folder Structure

AI-Career-Lab/
project-01-cv-parser/
data/
logs/
outputs/
main.py
README.md
requirements.txt

## Output Example

[
{
"file_name": "example_cv.pdf",
"email": "[candidate@example.com](mailto:candidate@example.com)",
"phone": "+966 50 000 0000"
},
{
"file_name": "missing_phone_cv.pdf",
"email": "[candidate2@example.com](mailto:candidate2@example.com)",
"phone": null
}
]

## Human Review Rule

This tool assists recruiters by extracting contact information.

It does not make hiring decisions.

Recruiters must review and validate the extracted information.

## Current Limitations

* Image-based or scanned PDFs may not return email or phone values.
* OCR is not included in the current version.
* The extraction depends on text quality inside the PDF.
* Some unusual phone formats may require future improvements.

## Status

Current project status: working local prototype.

The next improvements are:

* Improve test documentation
* Add architecture diagram
* Add case study
* Improve README formatting
