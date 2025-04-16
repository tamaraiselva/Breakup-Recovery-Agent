import subprocess
import sys
import time
import os
import webbrowser
from threading import Thread

def run_fastapi():
    print("Starting FastAPI backend server...")
    subprocess.run([sys.executable, "-m", "uvicorn", "app:app", "--reload", "--port", "8000"])

def run_streamlit():
    print("Starting Streamlit frontend...")
    subprocess.run([sys.executable, "-m", "streamlit", "run", "streamlit_app.py", "--server.port", "8501"])

def open_browser():
    time.sleep(5)  # Wait for servers to start
    print("Opening application in browser...")
    webbrowser.open("http://localhost:8501")  # Open Streamlit app

if __name__ == "__main__":
    # Start FastAPI in a separate thread
    fastapi_thread = Thread(target=run_fastapi)
    fastapi_thread.daemon = True  # Thread will exit when main program exits
    fastapi_thread.start()
    
    # Start browser in a separate thread
    browser_thread = Thread(target=open_browser)
    browser_thread.daemon = True
    browser_thread.start()
    
    # Run Streamlit in the main thread
    run_streamlit()
