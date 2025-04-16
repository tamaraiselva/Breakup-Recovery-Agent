# Deployment Guide for Breakup Recovery Agent

This guide provides detailed instructions for deploying the Breakup Recovery Agent to various platforms.

## Prerequisites

Before deploying, make sure you have:

1. A Gemini API key from Google AI Studio
2. Git installed on your machine
3. Docker installed (optional, for Docker deployment)

## Deployment Options

### 1. Render.com (Recommended)

Render.com provides a simple way to deploy both the FastAPI backend and Streamlit frontend together.

#### Render Deployment Steps

1. Fork or clone this repository to your GitHub account
2. Create a Render.com account at `https://render.com`
3. In the Render dashboard, click "New" and select "Blueprint"
4. Connect your GitHub repository
5. Render will automatically detect the `render.yaml` file and set up the service
6. Add your Gemini API key as an environment variable named `API_KEY`
7. Click "Apply" to deploy the service
8. Wait for the deployment to complete (this may take a few minutes)
9. Once deployed, your application will be available at the URL provided by Render

### 2. Docker Deployment

You can deploy the application using Docker on any platform that supports Docker containers.

#### Docker Deployment Steps

1. Clone the repository to your local machine or server
2. Navigate to the project directory
3. Build the Docker image:

   ```bash
   docker build -t breakup-recovery-agent .
   ```

4. Run the Docker container:

   ```bash
   docker run -p 8000:8000 -p 8501:8501 -e API_KEY="your_gemini_api_key_here" breakup-recovery-agent
   ```

5. Access the application at `http://localhost:8501`

### 3. Manual Deployment

You can also deploy the application manually on any server that supports Python.

#### Manual Deployment Steps

1. Clone the repository to your server
2. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file with your API key:

   ```env
   API_KEY="your_gemini_api_key_here"
   API_URL=http://your-server-address:8000/analyze/
   ```

4. Start the application:

   ```bash
   python run_app.py
   ```

5. Configure your server to keep the process running (using systemd, supervisor, or similar)
6. Set up a reverse proxy (like Nginx) to forward requests to the appropriate ports

## Troubleshooting

### Common Issues

1. **API Key Issues**: Make sure your Gemini API key is correctly set in the environment variables
2. **Port Conflicts**: If ports 8000 or 8501 are already in use, you may need to modify the ports in the code
3. **Dependencies**: Ensure all dependencies are correctly installed
4. **CORS Issues**: If you're deploying the frontend and backend separately, you may need to update the CORS settings in `app.py`

### Getting Help

If you encounter any issues during deployment, please:

1. Check the application logs for error messages
2. Refer to the documentation for the deployment platform you're using
3. Open an issue in the GitHub repository with details about the problem

## Post-Deployment

After successful deployment:

1. Test the application thoroughly to ensure all features work correctly
2. Update the API_URL in the `.env` file if necessary
3. Consider setting up monitoring and alerts for your deployed application
4. Set up regular backups if you're storing any user data
