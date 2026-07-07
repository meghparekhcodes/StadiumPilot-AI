from flask import Blueprint, render_template

security_bp = Blueprint('security', __name__)

@security_bp.route('/')
def dashboard():
    return render_template('security/dashboard.html')
