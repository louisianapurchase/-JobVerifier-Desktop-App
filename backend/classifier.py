import random

def classify_job(job_data):
    risk_score = random.randint(0, 100)  # Placeholder for actual ML model
    
    if risk_score > 70:
        return "Fake or Untrustworthy"
    elif risk_score > 40:
        return "Potentially Risky"
    else:
        return "Legitimate"
