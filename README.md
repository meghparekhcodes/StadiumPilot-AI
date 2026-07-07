# StadiumPilot AI 🏟️🤖
**The AI Operating System for Smart Stadiums**

A multi-role platform designed for the FIFA World Cup 2026 scenario, utilizing Generative AI to improve stadium operations and the overall tournament experience for fans, organizers, volunteers, and security staff.

## Features ✨
- **Role-Based Dashboards:** Specialized interfaces for Fan, Volunteer, Security, and Organizer.
- **Context-Aware AI Assistants:** Powered by Google Gemini API, each AI assistant is uniquely prompted to serve its specific role (e.g., helpful for fans, safety-first for security).
- **Match Day Simulation Center:** Trigger events like "Gate Congestion" or "Medical Emergency" and see how the AI system dynamically alerts and advises each user type.
- **Premium UI/UX:** Built with modern glassmorphism, smooth animations, dark mode, and responsive design. No frameworks, just pure HTML/CSS/JS.
- **Accessibility Built-In:** High contrast mode and large text options to ensure usability for everyone.
- **Data Visualization:** Interactive charts for Organizers using Chart.js.

## Folder Structure 📂
```
StadiumPilot/
├── ai/
│   ├── gemini.py         # AI integration (Gemini + fallback mock logic)
│   └── prompts.py        # Role-specific system prompts
├── database/
│   └── db.py             # SQLite setup
├── routes/
│   ├── api.py            # Chat and simulation endpoints
│   ├── fan.py            # Fan dashboard
│   ├── main.py           # Home page
│   ├── organizer.py      # Organizer dashboard
│   ├── security.py       # Security dashboard
│   ├── simulation.py     # Simulation center
│   └── volunteer.py      # Volunteer dashboard
├── static/
│   ├── css/
│   │   └── styles.css    # Global styling
│   ├── js/
│   │   ├── charts.js     # Chart.js initialization
│   │   ├── chat.js       # AI Chat logic
│   │   ├── main.js       # Accessibility and global UI logic
│   │   └── simulation.js # Polling for Match Day events
├── templates/            # Jinja2 HTML templates
│   ├── base.html
│   ├── index.html
│   ├── fan/
│   ├── organizer/
│   ├── security/
│   ├── simulation/
│   └── volunteer/
├── app.py                # Application entry point
├── requirements.txt
├── .env.example
├── Procfile
└── README.md
```

## Installation 🛠️

1. **Clone the repository:**
   ```bash
   git clone <repo_url>
   cd StadiumPilot
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Environment Variables:**
   Copy `.env.example` to `.env` and add your Gemini API Key. If you do not add an API key, the application will gracefully fall back to mock AI responses.
   ```bash
   cp .env.example .env
   ```

5. **Initialize Database:**
   ```bash
   python database/db.py
   ```

## Running Locally 🚀
Start the Flask development server:
```bash
python app.py
```
Open `http://localhost:5000` in your web browser.

## Deployment Guide (Render) 🌍
1. Push the code to a GitHub repository.
2. Link the repository on Render (Web Service).
3. Build Command: `pip install -r requirements.txt`
4. Start Command: `gunicorn app:app` (as specified in `Procfile`)
5. Add `GEMINI_API_KEY` to your Environment Variables on Render.

## Future Scope 🔮
- **Live IoT Integration:** Connecting real turnstile and camera data to the AI.
- **Multilingual Voice Capabilities:** Adding speech-to-text and text-to-speech for seamless international fan support.
- **Ticketing Integration:** Allowing fans to scan tickets and receive personalized seating paths.

## License
MIT License
