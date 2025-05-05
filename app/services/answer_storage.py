import json
from app.models.schemas import AnswerSubmission

STORAGE_FILE = "submitted_answers.json"

def save_answer_feedback(data: AnswerSubmission) -> bool:
    try:
        try:
            with open(STORAGE_FILE, "r", encoding="utf-8") as f:
                existing = json.load(f)
        except FileNotFoundError:
            existing = []

        existing.append(data.dict())

        with open(STORAGE_FILE, "w", encoding="utf-8") as f:
            json.dump(existing, f, ensure_ascii=False, indent=2)
        return True
    except Exception:
        return False
