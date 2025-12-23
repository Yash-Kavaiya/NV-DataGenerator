
# Use Python 3.10 slim image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Install system dependencies if needed (e.g. for some python packages)
# RUN apt-get update && apt-get install -y build-essential

# Copy project files
COPY . .

# Install dependencies
# We use pip to install directly from pyproject.toml if possible, or export requirements
# Since it uses hatchling, we can try installing the current directory
RUN pip install --no-cache-dir .

# Expose port
EXPOSE 8080

# Run the application
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]
