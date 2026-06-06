# CV Parser

## Project Overview

CV Parser is a Python project that extracts candidate contact information from PDF CV files.

The current version extracts:

* Candidate name
* Email address
* Phone number

The extracted information is saved in two formats:

* JSON for structured technical output
* Excel for recruiter-friendly review

## Business Problem

Recruiters often receive many CVs and manually search for basic contact information such as names, email addresses, and phone numbers.

This process is repetitive, time-consuming, and prone to manual error.

Many recruiters also prefer Excel over JSON because Excel is easier to review, filter, and share with hiring teams.

## Solution

This project automates the first step of candidate contact extraction.

The program reads PDF CV files, extracts text, identifies candidate contact details using pattern matching, and saves the results into both JSON and Excel files.

## Current Scope

Version 1 supports:

* Reading multiple PDF CV files
* Extracting text from PDFs
* Extracting candidate name
* Extracting email address
* Extracting phone number
* Saving results as JSON
* Saving results as Excel
* Handling missing values
* Writing basic processing logs
* Running public tests using synthetic CVs

## Tools Used

* Python
* pdfplumber
* openpyxl
* re
* json
* logging
* pathlib

## Folder Structure

```text
AI-Career-Lab/
├── architecture/
├── case-studies/
├── notes/
├── project-01-cv-parser/
│   ├── data/
│   ├── logs/
│   ├── outputs/
│   ├── sample_data/
│   ├── sample_outputs/
│   ├── src/
│   ├── tests/
│   ├── main.py
│   ├── README.md
│   ├── TESTING.md
│   └── requirements.txt
└── resources/
```

## Public Sample Test Data

This repository includes synthetic CV files for public testing.

The sample files are stored in:

```text
project-01-cv-parser/sample_data/
```

The sample outputs are stored in:

```text
project-01-cv-parser/sample_outputs/
```

Public sample outputs include:

```text
results.json
results.xlsx
app.log
```

These files are synthetic and do not represent real people.

## Private Data Rule

Private CV files should be kept in:

```text
project-01-cv-parser/data/
```

Private extraction outputs should be kept in:

```text
project-01-cv-parser/outputs/
```

Private logs should be kept in:

```text
project-01-cv-parser/logs/
```

Private folders are not uploaded to GitHub because they may contain personal information.

## Output Example

JSON output:

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

Excel output:

```text
file_name | candidate_name | email | phone
```

The Excel output is designed for recruiters who need a simple table they can review, filter, and share.

## How to Run

Install dependencies:

```powershell
python -m pip install -r project-01-cv-parser/requirements.txt
```

Run the parser:

```powershell
python project-01-cv-parser/main.py
```

## Current Output Locations

For public sample testing:

```text
project-01-cv-parser/sample_outputs/results.json
project-01-cv-parser/sample_outputs/results.xlsx
project-01-cv-parser/sample_outputs/app.log
```

## Human Review Rule

This tool assists recruiters by extracting contact information.

It does not make hiring decisions.

Recruiters must review and validate the extracted information before using it.

## Known Limitations

* Image-based or scanned PDFs may return null values.
* OCR is not included in the current version.
* Candidate name extraction uses a simple rule and may require future improvement for real-world CV formats.
* Phone extraction depends on recognizable phone number patterns.
* Some unusual CV layouts may require future parser improvements.

## Status

Current project status: working local prototype with public synthetic test evidence.

The next improvements are:

* Recreate architecture diagram with Excel output
* Add case study
* Record demo video
* Improve parser structure by moving logic into separate files
