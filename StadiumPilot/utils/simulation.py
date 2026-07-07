# Simulates match day events and how they affect different roles

EVENTS = {
    "gate_congestion": {
        "title": "Gate Congestion",
        "description": "Heavy crowding at Gate 3 due to delayed security checks.",
        "fan_message": "Gate 3 is experiencing delays. We recommend using Gate 4 or Gate 5 for faster entry.",
        "volunteer_message": "Please direct fans approaching Gate 3 towards Gates 4 and 5.",
        "security_message": "High density at Gate 3. Deploy 3 additional units to manage the queue and open alternate lanes.",
        "organizer_message": "Gate 3 throughput is down 40%. Recommend coordinating with transport to hold arriving buses slightly or opening emergency lanes."
    },
    "medical_emergency": {
        "title": "Medical Emergency",
        "description": "A fan fainted in Section C, Level 2.",
        "fan_message": "Medical personnel are responding to an incident in Section C. Please keep the aisles clear.",
        "volunteer_message": "Medical incident in Section C. Please help keep the aisles clear and guide medical staff if needed.",
        "security_message": "Medical emergency Section C. Dispatching medics. Secure the perimeter and ensure clear path for stretcher.",
        "organizer_message": "Medical response active in Section C. Average response time currently 3 minutes. Monitor for impact on nearby concession lines."
    },
    "lost_child": {
        "title": "Lost Child",
        "description": "A 5-year-old child wearing a yellow jersey is lost near Food Court A.",
        "fan_message": "If you see a lost 5-year-old in a yellow jersey, please contact the nearest volunteer or security staff.",
        "volunteer_message": "Lost child reported near Food Court A: 5yo, yellow jersey. Escort to Help Desk Zone 2 if found.",
        "security_message": "Code Yellow: Lost child, 5yo, yellow jersey near Food Court A. Monitor CCTV feeds for Zone A.",
        "organizer_message": "Code Yellow active. Ensure PA system announcement is ready if not resolved in 5 minutes."
    },
    "heavy_rain": {
        "title": "Heavy Rain",
        "description": "Sudden downpour causing fans in uncovered sections to seek shelter.",
        "fan_message": "Heavy rain detected. Covered concourses are available on Levels 1 and 2.",
        "volunteer_message": "Direct fans from uncovered sections to concourses. Ensure no slip hazards form near entrances.",
        "security_message": "Monitor crowd movement to covered areas. Prevent overcrowding in narrow concourse bottlenecks.",
        "organizer_message": "Weather alert: Rain. Concourse density increasing. Recommend opening additional indoor concession stands."
    },
    "power_outage": {
        "title": "Partial Power Outage",
        "description": "Lights out in the East Wing concourse.",
        "fan_message": "We are experiencing a temporary power issue in the East Wing. Backup lighting is active.",
        "volunteer_message": "Use flashlights if necessary and calmly reassure fans in the East Wing.",
        "security_message": "Power loss in East Wing. Deploy to key intersections to guide crowd and prevent panic.",
        "organizer_message": "East Wing power fault. Facilities team dispatched. Estimated resolution: 10 mins. Monitor CCTV on battery backup."
    },
    "parking_full": {
        "title": "Parking Full",
        "description": "Main parking lot has reached 100% capacity.",
        "fan_message": "Main parking is full. Please use the North overflow lot or park-and-ride services.",
        "volunteer_message": "Inform arriving cars that main parking is full and direct them to North overflow.",
        "security_message": "Main lot full. Close main gates to vehicles and redirect traffic to North lot.",
        "organizer_message": "Main parking at 100%. Update digital road signs and notify local traffic authorities to redirect flow."
    },
    "food_shortage": {
        "title": "Food Shortage",
        "description": "Food Court A is running out of hot meals.",
        "fan_message": "Food Court B currently has shorter lines and full menus available!",
        "volunteer_message": "If fans ask for food, suggest Food Court B or C as Court A is low on stock.",
        "security_message": "Monitor Food Court A for potential agitation due to long waits and low stock.",
        "organizer_message": "Inventory alert: Food Court A hot meals depleted. Restock requested from central kitchen."
    },
    "vip_arrival": {
        "title": "VIP Arrival",
        "description": "A high-profile VIP convoy is arriving at Gate 1.",
        "fan_message": "Temporary access restrictions around Gate 1. Please use other gates for the next 15 minutes.",
        "volunteer_message": "Keep pathways clear near Gate 1 for VIP transit.",
        "security_message": "VIP convoy 2 minutes out. Secure Gate 1 perimeter and VIP escort route to suites.",
        "organizer_message": "VIP arrival imminent. Ensure hospitality team is ready at the suite level."
    }
}

active_events = []

def trigger_event(event_id):
    if event_id in EVENTS:
        event = EVENTS[event_id]
        event['id'] = event_id
        active_events.insert(0, event) # Add to top
        return True
    return False

def get_active_events():
    return active_events

def clear_events():
    active_events.clear()
