# Job Description Parser

## Project Overview

Job Description Parser is a Python project that reads synthetic job description text files and extracts structured job requirement information.

The current version extracts:

- Job title
- Company
- Location
- Employment type
- Years of experience
- Education
- Required skills
- Preferred skills
- Responsibilities
- About the role

The extracted information is saved as JSON.

## Business Problem

Recruitment teams often deal with job descriptions written in different formats.

Before a job description can be matched against candidate CVs, the role requirements need to be converted into structured data.

Manual review is slow and inconsistent, especially when comparing multiple job descriptions.

## Solution

This project reads job descriptions from text files and extracts key fields into a structured JSON output.

The output can later be used as the foundation for a CV-to-job matching system.

## Why JSON Output

Unlike the CV Parser project, this project does not create Excel output in Version 1.

The main purpose of this parser is to structure job requirements for future automation.

JSON is the better format for:

- Future CV-to-JD matching
- APIs
- Automated scoring
- Structured storage
- Further Python processing

Excel may be added later if the use case becomes comparing many job descriptions manually.

## Current Scope

Version 1 supports:

- Reading multiple `.txt` job description files
- Extracting single-line fields
- Extracting bullet-list sections
- Extracting paragraph sections
- Saving structured JSON output
- Writing a processing log
- Running public tests using synthetic job descriptions

## Tools Used

- Python
- json
- logging
- pathlib

## Folder Structure

```text
project-02-jd-parser/
├── data/
├── logs/
├── outputs/
├── sample_data/
├── sample_outputs/
├── src/
├── tests/
├── main.py
├── README.md
├── TESTING.md
└── requirements.txt