# CV Parser Testing

## Purpose

This document records the test cases used for Project 1 — CV Parser.

The goal is to verify that the parser can read PDF CV files, extract email addresses, extract phone numbers, handle missing values, and save structured JSON output.

## Public Test Evidence

This project includes synthetic CV files for public testing.

Input files:

project-01-cv-parser/sample_data/

Generated sample output:

project-01-cv-parser/sample_outputs/results.json

Generated sample log:

project-01-cv-parser/sample_outputs/app.log

The sample files are synthetic and do not represent real people.

Private CV files, private logs, and private extraction results are not uploaded to GitHub.

## Test Summary

| Test Case | Description | Expected Result | Status |
|---|---|---|---|
| TC1 | Standard text-based CV | Email and phone extracted | Passed |
| TC2 | Two-column CV | Email and phone extracted | Passed |
| TC3 | CV with tables | Email and phone extracted | Passed |
| TC4 | CV with date gaps | Email and phone extracted | Passed |
| TC5 | CV with international phone format | Phone extracted | Passed |
| TC6 | Multi-page CV | Email and phone extracted | Passed |
| TC7 | Multiple PDF CVs in sample_data folder | All PDFs processed | Passed |
| TC8 | JSON output creation | results.json created | Passed |
| TC9 | Logging | app.log created with processing history | Passed |

## Observations

The parser successfully processed multiple synthetic PDF CV files from the sample_data folder.

For text-based PDFs, email and phone extraction worked correctly.

The parser saved structured results into sample_outputs/results.json.

The parser also created a log file showing processing history in sample_outputs/app.log.

## Known Limitation

The current version does not support OCR.

Scanned or image-based PDF files may not produce readable text through pdfplumber.

## Privacy Note

Real CV files, extracted results, and logs are not uploaded to GitHub because they may contain personal information.