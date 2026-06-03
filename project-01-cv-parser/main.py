import json
import re
import pdfplumber
from pathlib import Path

data_folder = Path("project-01-cv-parser/data")
pdf_files = sorted(data_folder.glob("*.pdf"))

if not pdf_files:
    print("No PDF files found in the data folder.")
else:
    pdf_path = pdf_files[0]

    text = ""

    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()

            if page_text:
                text += page_text + "\n"

    email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
    phone_pattern = r"(05\d{8}|\+\d{1,3}[\d\s-]{7,})"

    email_match = re.search(email_pattern, text)
    phone_match = re.search(phone_pattern, text)

    if email_match:
        email = email_match.group()
    else:
        email = None

    if phone_match:
        phone = phone_match.group()
    else:
        phone = None

    candidate_data = {
        "email": email,
        "phone": phone
    }

    with open("project-01-cv-parser/outputs/result.json", "w") as file:
        json.dump(candidate_data, file, indent=4)

    print(f"Reading PDF: {pdf_path.name}")
    print("CV extraction completed.")
    print(candidate_data)