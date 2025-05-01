# Use official Python base image
FROM python:3.11-slim

# Set work directory
WORKDIR /app

# Copy your project files
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Run the main script
CMD ["python", "legacy_airline_system_refactored.py"]
