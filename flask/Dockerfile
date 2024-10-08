# Use the official Python image from Docker Hub
FROM python:3.12.0

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the requirements.txt file into the container
COPY requirements.txt ./

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Set environment variables for Flask
ENV FLASK_APP=hello.py
ENV FLASK_ENV=development

# Expose the port the app runs on (5000 by default)
EXPOSE 5000

# Run the Flask app using the development server
CMD ["flask", "run", "--host=0.0.0.0", "--debug"]