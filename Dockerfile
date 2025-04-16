FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --no-cache-dir duckduckgo-search

COPY . .

# Make the start script executable
RUN chmod +x start.sh

# Expose ports for FastAPI and Streamlit
EXPOSE 8000
EXPOSE 8501

# Run the application
CMD ["./start.sh"]
