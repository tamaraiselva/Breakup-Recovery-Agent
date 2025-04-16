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

   ```env
   API_KEY="your_gemini_api_key_here"
   API_URL=http://localhost:8000/analyze/
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

### Option 1: Run both services with a single command

```bash
python run_app.py
```

This will start both the FastAPI backend and Streamlit frontend, and open your browser automatically.

### Option 2: Run services separately

Start the FastAPI backend:

```bash
uvicorn app:app --reload --port 8000
```

Start the Streamlit frontend (in a separate terminal):

```bash
streamlit run streamlit_app.py
```

## Usage

1. Enter your thoughts and feelings in the text area
2. Optionally upload relevant images
3. Click "Get Support" to receive personalized guidance
4. Review the different types of support provided by the AI agents

## Requirements

See `requirements.txt` for a complete list of dependencies.

## Deployment

### Deploying to Render.com

This application can be easily deployed to Render.com using the provided `render.yaml` Blueprint:

1. Fork or clone this repository to your GitHub account
2. Create a Render.com account if you don't have one
3. In Render dashboard, click "New" and select "Blueprint"
4. Connect your GitHub repository
5. Render will automatically detect the `render.yaml` file and set up the service
6. Add your Gemini API key as an environment variable named `API_KEY`
7. Deploy the service

### Docker Deployment

You can also deploy using Docker:

```bash
docker build -t breakup-recovery-agent .
docker run -p 8000:8000 -p 8501:8501 -e API_KEY="your_gemini_api_key_here" breakup-recovery-agent
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.
