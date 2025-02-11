FROM python:3.9

# Set working directory
WORKDIR /app
ENV QT_QPA_PLATFORM=offscreen
ENV XDG_RUNTIME_DIR=/tmp/runtime-root

# Copy only requirements first to leverage Docker caching
COPY requirements.txt .

# Install system dependencies required for PyQt5
RUN apt-get update && apt-get install -y \
    libxcb-xinerama0 \
    libegl1-mesa \
    libxkbcommon-x11-0 \
    libglib2.0-0 \
    libx11-xcb1 \
    libgl1-mesa-glx \
    libxrender1 \
    libfontconfig1 \
    libxkbcommon0 \
    libsm6 \
    libxext6 \
    && rm -rf /var/lib/apt/lists/*



# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt
RUN pip freeze | grep PyQt5

# Copy the rest of the application files
COPY . .

# Build the PyQt5 application using PyInstaller with hidden imports for PyQt5
RUN pyinstaller --onefile --windowed --hidden-import=PyQt5.QtWidgets --hidden-import=PyQt5.sip --hidden-import=PyQt5.QtGui --hidden-import=PyQt5.QtCore main.py


# Set executable permissions for the generated binary
RUN chmod +x /app/dist/main

# Run the application
CMD ["python", "main.py"]
