import subprocess
import sys
import time
import os
import webbrowser
from threading import Thread

def run_fastapi():
    print("Starting FastAPI backend server...")
    # In production, we don't use --reload
    if os.environ.get("ENVIRONMENT") == "production":
        subprocess.run([sys.executable, "-m", "uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"])
    else:
        subprocess.run([sys.executable, "-m", "uvicorn", "app:app", "--reload", "--port", "8000"])

def run_streamlit():
    print("Starting Streamlit frontend...")
    # In production, we need to specify the host as 0.0.0.0 to make it accessible
    if os.environ.get("ENVIRONMENT") == "production":
        subprocess.run([sys.executable, "-m", "streamlit", "run", "streamlit_app.py", "--server.port", "8501", "--server.address", "0.0.0.0"])
    else:
        subprocess.run([sys.executable, "-m", "streamlit", "run", "streamlit_app.py", "--server.port", "8501"])

def open_browser():
    # Only open browser in development mode
    if os.environ.get("ENVIRONMENT") != "production":
        time.sleep(5)  # Wait for servers to start
        print("Opening application in browser...")
        webbrowser.open("http://localhost:8501")  # Open Streamlit app

if __name__ == "__main__":
    # Set default environment if not specified
    if "ENVIRONMENT" not in os.environ:
        os.environ["ENVIRONMENT"] = "development"

    print(f"Starting application in {os.environ.get('ENVIRONMENT')} mode...")

    # Start FastAPI in a separate thread
    fastapi_thread = Thread(target=run_fastapi)
    fastapi_thread.daemon = True  # Thread will exit when main program exits
    fastapi_thread.start()

    # Start browser in a separate thread (only in development)
    if os.environ.get("ENVIRONMENT") != "production":
        browser_thread = Thread(target=open_browser)
        browser_thread.daemon = True
        browser_thread.start()

    # Run Streamlit in the main thread
    run_streamlit()
