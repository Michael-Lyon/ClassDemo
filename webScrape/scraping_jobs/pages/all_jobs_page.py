from webScrape.scraping_jobs.parsers.job_parser import JobParser
from bs4 import BeautifulSoup 
from webScrape.scraping_jobs.locators.all_jobs_locator import ALLJobLocators

class AllJobsPage:
    
    def __init__(self, page_content):
        self.soup = BeautifulSoup(page_content, 'html.parser')

    @property
    def jobs(self):
        """returns all the jobs in a page"""
        return [JobParser(e) for e in self.soup.select(ALLJobLocators.JOBS)]
