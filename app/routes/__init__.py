from .pdf_to_word import pdf_to_word_blueprint
from .image_to_pdf import image_to_pdf_blueprint

def register_blueprints(app):
    """Register all app blueprints."""
    app.register_blueprint(pdf_to_word_blueprint, url_prefix="/api/pdf-to-word")
    app.register_blueprint(image_to_pdf_blueprint, url_prefix="/api/image-to-pdf")


