FROM python:3.9-slim

# Create directories
RUN mkdir -p /home/data /home/data/output

# Copy the Python script and data files
COPY script.py /app/script.py
COPY IF.txt /home/data/IF.txt
COPY AlwaysRememberUsThisWay.txt /home/data/AlwaysRememberUsThisWay.txt

# Set working directory
WORKDIR /app

# Run the script automatically when the container starts
CMD ["python", "script.py"]
