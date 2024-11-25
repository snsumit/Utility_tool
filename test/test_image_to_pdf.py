def test_pdf_to_word(client):
    """Test PDF to Word conversion."""
    response = client.post("/api/pdf-to-word/", data={"file": open("sample.pdf", "rb")})
    assert response.status_code == 200
    assert "file_path" in response.json

