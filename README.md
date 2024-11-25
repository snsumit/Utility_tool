# File Converter API

## Overview
The **File Converter API** is a backend service built with Python and Flask to handle file conversion tasks. Currently, it provides two key features:
 **PDF to Word Conversion**: Convert PDF files into editable Word documents.
**Image to PDF Conversion**: Combine multiple images into a single PDF file.

The project is designed to be modular, secure, scalable, and easy to extend for future requirements.



## Features
 **PDF to Word**: Converts a PDF file into a `.docx` format using `pdf2docx`.
 **Image to PDF**: Combines multiple image files into a single PDF using `Pillow`.
 Modular architecture using Flask Blueprints.
 File validation to ensure only valid inputs are processed.
Comprehensive error handling and informative API responses.



## Project Structure
flask-file-converter/
├── app/
│   ├── __init__.py       # App factory and blueprint registration
│   ├── routes/
│   │   ├── __init__.py   # Blueprint imports
│   │   ├── pdf_to_word.py  # PDF to Word conversion route
│   │   ├── image_to_pdf.py  # Image to PDF conversion route
│   └── utils/
│       ├── file_handler.py  # File upload validation logic
├── instance/
│   ├── uploads/          # Folder for storing uploaded files
├── tests/
│   ├── test_pdf_to_word.py  # Unit tests for PDF to Word
│   ├── test_image_to_pdf.py  # Unit tests for Image to PDF
├── app.py                # Main Flask app entry point
├── config.py             # Configuration settings
├── requirements.txt      # Python dependencies
├── README.md             # Project documentation
├── .gitignore            # Git ignore file
