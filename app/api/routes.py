from fastapi import APIRouter, UploadFile, File, Form
from fastapi.responses import JSONResponse
from app.services.pdf_parser import extract_questions_from_pdf
from app.services.answer_storage import save_answer_feedback
from app.models.schemas import Question, AnswerSubmission, SubmissionResponse
from typing import List

router = APIRouter()

@router.post("/upload-pdf", response_model=List[Question])
async def upload_pdf(
    pdf_file: UploadFile = File(...),
    chapter: str = Form(...)
):
    contents = await pdf_file.read()
    return extract_questions_from_pdf(contents, chapter)

@router.post("/submit-answer", response_model=SubmissionResponse)
def submit_answer(data: AnswerSubmission):
    success = save_answer_feedback(data)
    return SubmissionResponse(success=success)
