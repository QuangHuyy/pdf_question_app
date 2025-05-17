import { Injectable } from '@nestjs/common';
import * as pdf from 'pdf-parse';

@Injectable()
export class PdfExtractService {
  async extractQuestions(buffer: Buffer, chapter: string) {
    const data = await pdf(buffer);
    const pattern = new RegExp(`${chapter}.*?(Câu \d+:.*?)\n(Đáp án:.*?)\n`, 'gis');
    const matches = Array.from(data.text.matchAll(pattern));
    return matches.map((m) => ({
      question_text: m[1].trim(),
      answer_text: m[2].trim(),
    }));
  }
}
