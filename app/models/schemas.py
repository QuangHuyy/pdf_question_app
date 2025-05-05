from pydantic import BaseModel
from typing import List

class Question(BaseModel):
    question_text: str
    answer_text: str

class AnswerSubmission(BaseModel):
    question_text: str
    user_answer: str
    is_correct: bool
    explanation: str

class SubmissionResponse(BaseModel):
    success: bool
