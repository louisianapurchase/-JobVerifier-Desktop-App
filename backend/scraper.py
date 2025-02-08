import requests
from bs4 import BeautifulSoup

def extract_job_data(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    
    job_title = soup.find("h1").text if soup.find("h1") else "Unknown"
    company = soup.find("div", class_="company-name").text if soup.find("div", class_="company-name") else "Unknown"

    return {"title": job_title, "company": company, "url": url}
