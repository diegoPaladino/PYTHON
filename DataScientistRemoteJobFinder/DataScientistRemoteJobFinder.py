import requests
from bs4 import BeautifulSoup
import csv

class DataScientistRemoteJobFinder:
    def __init__(self, url):
        self.url = url

    def fetch_jobs(self):
        response = requests.get(self.url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            return self.parse_jobs(soup)
        else:
            return []

    def parse_jobs(self, soup):
        job_listings = []
        jobs = soup.find_all('div', class_='job-listing')
        for job in jobs:
            title = job.find('h2', class_='title').text.strip()
            company = job.find('div', class_='company').text.strip()
            location = job.find('div', class_='location').text.strip()
            description = job.find('div', class_='description').text.strip()
            if 'remote' in location.lower():
                job_listings.append({
                    'title': title,
                    'company': company,
                    'location': location,
                    'description': description
                })
        return job_listings

    def save_to_csv(self, jobs, filename):
        keys = jobs[0].keys()
        with open(filename, 'w', newline='', encoding='utf-8') as output_file:
            dict_writer = csv.DictWriter(output_file, fieldnames=keys)
            dict_writer.writeheader()
            dict_writer.writerows(jobs)

    def run(self):
        jobs = self.fetch_jobs()
        if jobs:
            self.save_to_csv(jobs, 'remote_data_scientist_jobs.csv')
        else:
            print("No remote data scientist jobs found.")

if __name__ == "__main__":
    job_finder = DataScientistRemoteJobFinder('https://example.com/jobs')
    job_finder.run()
