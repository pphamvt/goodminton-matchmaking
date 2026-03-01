# Use Python 3.12 as the base image
FROM --platform=linux/amd64 python:3.12-slim

# Install dependencies for the container
RUN apt-get update && apt-get install -y \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Install pip (Python package manager)
RUN pip install --upgrade pip

# Install Python dependencies dynamically
COPY ../../src/requirements.txt .
RUN pip install -r requirements.txt

# Set the working directory inside the container
WORKDIR /app

# Expose port for Django development
EXPOSE 8000

CMD ["bash"]