# ---- Base image ----
FROM --platform=linux/amd64 python:3.12-slim

# Prevent Python from writing pyc files & enable stdout logging
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set work directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Add your application user to group 1000
RUN usermod -a -G 1000 your-app-user

# Upgrade pip
RUN pip install --upgrade pip

# Copy requirements first (better layer caching)
COPY src/requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy project
COPY src/ .

# Secret file
RUN --mount=type=secret,id=_env,dst=/app/.env cat /src/config/settings.ini

# Expose Django port
EXPOSE 8000

# Run with Gunicorn (production server)
CMD ["gunicorn", "goodminton.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "3"]