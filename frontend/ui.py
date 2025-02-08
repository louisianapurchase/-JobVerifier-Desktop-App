from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLineEdit, QLabel
import sys
import requests

class JobVerifierUI(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("JobVerifier")
        self.setGeometry(100, 100, 400, 200)

        layout = QVBoxLayout()

        self.url_input = QLineEdit(self)
        self.url_input.setPlaceholderText("Enter job URL...")
        layout.addWidget(self.url_input)

        self.verify_btn = QPushButton("Verify Job", self)
        self.verify_btn.clicked.connect(self.verify_job)
        layout.addWidget(self.verify_btn)

        self.result_label = QLabel("Result will be displayed here", self)
        layout.addWidget(self.result_label)

        self.setLayout(layout)

    def verify_job(self):
        url = self.url_input.text()
        response = requests.post("http://localhost:5000/verify", json={"url": url})
        result = response.json()
        self.result_label.setText(f"Status: {result['status']}")

    def run(self):
        app = QApplication(sys.argv)
        self.show()
        sys.exit(app.exec_())
