from flask import Blueprint, render_template
from utils.mock_data import STADIUM_KPI, MOCK_CHART_DATA

organizer_bp = Blueprint('organizer', __name__)

@organizer_bp.route('/')
def dashboard():
    return render_template('organizer/dashboard.html', kpi=STADIUM_KPI, chart_data=MOCK_CHART_DATA)
