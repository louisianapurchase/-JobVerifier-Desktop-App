from ui import JobVerifierUI  # Import the JobVerifierUI class from your UI file
import sys
from PyQt5.QtWidgets import QApplication
import os
os.environ['QT_QPA_PLATFORM'] = 'offscreen'
if __name__ == "__main__":
    app = QApplication(sys.argv)  # Create an instance of QApplication
    window = JobVerifierUI()  # Create an instance of JobVerifierUI (not QApplication)
    window.show()  # Show the main window
    sys.exit(app.exec_())  # Start the Qt event loop
