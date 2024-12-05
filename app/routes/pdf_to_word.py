from flask import Blueprint, request, jsonify ,send_from_directory
from werkzeug.utils import secure_filename
from app.utils.file_handlers import convert_pdf_to_word
import os

pdf_to_word_blueprint = Blueprint("pdf_to_word", __name__)

@pdf_to_word_blueprint.route("/download/<filename>", methods=["GET"])
def download_file(filename):
    """Endpoint to download the converted Word file."""
    
    return send_from_directory(os.path.abspath("instance/uploads"), filename, as_attachment=True)

@pdf_to_word_blueprint.route("/", methods=["POST"])
def pdf_to_word():
    """Endpoint to convert PDF to Word."""
    if "file" not in request.files:
        return jsonify({"error": "No file provided"}), 400

    file = request.files["file"]
    if file.filename=='':
        return jsonify({"error":'No selected file'})

    if not file.filename.endswith(".pdf"):
        return jsonify({"error": "Invalid file type. Please upload a PDF."}), 400

    filename = secure_filename(file.filename)
    upload_path = os.path.join("instance/uploads", filename)
    # Ensure upload directory exists
    os.makedirs(os.path.dirname(upload_path),exist_ok=True)
    try:
       file.save(upload_path)
       word_file_path = convert_pdf_to_word(upload_path)
       os.remove(upload_path)
       return jsonify({"message": "Conversion successful", "file_path": word_file_path}), 200
    except Exception as e:
        #clean up any uploaded file in case of error
        if os.path.exists(upload_path):
             os.remove(upload_path)
        return jsonify({"error": f"Failed to convert PDF: {str(e)}"}), 500

