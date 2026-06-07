# Job Description Parser Case Study

## Project Name

Job Description Parser

## Project Type

Learning Project

## Business Problem

Recruitment and HR teams often work with job descriptions that contain important role requirements, but the information is usually written in unstructured text.

Before a job description can be used for candidate matching, reporting, or automation, the key details need to be converted into structured data.

Manual review is slow and inconsistent, especially when comparing multiple job descriptions across different roles.

The problem is not candidate evaluation yet.

The problem is extracting structured job requirement data from job description text.

## Current Manual Process

The current manual process usually looks like this:

1. Recruiter opens a job description.
2. Recruiter identifies the job title.
3. Recruiter checks the location and employment type.
4. Recruiter reads the required experience and education.
5. Recruiter manually reviews required skills and preferred skills.
6. Recruiter copies the information into notes, spreadsheets, or another system.
7. Recruiter repeats the same process for every job description.

This creates repetitive manual work and makes later matching harder.

## Solution

I built a Python-based Job Description Parser that reads `.txt` job description files and extracts structured job requirement information.

The parser extracts:

- File name
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

The results are saved as structured JSON output.

## Why JSON Output

This project does not create Excel output in Version 1.

For the CV Parser project, Excel made sense because recruiters directly review candidate contact lists.

For the Job Description Parser, the main purpose is different.

The structured job description output is intended to support future automation, especially CV-to-job matching.

JSON is better for:

- Future matching systems
- APIs
- Automated scoring
- Structured storage
- Further Python processing

Excel may be added later only if the use case becomes manual comparison of many job descriptions.

## How The Solution Works

The workflow is:

1. Synthetic job description `.txt` files are placed in the sample input folder.
2. The Python script reads each `.txt` file.
3. The parser extracts single-line fields such as job title, company, location, employment type, years of experience, and education.
4. The parser extracts bullet-list sections such as required skills, preferred skills, and responsibilities.
5. The parser extracts paragraph sections such as about the role.
6. Results are saved into a structured JSON file.
7. A log file records the processing history.

## Tools Used

- Python
- json
- logging
- pathlib

## Public Test Setup

The project includes synthetic job descriptions for public testing.

Public test input folder:

```text
project-02-jd-parser/sample_data/