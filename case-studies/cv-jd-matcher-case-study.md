# CV-to-JD Matching System Case Study

## Project Name

CV-to-JD Matching System

## Project Type

Learning Project

## Business Problem

Recruiters and hiring teams often need to compare candidate profiles against job descriptions.

This comparison usually requires checking whether a candidate has the skills required for a role.

When this is done manually, it can become repetitive, slow, and inconsistent, especially when comparing multiple candidates against multiple jobs.

The problem is not making a final hiring decision.

The problem is creating a structured first-pass comparison between candidate skills and job requirements.

## Current Manual Process

A typical manual process looks like this:

1. Recruiter opens a candidate profile or CV summary.
2. Recruiter identifies the candidate’s listed skills.
3. Recruiter opens a job description.
4. Recruiter reviews the required skills.
5. Recruiter manually compares candidate skills against job required skills.
6. Recruiter notes which skills match.
7. Recruiter notes which required skills are missing.
8. Recruiter repeats the process for every candidate and every job.

This process becomes inefficient when there are many candidates and many job descriptions.

## Solution

I built a Python-based CV-to-JD Matching System that compares structured candidate skill data against structured job requirement data.

The system reads:

* Candidate JSON data
* Job JSON data

Then it compares each candidate against each job and produces structured match results.

The output includes:

* Candidate ID
* Candidate name
* Job ID
* Job title
* Matched skills
* Missing skills
* Match score

## Why This Project Comes After Project 1 and Project 2

This project connects the previous two portfolio projects.

Project 1 extracted structured candidate information from CVs.

Project 2 extracted structured requirement information from job descriptions.

Project 3 uses structured candidate and job data to perform matching logic.

The current Version 1 uses sample structured JSON data because the CV Parser does not extract skills yet.

This keeps the project focused on learning matching logic before adding more advanced parsing.

## How The Solution Works

The workflow is:

1. Candidate data is stored in `sample_candidates.json`.
2. Job data is stored in `sample_jobs.json`.
3. The Python script loads both JSON files.
4. Candidate skills are normalized by converting text to lowercase and trimming spaces.
5. Job required skills are normalized using the same method.
6. The system compares candidate skills against job required skills.
7. Matched skills are stored.
8. Missing required skills are stored.
9. A match score is calculated.
10. Results are saved to `match_results.json`.
11. A log file records the processing history.

## Matching Logic

The current matching logic uses exact skill matching.

The score formula is:

```text
matched required skills / total required skills * 100
```

Example:

```text
Candidate skills:
Python, SQL, FastAPI, Docker

Job required skills:
Python, FastAPI, PostgreSQL, Docker, CI/CD

Matched skills:
Python, FastAPI, Docker

Missing skills:
PostgreSQL, CI/CD

Match score:
3 / 5 * 100 = 60%
```

## Tools Used

* Python
* json
* logging
* pathlib

## Public Test Setup

The project uses synthetic sample data.

Candidate input:

```text
project-03-cv-jd-matcher/sample_data/sample_candidates.json
```

Job input:

```text
project-03-cv-jd-matcher/sample_data/sample_jobs.json
```

Generated match output:

```text
project-03-cv-jd-matcher/sample_outputs/match_results.json
```

Generated log output:

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

## Results

The system successfully compared:

```text
4 candidates
4 jobs
```

This produced:

```text
4 candidates × 4 jobs = 16 match results
```

The strongest sample matches were:

```text
Maya Benton → Python Backend Developer → 80%
Omar Faris → Data Analyst → 80%
Lina Carter → HR Specialist → 80%
Noah Kim → Cybersecurity Analyst → 80%
```

The system also produced lower scores for weaker candidate-job combinations.

## Business Value

This project creates a structured first-pass skill comparison.

It can help recruitment teams:

* Compare candidates more consistently
* Identify skill overlap quickly
* See missing required skills
* Reduce repetitive manual screening work
* Prepare data for future ranking or dashboard tools
* Build toward a larger recruitment automation workflow

The system is not intended to replace recruiters.

It supports recruiter review by organizing candidate-job comparison data.

## Human Review Rule

This project is a decision-support tool.

It does not make hiring decisions.

It does not decide whether a candidate should be hired.

It does not judge candidate quality beyond listed skill overlap.

A recruiter or hiring manager must review all results before making any decision.

## Known Limitations

Version 1 uses exact skill matching only.

It does not understand similar or related terms.

For example, it does not automatically know that these may be related:

```text
CI/CD
Continuous Integration
Deployment pipelines
```

It also does not compare:

* Years of experience
* Education
* Certifications
* Seniority level
* Project experience
* Industry background
* Soft skills
* Preferred skills weighting

The current version also uses sample structured JSON data instead of directly reading skills from real CV parser output.

## Lessons Learned

This project helped practice:

* Reading multiple JSON files
* Comparing two structured datasets
* Normalizing text before comparison
* Calculating a percentage score
* Creating matched and missing skill lists
* Writing structured JSON output
* Creating processing logs
* Thinking about human review and responsible automation

## Connection To Earlier Projects

This project builds on the previous projects:

```text
Project 1: CV Parser
Project 2: Job Description Parser
Project 3: CV-to-JD Matching System
```

Together, they form the foundation of a simple recruitment automation pipeline:

```text
CV data
+
Job description data
↓
Candidate-job matching
```

## Future Improvements

Possible future improvements include:

* Add skill extraction to the CV Parser
* Connect real CV Parser output to the matcher
* Connect real JD Parser output to the matcher
* Add preferred skill scoring
* Add weighted scoring for required skills
* Add experience matching
* Add education matching
* Add skill synonym mapping
* Add fuzzy matching
* Add AI-assisted semantic matching later
* Add Excel output for recruiter review
* Add dashboard visualization
* Add automated tests
* Add ranked top candidates per job

## Summary

The CV-to-JD Matching System is a practical third project in the recruitment automation roadmap.

It connects candidate data and job requirement data, compares skills, calculates match scores, and creates structured output for review.

Version 1 is intentionally simple and transparent.

It does not use AI yet, but it creates the foundation for more advanced matching later.
