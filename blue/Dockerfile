FROM python:3.7.3-stretch

## Step 1:
# Create a working directory
WORKDIR /app

## Step 2:
# Copy source code to working directory
COPY blue_app.py /app/

## Step 3:
# Expose port 8080
EXPOSE 8080

## Step 4:
# Run app.py at container launch
CMD ["python3", "blue_app.py"]
