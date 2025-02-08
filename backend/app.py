from flask import Flask, request, jsonify
from scraper import extract_job_data
from classifier import classify_job

app = Flask(__name__)

@app.route("/verify", methods=["POST"])
def verify():
    url = request.json.get("url")
    job_data = extract_job_data(url)
    classification = classify_job(job_data)
    return jsonify({"status": classification, "details": job_data})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
