# CV Parser Testing

## Purpose

This document records the test cases used for Project 1 — CV Parser.

The goal is to verify that the parser can read PDF CV files, extract candidate names, extract email addresses, extract phone numbers, handle missing values, and save structured outputs.

The project currently saves results in both JSON and Excel formats.

## Public Test Evidence

This project includes synthetic CV files for public testing.

Input files:

```text
project-01-cv-parser/sample_data/
```

Generated sample JSON output:

```text
project-01-cv-parser/sample_outputs/results.json
```

Generated sample Excel output:

```text
project-01-cv-parser/sample_outputs/results.xlsx
```

Generated sample log:

```text
project-01-cv-parser/sample_outputs/app.log
```

The sample files are synthetic and do not represent real people.

Private CV files, private logs, and private extraction results are not uploaded to GitHub.

## Test Summary

| Test Case | Description                            | Expected Result                            | Status |
| --------- | -------------------------------------- | ------------------------------------------ | ------ |
| TC1       | Standard text-based CV                 | Candidate name, email, and phone extracted | Passed |
| TC2       | Two-column CV                          | Candidate name, email, and phone extracted | Passed |
| TC3       | CV with tables                         | Candidate name, email, and phone extracted | Passed |
| TC4       | CV with date gaps                      | Candidate name, email, and phone extracted | Passed |
| TC5       | CV with international phone format     | Phone extracted correctly                  | Passed |
| TC6       | Multi-page CV                          | Candidate name, email, and phone extracted | Passed |
| TC7       | Multiple PDF CVs in sample_data folder | All PDFs processed                         | Passed |
| TC8       | JSON output creation                   | results.json created                       | Passed |
| TC9       | Excel output creation                  | results.xlsx created                       | Passed |
| TC10      | Logging                                | app.log created with processing history    | Passed |

## Sample Output Fields

The parser currently outputs the following fields:

```text
file_name
candidate_name
email
phone
```

## JSON Output

The JSON file stores structured extraction results for technical use.

Example:

```json
[
    {
        "file_name": "cv_001_standard.pdf",
        "candidate_name": "Maya R. Benton",
        "email": "maya.benton@example.com",
        "phone": "+1-555-0138"
    }
]
```

## Excel Output

The Excel file stores the same extraction results in a recruiter-friendly table.

This is useful because recruiters commonly work with spreadsheets instead of JSON files.

Expected Excel columns:

```text
file_name | candidate_name | email | phone
```

## Logging Output

The log file records the processing history.

It confirms:

* Parser run started
* Number of PDF files found
* Each PDF processed
* Text extraction status
* Email extraction status
* Phone extraction status
* Candidate name extraction status
* Parser run completed

## Observations

The parser successfully processed multiple synthetic PDF CV files from the sample_data folder.

For text-based PDFs, candidate name, email, and phone extraction worked correctly.

The parser saved structured results into:

```text
sample_outputs/results.json
sample_outputs/results.xlsx
```

The parser also created a processing log in:

```text
sample_outputs/app.log
```

## Known Limitation

The current version does not support OCR.

Scanned or image-based PDF files may not produce readable text through pdfplumber.

Candidate name extraction currently uses a simple rule based on the first useful line of extracted text. This works for the synthetic test CVs but may need improvement for real-world CVs.

## Privacy Note

Real CV files, extracted results, and logs are not uploaded to GitHub because they may contain personal information.

Public testing uses synthetic CVs only.
