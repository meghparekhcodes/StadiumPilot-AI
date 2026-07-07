from flask import Blueprint, request, jsonify
from ai.gemini import get_ai_response
from ai.prompts import FAN_SYSTEM_PROMPT, VOLUNTEER_SYSTEM_PROMPT, SECURITY_SYSTEM_PROMPT, ORGANIZER_SYSTEM_PROMPT
from utils.simulation import trigger_event, get_active_events, clear_events

api_bp = Blueprint('api', __name__)

# Map roles to their prompts
PROMPTS = {
    'fan': FAN_SYSTEM_PROMPT,
    'volunteer': VOLUNTEER_SYSTEM_PROMPT,
    'security': SECURITY_SYSTEM_PROMPT,
    'organizer': ORGANIZER_SYSTEM_PROMPT
}

@api_bp.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    message = data.get('message', '')
    role = data.get('role', 'fan')

    if not message:
        return jsonify({'error': 'Message is required'}), 400

    system_prompt = PROMPTS.get(role, FAN_SYSTEM_PROMPT)
    
    # Call Gemini API or Mock
    response_text = get_ai_response(message, system_prompt, role)

    return jsonify({'response': response_text})

@api_bp.route('/simulation/trigger', methods=['POST'])
def trigger_sim_event():
    data = request.get_json()
    event_id = data.get('event_id')
    
    success = trigger_event(event_id)
    if success:
        return jsonify({'status': 'success', 'message': f'Event {event_id} triggered'})
    return jsonify({'status': 'error', 'message': 'Event not found'}), 404

@api_bp.route('/simulation/events', methods=['GET'])
def get_events():
    events = get_active_events()
    return jsonify({'events': events})

@api_bp.route('/simulation/clear', methods=['POST'])
def clear_sim_events():
    clear_events()
    return jsonify({'status': 'success', 'message': 'Events cleared'})
