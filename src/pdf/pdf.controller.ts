import {
  Controller,
  Post,
  UploadedFile,
  UseInterceptors,
  Body,
} from '@nestjs/common';
import { FileInterceptor } from '@nestjs/platform-express';
import { PdfExtractService } from './services/pdf-extract.service';
import { PdfSaveService } from './services/pdf-save.service';
import { SubmitAnswerDto } from './submit-answer.dto';

@Controller()
export class PdfController {
  constructor(
    private readonly extractService: PdfExtractService,
    private readonly saveService: PdfSaveService,
  ) {}

  @Post('upload-pdf')
  @UseInterceptors(FileInterceptor('pdf_file'))
  async uploadPdf(
    @UploadedFile() file: Express.Multer.File,
    @Body('chapter') chapter: string,
  ) {
    return this.extractService.extractQuestions(file.buffer, chapter);
  }

  @Post('submit-answer')
  async submitAnswer(@Body() body: SubmitAnswerDto) {
    return this.saveService.saveAnswer(body);
  }
}
