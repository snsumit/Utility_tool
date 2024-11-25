import os
from PyPDF2 import PdfReader
from docx import Document
from PIL import Image

def convert_pdf_to_word(pdf_path):
    """Convert a PDF file to Word."""
    word_path = pdf_path.replace(".pdf", ".docx")
    doc = Document()
    reader = PdfReader(pdf_path)
    for page in reader.pages:
        doc.add_paragraph(page.extract_text())
    doc.save(word_path)
    return word_path

def convert_images_to_pdf(image_paths):
    """Convert image files to a single PDF."""
    images = [Image.open(image).convert("RGB") for image in image_paths]
    pdf_path = os.path.join("instance/uploads", "output.pdf")
    images[0].save(pdf_path, save_all=True, append_images=images[1:])
    return pdf_path
