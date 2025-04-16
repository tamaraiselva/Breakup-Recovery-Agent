# Fix for Docker Deployment Error

The error you're seeing is because the `google-generativeai` package is missing from your Docker container. This package is required by the `agno` library to work with Google's Gemini API.

## Solution

I've updated the `requirements.txt` file to include the missing package. Follow these steps to fix the issue:

1. Make sure your `requirements.txt` file includes `google-generativeai` (I've already added it)

2. Rebuild your Docker image:
   ```bash
   docker build -t breakup-recovery-agent .
   ```

3. Run the container again:
   ```bash
   docker run -p 8000:8000 -p 8501:8501 -e API_KEY="your_gemini_api_key_here" breakup-recovery-agent
   ```

## Explanation

The error occurred because:
- The `agno` library depends on `google-generativeai` to interact with Google's Gemini API
- This dependency wasn't explicitly listed in your requirements.txt file
- When the Docker container was built, it didn't install this necessary package

By adding `google-generativeai` to your requirements.txt file and rebuilding the Docker image, the container will now have all the necessary dependencies to run your application.

## Additional Troubleshooting

If you encounter any other issues:

1. Check the Docker logs for error messages
2. Verify that your API key is correct and has access to the Gemini API
3. Make sure all environment variables are properly set

Let me know if you need any further assistance with the deployment!
