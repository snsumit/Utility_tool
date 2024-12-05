from app import create_app
from flask_cors import CORS

app = create_app()
CORS(app, resources={r"/api/*": {"origins": "http://localhost:3000"}})
@app.route("/")
def home():
    return "Welcome to the File Converter API. Use /api/pdf-to-word/ or /api/image-to-pdf/"


if __name__ == "__main__":
    app.run(debug=True)


