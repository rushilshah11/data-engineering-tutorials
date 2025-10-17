# Start from the official Airflow image
FROM apache/airflow:3.1.0

# Switch to root to install OS-level dependencies
USER root
RUN apt-get update && apt-get install -y \
    libpq-dev \
    build-essential \
    # Add any other required build libs if needed, e.g., for matplotlib
    # python3-dev is often required for packages with C extensions
    python3-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Switch back to the Airflow user
USER airflow

# Copy and install Python dependencies
COPY requirements.txt /requirements.txt
RUN pip install --no-cache-dir -r /requirements.txt