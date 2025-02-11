#!/bin/bash

# Ensure the script is being run from the correct directory
echo "Running from: $(pwd)"

# Stop any running containers
echo "Stopping existing containers..."
docker-compose down --volumes --remove-orphans

# Build the containers without using cache (to ensure a fresh build)
echo "Building Docker containers..."
docker-compose build --no-cache

# Start the containers in detached mode
echo "Starting Docker containers..."
docker-compose up -d

# Check if the containers are running
echo "Checking Docker container status..."
docker-compose ps

# Optional: Tail logs for debugging if something goes wrong
echo "Tailing logs for frontend and backend..."
docker-compose logs -f frontend backend
