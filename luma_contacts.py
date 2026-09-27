import csv


def load_contacts(filepath: str = "contacts.csv"):
    contacts = []
    try:
        with open(filepath, newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                contacts.append({
                    "name": row.get("name", "").strip(),
                    "email": row.get("email", "").strip(),
                    "fun_fact": row.get("fun_fact", "").strip(),
                })
    except FileNotFoundError:
        print(f"Warning: {filepath} not found.")
    return contacts