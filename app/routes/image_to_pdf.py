from flask import Blueprint, request, jsonify
from werkzeug.utils import secure_filename
from app.utils.file_handlers import convert_images_to_pdf
import os

image_to_pdf_blueprint = Blueprint("image_to_pdf", __name__)

@image_to_pdf_blueprint.route("/", methods=["POST"])
def image_to_pdf():
    """Endpoint to convert images to a single PDF."""
    files = request.files.getlist("files[]")
    if not files:
        return jsonify({"error": "No files provided"}), 400

    filenames = []
    for file in files:
        if not file.filename.lower().endswith((".png", ".jpg", ".jpeg")):
            return jsonify({"error": f"Invalid file type for {file.filename}"}), 400

        filename = secure_filename(file.filename)
        upload_path = os.path.join("instance/uploads", filename)
        file.save(upload_path)
        filenames.append(upload_path)

    try:
        pdf_file_path = convert_images_to_pdf(filenames)
        return jsonify({"message": "Conversion successful", "file_path": pdf_file_path}), 200
    except Exception as e:
        return jsonify({"error": f"Failed to convert images: {str(e)}"}), 500
