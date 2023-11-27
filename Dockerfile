# Use the official Python image as a base image
FROM python:3.12

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install virtualenv
RUN pip install virtualenv

# Create a virtual environment and activate it
RUN python -m venv venv
ENV PATH="/app/venv/bin:$PATH"

# Create and set the working directory
WORKDIR /libraryAPI

# Install dependencies
COPY requirements.txt /libraryAPI/
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy the project code into the container
COPY . /libraryAPI/

# Expose the port the app will run on
EXPOSE 8000

# Command to run the application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
