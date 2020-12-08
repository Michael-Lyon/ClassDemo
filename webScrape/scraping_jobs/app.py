import requests
from bs4 import BeautifulSoup
from webScrape.scraping_jobs.pages.all_jobs_page import AllJobsPage

#PAGE 1
page_content = requests.get('https://www.jobberman.com/jobs').content
# print(page_content)

page = AllJobsPage(page_content) #CREATING AN OBJECT OF THE ALLJOBSPAGE CLASS
jobs = page.jobs # Getting just one page



#getting multiple pages.
for page_num in range(1, page.page_count):
    url = f'https://www.jobberman.com/jobs?page={page_num+1}'
    page_content = requests.get(url).content
    page = AllJobsPage(page_content)
    jobs.extend(page.jobs)

print(jobs)

