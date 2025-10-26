FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the application code

COPY . /app/

# Install dependencies from requirements.txt
RUN pip install --no-cache-dir -e .

# Expose the port that Flask will run on
EXPOSE 5000

# Command to run the app
CMD ["python", "application.py"]