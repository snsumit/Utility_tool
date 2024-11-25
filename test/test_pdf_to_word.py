def test_image_to_pdf(client):
    """Test Image to PDF conversion."""
    response = client.post("/api/image-to-pdf/", data={"files[]": [open("image1.png", "rb")]})
    assert response.status_code == 200
    assert "file_path" in response.json


