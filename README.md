# Breakup Recovery Assistant

A comprehensive application that provides emotional support and guidance for individuals going through a breakup. The application uses AI agents to offer therapeutic support, closure guidance, recovery planning, and honest feedback.

## Features

- 🤝 **Therapist Agent**: Provides empathetic support and validation
- ✉️ **Closure Agent**: Helps craft emotional messages and find closure
- 📅 **Routine Planner**: Creates a 7-day recovery plan
- 💪 **Brutal Honesty Agent**: Gives direct feedback and truth

## Architecture

- **Backend**: FastAPI application with multiple AI agents using the Agno library
- **Frontend**: Streamlit web interface for user interaction
- **Integration**: Python script to run both services together

## Setup

1. Clone this repository
2. Create a `.env` file with your API key:
   ```
   API_KEY="your_gemini_api_key_here"
   API_URL=http://localhost:8000/analyze/
   ```
3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

## Running the Application

### Option 1: Run both services with a single command

```
python run_app.py
```

This will start both the FastAPI backend and Streamlit frontend, and open your browser automatically.

### Option 2: Run services separately

Start the FastAPI backend:
```
uvicorn app:app --reload --port 8000
```

Start the Streamlit frontend (in a separate terminal):
```
streamlit run streamlit_app.py
```

## Usage

1. Enter your thoughts and feelings in the text area
2. Optionally upload relevant images
3. Click "Get Support" to receive personalized guidance
4. Review the different types of support provided by the AI agents

## Requirements

See `requirements.txt` for a complete list of dependencies.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
