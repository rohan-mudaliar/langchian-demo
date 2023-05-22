FROM python:3.8

# Install Java
RUN apt-get update && \
    apt-get install -y --no-install-recommends openjdk-11-jdk-headless && \
    rm -rf /var/lib/apt/lists/*

# Set the JAVA_HOME environment variable
ENV JAVA_HOME=/usr/local/openjdk-11

# Copy your application files to the container
COPY . /app
WORKDIR /app

# Install Python dependencies
RUN pip3 install --no-cache-dir -r requirements.txt

# Start the Streamlit application
CMD ["streamlit", "run", "app.py"]
