# Car Price Prediction App

A machine learning web application built with Streamlit that predicts car prices based on car features like manufacturing year, fuel type, and maximum power.

## Project Structure

## Quick Start

### Prerequisites

- Docker and Docker Compose installed on your system
- Git (for cloning the repository)

### Option 1: Using Docker Compose (Recommended)

1. **Clone the repository:**

   ```bash
   git clone <your-repo-url>
   cd app
   ```

2. **Start the application:**

   ```bash
   docker-compose up --build
   ```

3. **Access the app:**
   Open your browser and navigate to `http://localhost:8501`

4. **Stop the application:**
   ```bash
   docker-compose down
   ```

### Option 2: Using uv (Local Development)

1. **Clone the repository:**

   ```bash
   git clone <your-repo-url>
   cd app
   ```

2. **Install uv (if not already installed):**

   ```bash
   # On macOS/Linux
   curl -LsSf https://astral.sh/uv/install.sh | sh

   # On Windows (PowerShell)
   powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
   ```

3. **Install dependencies:**

   ```bash
   uv pip install -r pyproject.toml
   ```

4. **Run the application:**

   ```bash
   cd code
   streamlit run app.py
   ```

5. **Access the app:**
   Open your browser and navigate to `http://localhost:8501`

## How to Use the App

1. **Manufacturing Year**: Use the slider to select the car's manufacturing year (1990-2024)
2. **Fuel Type**: Choose between Diesel or Petrol
3. **Max Power**: Adjust the slider to set the car's maximum power in BHP (0-200)
4. **Predict**: Click the "Predict Price" button to get the estimated car price

## Model Information

The application uses a pre-trained machine learning model (`car-price.model`) that predicts car prices based on:

- Manufacturing year
- Fuel type (encoded as Diesel=0, Petrol=1)
- Maximum power in BHP
