from flask import Blueprint, render_template

fan_bp = Blueprint('fan', __name__)

@fan_bp.route('/')
def dashboard():
    return render_template('fan/dashboard.html')
