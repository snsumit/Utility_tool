from flask import Blueprint, request, jsonify, send_from_directory
from werkzeug.utils import secure_filename
import os
import logging
from app.utils.file_handlers import convert_images_to_pdf 

image_to_pdf_blueprint = Blueprint("image_to_pdf", __name__)

@image_to_pdf_blueprint.route("/download/<filename>", methods=["GET"])
def download_file(filename):
    """Endpoint to download the converted PDF file."""
    return send_from_directory(os.path.abspath("instance/uploads"), filename, as_attachment=True)

@image_to_pdf_blueprint.route("/", methods=["POST"])
def image_to_pdf():
    """Endpoint to convert images to a single PDF."""
    if 'files[]' not in request.files:
        return jsonify({"error": "No file part in the request"}), 400

    files = request.files.getlist("files[]")
    if not files or all(file.filename == '' for file in files):
        return jsonify({"error": "No files selected"}), 400

    saved_files = []
    try:
        upload_dir = os.path.join("instance/uploads")
        os.makedirs(upload_dir, exist_ok=True)

        for file in files:
            filename = secure_filename(file.filename)
            upload_path = os.path.join(upload_dir, filename)

            # Save the file
            file.save(upload_path)
            saved_files.append(upload_path)

            # Validate file size
            if os.path.getsize(upload_path) > 10 * 1024 * 1024:  # 10MB
                os.remove(upload_path)
                return jsonify({"error": f"File {file.filename} exceeds size limit of 10MB"}), 400

           

        pdf_file_path = convert_images_to_pdf(saved_files)
        return jsonify({
            "message": "Conversion successful",
            "download_url": f"/api/image-to-pdf/download/{os.path.basename(pdf_file_path)}"
        }), 200

    except Exception as e:
        logging.error(f"Failed to convert images: {e}")
        return jsonify({"error": f"Failed to convert images: {str(e)}"}), 500

    finally:
        for filepath in saved_files:
            try:
                os.remove(filepath)
            except Exception as cleanup_error:
                logging.error(f"Failed to clean up file {filepath}: {cleanup_error}")
