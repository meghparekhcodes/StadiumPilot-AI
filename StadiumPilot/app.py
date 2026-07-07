import os
from flask import Flask, render_template
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'default-dev-key')

    # Register Blueprints
    from routes.main import main_bp
    from routes.fan import fan_bp
    from routes.volunteer import volunteer_bp
    from routes.security import security_bp
    from routes.organizer import organizer_bp
    from routes.simulation import simulation_bp
    from routes.api import api_bp

    app.register_blueprint(main_bp)
    app.register_blueprint(fan_bp, url_prefix='/fan')
    app.register_blueprint(volunteer_bp, url_prefix='/volunteer')
    app.register_blueprint(security_bp, url_prefix='/security')
    app.register_blueprint(organizer_bp, url_prefix='/organizer')
    app.register_blueprint(simulation_bp, url_prefix='/simulation')
    app.register_blueprint(api_bp, url_prefix='/api')

    @app.errorhandler(404)
    def page_not_found(e):
        return render_template('404.html'), 404

    return app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
