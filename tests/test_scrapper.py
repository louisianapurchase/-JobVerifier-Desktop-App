import unittest
from backend.scraper import extract_job_data

class TestScraper(unittest.TestCase):
    def test_extract_job_data(self):
        data = extract_job_data("https://fakejobsite.com/sample-job")
        self.assertIn("title", data)
        self.assertIn("company", data)

if __name__ == "__main__":
    unittest.main()
