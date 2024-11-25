from app import create_app

app = create_app()
@app.route("/")
def home():
    return "Welcome to the File Converter API. Use /api/pdf-to-word/ or /api/image-to-pdf/"


if __name__ == "__main__":
    app.run(debug=True)


