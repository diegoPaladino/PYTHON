# DataScientistRemoteJobFinder

## Introduction
DataScientistRemoteJobFinder is a Python-based web scraping tool designed to search for remote Data Scientist job listings. The tool fetches job postings from a specified website, filters for remote positions, and saves the results in a CSV file.

## List of Required Materials
- Python 3.x
- `requests` library
- `beautifulsoup4` library
- `csv` module

## Purpose of the Project
The project aims to simplify the job search process for Data Scientists looking for remote opportunities. By automating the scraping and filtering of job listings, users can efficiently find relevant job postings without manually browsing through multiple websites.

## Pros and Cons
### Pros
- Automates the job search process
- Saves time by filtering for remote positions
- Exports job listings to a CSV file for easy access and organization

### Cons
- Limited to the specified website for job listings
- Requires internet connection to fetch job postings
- Website structure changes may break the scraper

## General Instructions
### Installation
1. Clone the repository:
    ```sh
    git clone https://github.com/username/DataScientistRemoteJobFinder.git
    cd DataScientistRemoteJobFinder
    ```
2. Install the required libraries:
    ```sh
    pip install requests beautifulsoup4
    ```

### Usage
1. Open `DataScientistRemoteJobFinder.py` and update the URL to the target job listing website.
2. Run the script:
    ```sh
    python DataScientistRemoteJobFinder.py
    ```
3. The remote job listings will be saved to `remote_data_scientist_jobs.csv`.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
