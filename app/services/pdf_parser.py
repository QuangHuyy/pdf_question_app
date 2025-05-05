import fitz  # PyMuPDF
import re
from typing import List
from app.models.schemas import Question

def extract_questions_from_pdf(pdf_bytes: bytes, chapter: str) -> List[Question]:
    doc = fitz.open(stream=pdf_bytes, filetype="pdf")
    full_text = ""
    for page in doc:
        full_text += page.get_text()

    # Very basic example — should be improved with NLP or better patterns
    questions = []
    pattern = re.compile(rf"{chapter}.*?(Câu \d+:.*?)\n(Đáp án:.*?)\n", re.DOTALL | re.IGNORECASE)
    matches = pattern.findall(full_text)

    for match in matches:
        q = match[0].strip()
        a = match[1].strip()
        questions.append(Question(question_text=q, answer_text=a))

    return questions
