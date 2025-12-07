# Use official Python image
FROM python:3.10-slim

# Set working directory inside container
WORKDIR /app

# Copy requirements first (for caching)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project
COPY . .

# Expose port 5000 (Flask default)
EXPOSE 5000

# Set working directory to Flask app folder
WORKDIR /app/app

# Run Flask app
CMD ["python", "app.py"]
