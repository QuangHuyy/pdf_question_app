import { Module } from '@nestjs/common';
import { PdfController } from './pdf.controller';
import { PdfExtractService } from './services/pdf-extract.service';
import { PdfSaveService } from './services/pdf-save.service';

@Module({
  controllers: [PdfController],
  providers: [PdfExtractService, PdfSaveService],
})
export class PdfModule {}
