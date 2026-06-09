# CV-to-JD Matching System Testing

## Purpose

This document records the test cases for Project 3 — CV-to-JD Matching System.

The goal is to verify that the system can read candidate data, read job data, compare skills, calculate match scores, save JSON output, and create a processing log.

## Test Input

Candidate input file:

```text
project-03-cv-jd-matcher/sample_data/sample_candidates.json
```

Job input file:

```text
project-03-cv-jd-matcher/sample_data/sample_jobs.json
```

## Test Output

Match results:

```text
project-03-cv-jd-matcher/sample_outputs/match_results.json
```

Log file:

```text
project-03-cv-jd-matcher/sample_outputs/app.log
```

## Test Summary

| Test Case | Description                                     | Expected Result                                            | Status |
| --------- | ----------------------------------------------- | ---------------------------------------------------------- | ------ |
| TC1       | Load candidate JSON file                        | Candidate records loaded successfully                      | Passed |
| TC2       | Load job JSON file                              | Job records loaded successfully                            | Passed |
| TC3       | Compare Maya Benton to Python Backend Developer | Match score calculated as 80%                              | Passed |
| TC4       | Compare Omar Faris to Data Analyst              | Match score calculated as 80%                              | Passed |
| TC5       | Compare Lina Carter to HR Specialist            | Match score calculated as 80%                              | Passed |
| TC6       | Compare Noah Kim to Cybersecurity Analyst       | Match score calculated as 80%                              | Passed |
| TC7       | Compare all candidates against all jobs         | 16 match results created                                   | Passed |
| TC8       | Identify matched skills                         | Matched skills are listed correctly                        | Passed |
| TC9       | Identify missing skills                         | Missing skills are listed correctly                        | Passed |
| TC10      | Calculate percentage score                      | Score uses matched skills divided by total required skills | Passed |
| TC11      | Save JSON output                                | match_results.json created successfully                    | Passed |
| TC12      | Create log file                                 | app.log created successfully                               | Passed |

## Expected Match Count

The sample data contains:

```text
4 candidates
4 jobs
```

Expected total comparisons:

```text
4 candidates × 4 jobs = 16 match results
```

The system produced 16 match results.

## Example Passed Result

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

## Matching Formula

The score is calculated using this formula:

```text
matched required skills / total required skills * 100
```

Example:

```text
4 matched skills / 5 required skills * 100 = 80%
```

## Observations

The matcher correctly identified the strongest candidate for each sample job:

```text
Maya Benton → Python Backend Developer → 80%
Omar Faris → Data Analyst → 80%
Lina Carter → HR Specialist → 80%
Noah Kim → Cybersecurity Analyst → 80%
```

The system also correctly produced lower scores for weaker matches.

## Known Limitations

The current version uses exact skill matching.

For example, it does not automatically understand that:

```text
CI/CD
Continuous Integration
Deployment pipelines
```

may refer to related concepts.

Future versions may improve this with skill normalization or AI-assisted semantic matching.

## Privacy Note

The current test data is synthetic.

No real candidate data or confidential job descriptions should be uploaded to GitHub.
