# Fix for Docker Deployment Error

The error you're seeing is because the `duckduckgo-search` package is missing from your Docker container. This package is required by the `agno.tools.duckduckgo` module which is used by the Brutal Honesty Agent.

## Solution

I've updated the `requirements.txt` and `Dockerfile` to include the missing package. Follow these steps to fix the issue:

1. Make sure your `requirements.txt` file includes `duckduckgo-search` (I've already added it)

2. Rebuild your Docker image:
   ```bash
   docker build -t breakup-recovery-agent .
   ```

3. Run the container again:
   ```bash
   docker run -p 8000:8000 -p 8501:8501 -e API_KEY="your_gemini_api_key_here" breakup-recovery-agent
   ```

## Alternative Solution

If you don't want to rebuild the Docker image, I've also modified the `app.py` file to gracefully handle the missing dependency. The Brutal Honesty Agent will run without search capabilities, but the application will still function.

## Explanation

The error occurred because:
- The `agno.tools.duckduckgo` module depends on the `duckduckgo-search` package
- This dependency wasn't explicitly listed in your requirements.txt file
- When the Docker container was built, it didn't install this necessary package

By adding `duckduckgo-search` to your requirements.txt file and rebuilding the Docker image, the container will now have all the necessary dependencies to run your application.

## Additional Troubleshooting

If you encounter any other issues:

1. Check the Docker logs for error messages
2. Verify that your API key is correct and has access to the Gemini API
3. Make sure all environment variables are properly set

Let me know if you need any further assistance with the deployment!
