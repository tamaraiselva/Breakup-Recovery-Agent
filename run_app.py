import subprocess
import sys
import time
import os
import webbrowser
from threading import Thread

def run_fastapi():
    print("Starting FastAPI backend server...")
    if os.environ.get("ENVIRONMENT") == "production":
        subprocess.run([sys.executable, "-m", "uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"])
    else:
        subprocess.run([sys.executable, "-m", "uvicorn", "app:app", "--reload", "--port", "8000"])

def run_streamlit():
    print("Starting Streamlit frontend...")
    if os.environ.get("ENVIRONMENT") == "production":
        subprocess.run([sys.executable, "-m", "streamlit", "run", "streamlit_app.py", "--host", "0.0.0.0", "--server.port", "8501"])
    else:
        subprocess.run([sys.executable, "-m", "streamlit", "run", "streamlit_app.py", "--server.port", "8501"])

def open_browser():
    if os.environ.get("ENVIRONMENT") != "production":
        time.sleep(5)
        print("Opening application in browser...")
        webbrowser.open("http://localhost:8501")

if __name__ == "__main__":
    if "ENVIRONMENT" not in os.environ:
        os.environ["ENVIRONMENT"] = "development"

    print(f"Starting application in {os.environ.get('ENVIRONMENT')} mode...")

    fastapi_thread = Thread(target=run_fastapi)
    fastapi_thread.daemon = True
    fastapi_thread.start()

    if os.environ.get("ENVIRONMENT") != "production":
        browser_thread = Thread(target=open_browser)
        browser_thread.daemon = True
        browser_thread.start()

    run_streamlit()
