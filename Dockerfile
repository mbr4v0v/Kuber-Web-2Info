FROM ubuntu:22.04

# Install dependencies
RUN apt-get update && apt-get install -y python3 python3-pip

# Set working directory
WORKDIR /app

# Copy the application files
COPY . /app/

# Install Python dependencies
RUN pip3 install -r requirements.txt

# Expose port 5000
EXPOSE 5000

# Set environment variables (optional, but good practice)
ENV FLASK_APP=conip.py
ENV FLASK_RUN_HOST=0.0.0.0

# Run the application
CMD ["flask", "run", "--host=0.0.0.0"]
