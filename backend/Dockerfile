FROM python:3.12-slim

# Set the directory where the commands will run inside of the container
WORKDIR /app

# Copy dependency list
COPY requirements.txt ./

# Install the list
RUN pip install --no-cache-dir -r requirements.txt

# COPY the rest of application code
COPY . .

# Document port listem us
EXPOSE 8000

# The commands runs when the container is started
CMD ["uvicorn", "app.main:app", "--host","0.0.0.0", "--port", "8000"]