import requests
from bs4 import BeautifulSoup
from webScrape.scraping_jobs.pages.all_jobs_page import AllJobsPage

page_content = requests.get('https://www.jobberman.com/jobs').content
# print(page_content)

page = AllJobsPage(page_content)


jobs = page.jobs
for job in jobs:
    print(job)

