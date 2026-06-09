import json
import logging
from pathlib import Path

candidates_file = Path("project-03-cv-jd-matcher/sample_data/sample_candidates.json")
jobs_file = Path("project-03-cv-jd-matcher/sample_data/sample_jobs.json")
output_file = Path("project-03-cv-jd-matcher/sample_outputs/match_results.json")
log_file = Path("project-03-cv-jd-matcher/sample_outputs/app.log")

output_file.parent.mkdir(parents=True, exist_ok=True)
log_file.parent.mkdir(parents=True, exist_ok=True)

logging.basicConfig(
    filename=log_file,
    filemode="w",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def load_json(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)

def normalize_skill(skill):
    return skill.strip().lower()

def compare_candidate_to_job(candidate, job):
    candidate_skills = candidate["skills"]
    required_skills = job["required_skills"]

    normalized_candidate_skills = {
        normalize_skill(skill): skill
        for skill in candidate_skills
    }

    matched_skills = []
    missing_skills = []

    for required_skill in required_skills:
        normalized_required_skill = normalize_skill(required_skill)

        if normalized_required_skill in normalized_candidate_skills:
            matched_skills.append(required_skill)
        else:
            missing_skills.append(required_skill)

    if required_skills:
        match_score = round((len(matched_skills) / len(required_skills)) * 100, 2)
    else:
        match_score = 0

    return {
        "candidate_id": candidate["candidate_id"],
        "candidate_name": candidate["candidate_name"],
        "job_id": job["job_id"],
        "job_title": job["job_title"],
        "matched_skills": matched_skills,
        "missing_skills": missing_skills,
        "match_score": match_score
    }

logging.info("CV-to-JD Matcher run started.")

try:
    candidates = load_json(candidates_file)
    logging.info(f"Candidates loaded: {len(candidates)}")
except Exception as error:
    print("Error loading candidates file.")
    logging.error(f"Error loading candidates file: {error}")
    candidates = []

try:
    jobs = load_json(jobs_file)
    logging.info(f"Jobs loaded: {len(jobs)}")
except Exception as error:
    print("Error loading jobs file.")
    logging.error(f"Error loading jobs file: {error}")
    jobs = []

match_results = []

for candidate in candidates:
    for job in jobs:
        result = compare_candidate_to_job(candidate, job)
        match_results.append(result)
        logging.info(
            f"Matched {candidate['candidate_name']} against {job['job_title']} - Score: {result['match_score']}%"
        )

match_results = sorted(
    match_results,
    key=lambda result: (result["job_title"], -result["match_score"])
)

with open(output_file, "w", encoding="utf-8") as file:
    json.dump(match_results, file, indent=4, ensure_ascii=False)

logging.info("CV-to-JD Matcher run completed.")

print("CV-to-JD matching completed.")
print(f"Candidates processed: {len(candidates)}")
print(f"Jobs processed: {len(jobs)}")
print(f"Total match results: {len(match_results)}")
print(f"Results saved to: {output_file}")
print(f"Log saved to: {log_file}")