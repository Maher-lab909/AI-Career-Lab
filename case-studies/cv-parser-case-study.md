# CV Parser Case Study

## Project Name

CV Parser

## Project Type

Learning Project

## Business Problem

Recruiters often receive multiple CVs and manually search for basic candidate contact information such as candidate name, email address, and phone number.

This process is repetitive and time-consuming.

It can also create manual errors, especially when recruiters process many CVs in a short period of time.

The problem is not complex hiring decision-making.

The problem is simple contact extraction from PDF CVs.

## Current Manual Process

The current manual process usually looks like this:

1. Recruiter opens each CV.
2. Recruiter searches for the candidate name.
3. Recruiter searches for the email address.
4. Recruiter searches for the phone number.
5. Recruiter copies the information into Excel or another tracking file.
6. Recruiter repeats the same steps for every CV.

This creates unnecessary manual work.

## Solution

I built a Python-based CV Parser that reads PDF CV files and extracts basic candidate contact information.

The parser extracts:

* File name
* Candidate name
* Email address
* Phone number

The results are saved in two formats:

* JSON for structured technical output
* Excel for recruiter-friendly review

The Excel output is important because recruiters commonly use spreadsheets for tracking and sharing candidate information.

## How The Solution Works

The workflow is:

1. PDF CV files are placed in the input folder.
2. The Python script reads the PDF files.
3. pdfplumber extracts text from each PDF.
4. Regex patterns identify email addresses and phone numbers.
5. A simple name extraction rule identifies the candidate name.
6. Results are saved into a structured JSON file.
7. Results are also saved into an Excel file.
8. A log file records the processing history.

## Tools Used

* Python
* pdfplumber
* openpyxl
* re
* json
* logging
* pathlib

## Public Test Setup

The project includes synthetic CVs for public testing.

Public test input folder:

```text
project-01-cv-parser/sample_data/
```

Public output folder:

```text
project-01-cv-parser/sample_outputs/
```

Generated public outputs:

```text
results.json
results.xlsx
app.log
```

The sample CVs are synthetic and do not represent real people.

Private CVs, private outputs, and private logs are not uploaded to GitHub.

## Output

The parser produces these fields:

```text
file_name
candidate_name
email
phone
```

Example JSON structure:

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

Example Excel structure:

```text
file_name | candidate_name | email | phone
```

## Results

The parser successfully processed multiple synthetic PDF CV files.

The system created:

* Structured JSON output
* Recruiter-friendly Excel output
* Processing log file

The Excel output makes the result easier for recruiters to review, filter, and share.

## Business Value

This project reduces repetitive manual work in early-stage recruitment processing.

Instead of manually opening each CV and copying contact information, the recruiter can run the parser and review the extracted results in Excel.

Potential value includes:

* Time saved during CV review
* Reduced manual copy-paste errors
* Faster candidate tracking
* More structured recruitment data
* Better handoff to recruiters or hiring teams

## Human Review Rule

The parser assists recruiters.

It does not make hiring decisions.

It does not shortlist candidates.

It does not reject candidates.

Recruiters must review and validate extracted information before using it.

## Known Limitations

The current version does not support OCR.

Scanned or image-based PDFs may not produce readable text.

Candidate name extraction uses a simple rule based on the first useful line of extracted text. This works for the synthetic test CVs but may require improvement for real-world CV formats.

Phone extraction depends on recognizable phone number patterns.

Some unusual CV layouts may require future improvements.

## Lessons Learned

This project showed how Python can be used to automate a real recruitment process.

The most important learning points were:

* How to read PDF files using Python
* How to extract text from PDFs
* How to use regex for email and phone detection
* How to structure output as JSON
* How to create recruiter-friendly Excel output
* How to process multiple files
* How to log processing activity
* How to separate public sample data from private real data

## Next Improvements

Possible next improvements:

* Improve candidate name extraction
* Add support for more phone number formats
* Add OCR support for scanned PDFs
* Move logic into separate Python files
* Add automated tests
* Add a simple user interface later
* Calculate time saved compared with manual extraction

## Summary

The CV Parser is a practical first automation project.

It solves a real recruitment operations problem by converting PDF CVs into structured contact data.

The project is intentionally simple, but it demonstrates the foundation for larger recruitment automation systems.
