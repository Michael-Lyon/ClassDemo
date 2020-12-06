# from webScrape.scraping_jobs.locators.job_locators import JobLocator



from webScrape.scraping_jobs.locators.job_locators import JobLocator


class JobParser:
    """
    A class to take an HTML page and findjobs on a page(s) on Jobberman website.
    """

    def __init__(self, parent):
        self.parent = (parent)

    def __repr__(self):
        return f"<JOB {self.find_job_name}, {self.employer}, {self.job_function}, {self.job_type}, {self.salary}, {self.find_job_link}, {self.salary}>"

    @property       
    def find_job_name(self):
        locator = JobLocator.JOB_NAME
        job_link = self.parent.select_one(locator)
        job_name = job_link.attrs['title']
        return(job_name)

    @property
    def find_job_link(self):
        locator = JobLocator.JOB_LINK
        job_link = self.parent.select_one(locator).attrs['href']
        return(job_link)

    @property
    def employer(self): 
        """reaturns a tuple (employer name and employer link) """
        #  aLSO RETURNS LINK TO THE EMPLOYERS SITE
        locator = JobLocator.EMPLOYER
        emp_link = self.parent.select_one(locator).attrs['href']
        emp_name = self.parent.select_one(locator).string.strip()
        # return(emp_name)
        return(emp_name, emp_link)
        

    @property
    def location(self):
        locator = JobLocator.LOCATION
        location = self.parent.select_one(locator).string.strip()
        return(location)

    @property
    def job_type(self):
        locator = JobLocator.JOB_TYPE
        type = self.parent.select_one(locator).string.strip()
        return(type)

    @property
    def salary(self):
        locator = JobLocator.SALARY
        salary = self.parent.select_one(locator).text.strip().split()
        salary = ' '.join(map(str, salary))
        return(salary)

    @property
    def job_function(self): 
        """returns a tuple (job function and time stamp ) """
         # ALSO RETURNS THE TIME STAMP
        locator = JobLocator.JOB_FUNCTION
        locator2 = JobLocator.TIME_STAMP
        function = self.parent.select_one(locator).string.strip()
        time_stamp = self.parent.select_one(locator2).text.strip()
        return(function, time_stamp)

    @property
    def summary(self):
        locator = JobLocator.SUMMARY
        summ = self.parent.select_one(locator).string.strip()
        return(summ)
