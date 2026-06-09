# CV-to-JD Matching System

## Project Overview

CV-to-JD Matching System is a Python project that compares candidate skills against job required skills.

This project connects the logic of the previous two projects:

* Project 1: CV Parser
* Project 2: Job Description Parser

Project 3 focuses on matching structured candidate data with structured job requirement data.

## Business Problem

Recruiters often need to compare many candidates against many job descriptions.

Doing this manually can be slow and inconsistent.

A basic matching system can help identify which candidates have the strongest skill overlap with a job description.

This project does not replace recruiter judgment.

It creates a structured first-pass comparison to support human review.

## Solution

The system reads two JSON files:

* Candidate data
* Job data

It compares candidate skills against job required skills and calculates a match score.

The output shows:

* Candidate name
* Job title
* Matched skills
* Missing skills
* Match score

## Current Scope

Version 1 supports:

* Reading structured candidate JSON
* Reading structured job JSON
* Comparing candidate skills with required job skills
* Calculating a simple percentage score
* Saving match results as JSON
* Writing a processing log

## Matching Logic

The matching formula is:

```text
matched required skills / total required skills * 100
```

Example:

```text
Candidate skills:
Python, SQL, FastAPI

Job required skills:
Python, FastAPI, Docker

Matched skills:
Python, FastAPI

Missing skills:
Docker

Match score:
2 / 3 * 100 = 66.67%
```

## Tools Used

* Python
* json
* logging
* pathlib

## Folder Structure

```text
project-03-cv-jd-matcher/
├── data/
├── logs/
├── outputs/
├── sample_data/
├── sample_outputs/
├── src/
├── tests/
├── main.py
├── README.md
└── requirements.txt
```

## Public Sample Input

The project uses synthetic sample data.

Candidate sample file:

```text
project-03-cv-jd-matcher/sample_data/sample_candidates.json
```

Job sample file:

```text
project-03-cv-jd-matcher/sample_data/sample_jobs.json
```

## Public Sample Output

Generated match results:

```text
project-03-cv-jd-matcher/sample_outputs/match_results.json
```

Generated log file:

```text
project-03-cv-jd-matcher/sample_outputs/app.log
```

## Output Example

```json
{
    "candidate_id": "CAND-001",
    "candidate_name": "Maya Benton",
    "job_id": "JOB-001",
    "job_title": "Python Backend Developer",
    "matched_skills": [
        "Python",
        "FastAPI",
        "PostgreSQL",
        "Docker"
    ],
    "missing_skills": [
        "CI/CD"
    ],
    "match_score": 80.0
}
```

## How to Run

Run the matcher from the repository root:

```powershell
python project-03-cv-jd-matcher/main.py
```

Expected output:

```text
CV-to-JD matching completed.
Candidates processed: 4
Jobs processed: 4
Total match results: 16
Results saved to: project-03-cv-jd-matcher\sample_outputs\match_results.json
Log saved to: project-03-cv-jd-matcher\sample_outputs\app.log
```

## Human Review Rule

This project is a decision-support tool.

It does not make hiring decisions.

It does not decide whether a candidate is qualified.

It only compares listed skills against job required skills.

A recruiter or hiring manager should always review the final result.

## Known Limitations

* Version 1 uses exact skill matching.
* It does not understand similar skills yet.
* It does not use AI or semantic matching.
* It does not compare years of experience.
* It does not compare education.
* It does not rank candidates by overall hiring suitability.
* It currently uses sample structured JSON rather than real CV parser skill output.

## Future Improvements

Possible improvements include:

* Add skill extraction to the CV Parser
* Connect real CV Parser output to the matcher
* Connect real JD Parser output to the matcher
* Add skill normalization
* Add weighted required and preferred skills
* Add experience matching
* Add education matching
* Add CSV or Excel output for recruiter review
* Add automated tests
* Add a simple dashboard
* Add AI-assisted semantic matching later

## Project Status

Current status: working Version 1 prototype.

The system successfully compares 4 sample candidates against 4 sample jobs and produces 16 match results.
