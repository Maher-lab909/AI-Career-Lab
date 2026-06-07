import json
import logging
from pathlib import Path

data_folder = Path("project-02-jd-parser/sample_data")
output_file = Path("project-02-jd-parser/sample_outputs/results.json")
log_file = Path("project-02-jd-parser/sample_outputs/app.log")

data_folder.mkdir(parents=True, exist_ok=True)
output_file.parent.mkdir(parents=True, exist_ok=True)
log_file.parent.mkdir(parents=True, exist_ok=True)

logging.basicConfig(
    filename=log_file,
    filemode="w",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def extract_single_line_field(text, field_name):
    for line in text.splitlines():
        clean_line = line.strip()

        if clean_line.startswith(field_name + ":"):
            return clean_line.replace(field_name + ":", "").strip()

    return None


def extract_bullet_section(text, section_name):
    lines = text.splitlines()
    section_items = []
    inside_section = False

    known_sections = [
        "Job Title:",
        "Company:",
        "Location:",
        "Employment Type:",
        "Years of Experience:",
        "Education:",
        "Required Skills:",
        "Preferred Skills:",
        "Responsibilities:",
        "About the Role:"
    ]

    for line in lines:
        clean_line = line.strip()

        if clean_line == section_name + ":":
            inside_section = True
            continue

        if inside_section:
            if clean_line in known_sections:
                break

            if clean_line.startswith("-"):
                item = clean_line.replace("-", "", 1).strip()
                section_items.append(item)

    return section_items


def extract_paragraph_section(text, section_name):
    lines = text.splitlines()
    paragraph_lines = []
    inside_section = False

    known_sections = [
        "Job Title:",
        "Company:",
        "Location:",
        "Employment Type:",
        "Years of Experience:",
        "Education:",
        "Required Skills:",
        "Preferred Skills:",
        "Responsibilities:",
        "About the Role:"
    ]

    for line in lines:
        clean_line = line.strip()

        if clean_line == section_name + ":":
            inside_section = True
            continue

        if inside_section:
            if clean_line in known_sections:
                break

            if clean_line:
                paragraph_lines.append(clean_line)

    if paragraph_lines:
        return " ".join(paragraph_lines)

    return None


txt_files = sorted(data_folder.glob("*.txt"))

results = []

logging.info("JD Parser run started.")
logging.info(f"TXT files found: {len(txt_files)}")

if not txt_files:
    print("No TXT files found in the sample_data folder.")
    logging.warning("No TXT files found in the sample_data folder.")

for txt_path in txt_files:
    print(f"Processing JD: {txt_path.name}")
    logging.info(f"Processing JD: {txt_path.name}")

    try:
        text = txt_path.read_text(encoding="utf-8")
        logging.info(f"Text loaded successfully: {txt_path.name}")

    except Exception as error:
        print(f"Error reading file: {txt_path.name}")
        logging.error(f"Error reading file: {txt_path.name} - {error}")
        text = ""

    job_data = {
        "file_name": txt_path.name,
        "job_title": extract_single_line_field(text, "Job Title"),
        "company": extract_single_line_field(text, "Company"),
        "location": extract_single_line_field(text, "Location"),
        "employment_type": extract_single_line_field(text, "Employment Type"),
        "years_experience": extract_single_line_field(text, "Years of Experience"),
        "education": extract_single_line_field(text, "Education"),
        "required_skills": extract_bullet_section(text, "Required Skills"),
        "preferred_skills": extract_bullet_section(text, "Preferred Skills"),
        "responsibilities": extract_bullet_section(text, "Responsibilities"),
        "about_the_role": extract_paragraph_section(text, "About the Role")
    }

    results.append(job_data)
    logging.info(f"Extraction completed: {txt_path.name}")

with open(output_file, "w", encoding="utf-8") as file:
    json.dump(results, file, indent=4, ensure_ascii=False)

logging.info("JD Parser run completed.")

print("JD extraction completed.")
print(f"Total JDs processed: {len(results)}")
print(f"Results saved to: {output_file}")
print(f"Log saved to: {log_file}")