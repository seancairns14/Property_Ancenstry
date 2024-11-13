FROM python:3.10

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Copy requirements file and install dependencies
COPY requirements.txt .
RUN echo "Upgrading pip..." && \
    pip install --upgrade pip
RUN echo "Installing dependencies from requirements.txt..." && \
    pip install --no-cache-dir -r requirements.txt -v

# Copy application files
COPY . .

# Running migrations
RUN echo "Running Django migrations..." && \
    python manage.py migrate

# Gunicorn command with console logging enabled
CMD ["gunicorn", "--config", "gunicorn-cfg.py", "--access-logfile", "-", "--error-logfile", "-", "core.wsgi"]

