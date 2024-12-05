import os

class Config:
    # Secret key for signing cookies and sessions; use an environment variable in production
    SECRET_KEY = os.getenv('SECRET_KEY', 'default_secret_key')  # Default secret key for development
    
    # Folder to store uploaded files, located in the instance folder
    UPLOAD_FOLDER = os.path.join(os.getenv('FLASK_INSTANCE_PATH', 'instance'), 'uploads')
    
    # Max file size for uploads (16MB in this case)
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16 MB
    
   