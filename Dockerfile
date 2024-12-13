# base image
FROM python:3.9-slim

# Set the working directory in the cont
WORKDIR /app

# Copy the requirements.txt 
COPY requirements.txt .

# Install the dependencies 
RUN pip install -r requirements.txt

# Copy the project directory 
COPY . .

# Run the codeKata.py 
CMD ["python", "codeKata.py"]
