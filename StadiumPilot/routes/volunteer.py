from flask import Blueprint, render_template

volunteer_bp = Blueprint('volunteer', __name__)

@volunteer_bp.route('/')
def dashboard():
    return render_template('volunteer/dashboard.html')
