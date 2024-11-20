# Use the official Python 3.12 image as the base
FROM python:3.12

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Copy the application code
COPY . .

# Expose the port the app will listen on
EXPOSE 8000

# Command to run the app
CMD ["fastapi", "dev", "main.py", "--host", "0.0.0.0", "--port", "8000"]