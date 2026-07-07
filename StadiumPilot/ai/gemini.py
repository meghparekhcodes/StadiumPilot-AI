import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

api_key = os.environ.get("GEMINI_API_KEY")
is_mock = False

if api_key and api_key != "your_gemini_api_key_here":
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-2.5-flash')
else:
    is_mock = True

def get_ai_response(prompt, system_prompt, role):
    if is_mock:
        return _get_mock_response(prompt, role)
    
    try:
        # Gemini 2.5 Flash supports system instructions
        model = genai.GenerativeModel(
            model_name='gemini-2.5-flash',
            system_instruction=system_prompt
        )
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        print(f"Gemini API Error: {e}")
        return _get_mock_response(prompt, role)

def _get_mock_response(prompt, role):
    # Fallback mock responses based on role
    prompt_lower = prompt.lower()
    if role == 'fan':
        if 'gate 5' in prompt_lower:
            return "Gate 5 is located on the East side of the stadium, near Section B. Just follow the blue signs from the main concourse."
        elif 'vegetarian' in prompt_lower or 'food' in prompt_lower:
            return "There is a great vegetarian stall called 'Green Bites' just behind Section C on Level 1. It's a 2-minute walk from there."
        elif 'translate' in prompt_lower:
            return "Translation: [Mock Translation output for your request]."
        else:
            return f"Mock Fan AI: I can help you find seats, food, or answer match questions. (Your prompt: {prompt})"
            
    elif role == 'volunteer':
        if 'lost child' in prompt_lower:
            return "- Escort the child to the nearest Help Desk (Zone 2).\n- Contact Security via your radio on Channel 4.\n- I will generate an announcement suggestion for the PA system."
        else:
            return f"Mock Volunteer AI: I can provide operational guidance for incidents. (Your prompt: {prompt})"
            
    elif role == 'security':
        if 'crowd' in prompt_lower or 'gate 3' in prompt_lower:
            return "RISK LEVEL: Elevated.\nRECOMMENDATION:\n1. Open nearby Gate 4 to ease congestion.\n2. Deploy 2 additional staff to manage the queue.\n3. Suggest alternate routing via PA system."
        else:
            return f"Mock Security AI: Standby for safety recommendations. (Your prompt: {prompt})"
            
    elif role == 'organizer':
        if 'food court' in prompt_lower or 'overloaded' in prompt_lower:
            return "INSIGHT: Food Court A is currently at 95% capacity.\nRECOMMENDATION:\n- Open temporary food stations in Concourse B.\n- Redirect visitors via the stadium app notifications.\n- Dispatch extra cleaning staff to Area A."
        else:
            return f"Mock Organizer AI: Ready to provide operational insights. (Your prompt: {prompt})"

    return "Mock AI: How can I help?"
