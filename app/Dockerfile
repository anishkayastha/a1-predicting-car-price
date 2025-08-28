# Use Python 3.12 slim image
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Install uv
RUN pip install uv

# Copy project files
COPY pyproject.toml .
COPY .python-version .

# Install Python dependencies using uv
RUN uv pip install --system -r pyproject.toml

# Copy application code
COPY code/ ./code/

# Expose Streamlit port
EXPOSE 8501

# Set the working directory to code folder
WORKDIR /app/code

# Health check
HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

# Run the Streamlit app
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]