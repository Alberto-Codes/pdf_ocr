from docling.pipeline.standard_pdf_pipeline import StandardPdfPipeline
from docling.datamodel.pipeline_options import PdfPipelineOptions
from docling.document_converter import DocumentConverter, PdfFormatOption
from docling.datamodel.base_models import InputFormat


artifacts_path = StandardPdfPipeline.download_models_hf(local_dir=".\\artifacts")


pipeline_options = PdfPipelineOptions(artifacts_path=artifacts_path)

source = "https://arxiv.org/pdf/2408.09869" 
converter = DocumentConverter(format_options={
        InputFormat.PDF: PdfFormatOption(pipeline_options=pipeline_options)
    })
result = converter.convert(source)
print(result.document.export_to_markdown())  
