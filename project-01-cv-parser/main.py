import json
import re
import logging
import pdfplumber
from pathlib import Path

data_folder = Path("project-01-cv-parser/sample_data")
output_file = Path("project-01-cv-parser/sample_outputs/results.json")
log_file = Path("project-01-cv-parser/sample_outputs/app.log")

logging.basicConfig(
    filename=log_file,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

pdf_files = sorted(data_folder.glob("*.pdf"))

email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
phone_pattern = r"(05(?:[ -]?\d){8}|\+\d{1,3}(?:[ -]?\d){7,14})"

results = []

logging.info("CV Parser run started.")
logging.info(f"PDF files found: {len(pdf_files)}")

if not pdf_files:
    print("No PDF files found in the data folder.")
    logging.warning("No PDF files found in the data folder.")

for pdf_path in pdf_files:
    print(f"Processing PDF: {pdf_path.name}")
    logging.info(f"Processing PDF: {pdf_path.name}")

    text = ""

    try:
        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()

                if page_text:
                    text += page_text + "\n"

        logging.info(f"Text extracted successfully: {pdf_path.name}")

    except Exception as error:
        print(f"Error reading PDF: {pdf_path.name}")
        logging.error(f"Error reading PDF: {pdf_path.name} - {error}")

    email_match = re.search(email_pattern, text)
    phone_match = re.search(phone_pattern, text)

    if email_match:
        email = email_match.group()
        logging.info(f"Email found: {pdf_path.name}")
    else:
        email = None
        logging.warning(f"Email not found: {pdf_path.name}")

    if phone_match:
        phone = phone_match.group()
        logging.info(f"Phone found: {pdf_path.name}")
    else:
        phone = None
        logging.warning(f"Phone not found: {pdf_path.name}")

    candidate_data = {
        "file_name": pdf_path.name,
        "email": email,
        "phone": phone
    }

    results.append(candidate_data)

with open(output_file, "w") as file:
    json.dump(results, file, indent=4)

logging.info("CV Parser run completed.")

print("CV extraction completed.")
print(f"Total PDFs processed: {len(results)}")
print(f"Results saved to: {output_file}")