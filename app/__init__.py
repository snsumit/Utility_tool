import os
from flask import Flask
from app.routes import register_blueprints

def create_app(test_config=None):
    """Create and configure the Flask application.
    
    Args:
        test_config (dict, optional): Test configuration to override default config
    
    Returns:
        Flask: Configured Flask application instance
    """
    app = Flask(__name__, instance_relative_config=True)
    
    try:
        # Ensure the instance folder exists
        os.makedirs(app.instance_path, exist_ok=True)
        
        if test_config is None:
            # Load the default configuration
            app.config.from_object("config")
            
            # Load instance config, if it exists
            if os.path.exists(os.path.join(app.instance_path, 'config.py')):
                app.config.from_pyfile('config.py')
        else:
            # Load the test config if passed in
            app.config.update(test_config)
            
        # Configure upload folder
        upload_folder = os.path.join(app.instance_path, "uploads")
        os.makedirs(upload_folder, exist_ok=True)
        app.config['UPLOAD_FOLDER'] = upload_folder
        
        # Initialize blueprints
        register_blueprints(app)
        
        return app
        
    except Exception as e:
        raise RuntimeError(f"Failed to create Flask app: {str(e)}")