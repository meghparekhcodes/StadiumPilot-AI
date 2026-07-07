from flask import Blueprint, render_template
from utils.simulation import EVENTS

simulation_bp = Blueprint('simulation', __name__)

@simulation_bp.route('/')
def center():
    return render_template('simulation/center.html', events=EVENTS)
