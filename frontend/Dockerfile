FROM python:3.9

# Set working directory
WORKDIR /app

# Copy only requirements first to leverage Docker caching
COPY requirements.txt .

# Install system dependencies required for PyQt5
RUN apt-get update && apt-get install -y \
    libxcb-xinerama0 \
    libegl1-mesa \
    libxkbcommon-x11-0 \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application files
COPY . .

# Build the PyQt5 application using PyInstaller with hidden imports for PyQt5
RUN pyinstaller --onefile --windowed --hidden-import=PyQt5.QtWidgets --hidden-import=PyQt5.sip main.py

# Set executable permissions for the generated binary
RUN chmod +x /app/dist/main

# Run the application
CMD ["/app/dist/main"]
