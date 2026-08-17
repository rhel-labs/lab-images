# Use RHHI builder image to get rpm and make run a little easier
FROM registry.access.redhat.com/hi/python:3.11-builder

# Set the working directory in the container
WORKDIR /app

# Create the application venv and add the requirements to install
RUN python3 -m venv /app/venv
COPY --chown=65532 app/requirements.txt .
RUN /app/venv/bin/pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
# Ensure ownership is set to the default non-root user 
COPY --chown=65532 app/ .

# Expose the port Gunicorn will run on
EXPOSE 8000

# Set environment variables 
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1
ENV PATH="/app/venv/bin:$PATH"

# Define the command to run the application using Gunicorn
CMD ["gunicorn", "--workers", "2", "--bind", "0.0.0.0:8000", "app:app"]
