import { Injectable } from '@nestjs/common';
import * as fs from 'fs';
import { SubmitAnswerDto } from '../submit-answer.dto';

@Injectable()
export class PdfSaveService {
  private readonly filePath = 'submitted_answers.json';

  saveAnswer(body: SubmitAnswerDto) {
    const existing = fs.existsSync(this.filePath)
      ? JSON.parse(fs.readFileSync(this.filePath, 'utf-8'))
      : [];
    existing.push(body);
    fs.writeFileSync(this.filePath, JSON.stringify(existing, null, 2));
    return { success: true };
  }
}
