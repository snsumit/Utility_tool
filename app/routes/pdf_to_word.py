from flask import Blueprint, request, jsonify
from werkzeug.utils import secure_filename
from app.utils.file_handlers import convert_pdf_to_word
import os

pdf_to_word_blueprint = Blueprint("pdf_to_word", __name__)

@pdf_to_word_blueprint.route("/", methods=["POST"])
def pdf_to_word():
    """Endpoint to convert PDF to Word."""
    if "file" not in request.files:
        return jsonify({"error": "No file provided"}), 400

    file = request.files["file"]
    if not file.filename.endswith(".pdf"):
        return jsonify({"error": "Invalid file type. Please upload a PDF."}), 400

    filename = secure_filename(file.filename)
    upload_path = os.path.join("instance/uploads", filename)
    file.save(upload_path)

    try:
        word_file_path = convert_pdf_to_word(upload_path)
        return jsonify({"message": "Conversion successful", "file_path": word_file_path}), 200
    except Exception as e:
        return jsonify({"error": f"Failed to convert PDF: {str(e)}"}), 500

