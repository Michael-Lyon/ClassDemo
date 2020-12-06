from bs4 import BeautifulSoup
from soupsieve.css_parser import PAT_AT_RULE
ITEM_HTML = '''<article class="search-result ">
    <header class="search-result__header">
        <div class="customer-card--column">
            <div class="wrapper--inline-flex justify--space-between padding-lr-20">
                <div class="flex--3 wrapper--inline-flex align--center direction--row"><a
                        href="https://www.jobberman.com/listings/architect-p62jgj"
                        class="search-result__job-title metrics-apply-now "
                        onclick="window.dataLayer &amp;&amp; window.dataLayer.push({'listing_type': 'Normal'});"
                        title="Architect">
                        <h3>Architect</h3>
                    </a></div>
                <div
                    class="flex--2 wrapper--inline-flex justify--flex-end align--center direction--row width--120 max-width--260">
                    <div class="label--new margin-left--10" title="Added 20 hours ago">
                        New
                    </div>
                </div>
            </div>
            <div
                class="if-content-panel padding-lr-20 flex-direction-top-to-bottom--under-lg align--start--under-lg search-result__job-meta">
                <a href="/company/studenthubng_15f2d3bff23b39">
                    Studenthubng
                </a></div>
            <div
                class="if-content-panel align--center padding-lr-10 flex-direction-top-to-bottom--under-lg align--start--under-lg">
                <div class="search-result__location">
                    Lagos
                </div><span class="job-header__divider">|</span><span class="search-result__job-type">
                    Full Time
                </span><span class="job-header__divider">|</span>
                <div class="search-result__job-salary"><span class="text--bold">
                        NGN
                    </span>
                    75,000 - 150,000
                </div>
            </div>
            <div class="wrapper--inline-flex justify--flex-start direction--column padding-lr-20">
                <div class="customer-card--column">
                    <div class="search-result__job-function">
                        <div class="wrapper--inline-flex">
                            <div class="if-wrapper-row ellipses">
                                Job Function:
                                <span class="padding-lr-10 gutter-flush-under-lg">
                                    Creative &amp; Design
                                </span></div>
                            <div class="if-wrapper-column align-self--end text--right">
                                20h
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </header>
    <div class="search-result__body">
        <div class="search-result__image-container">
            <div class="search-result__card-icon  basic-icon "><a href="/company/studenthubng_15f2d3bff23b39"><img
                        class="basic-icon-logo ls-is-cached lazyloaded"
                        data-src="/build/static-assets/img/dashboard-default-6fec87a49a.svg" alt="Studenthubng"
                        width="60" height="60" src="/build/static-assets/img/dashboard-default-6fec87a49a.svg"></a>
            </div>
        </div><a href="https://www.jobberman.com/listings/architect-p62jgj" class="metrics-apply-now "
            onclick="window.dataLayer &amp;&amp; window.dataLayer.push({'listing_type': 'Normal'});" title="Architect">
            <div class="search-result__content transform-y-center content-hide--under-md">
                <p>
                    We are looking for a creative and inspired Architect to handle projects for our client briefing
                    through to the final stages of construction. The Architect's responsibilities include managing
                    relationships, developing and presenting design proposals, preparing drawings, specifications,
                    budgets, construction documents and managing project. You sh ...
                </p>
            </div>
            <div class="search-result__content transform-y-center content-show--under-md">
                <p>
                    We are looking for a creative and inspired Architect to handle projects for our client briefing ...
                </p>
            </div>
        </a>
    </div>
</article>

'''

class ParsedItemLocator:
    """
    This allows us to easily change/enhance our page/parser locators
    """
    JOB_NAME = 'article.search-result header.search-result__header div div div a'
    JOB_LINK = 'article.search-result header.search-result__header div div div a'
    EMPLOYER = 'article.search-result header.search-result__header div.search-result__job-meta a'
    LOCATION = 'article.search-result header.search-result__header div.search-result__location'
    JOB_TYPE = 'article.search-result header.search-result__header span.search-result__job-type'
    SALARY = 'article.search-result header.search-result__header div.search-result__job-salary'
    JOB_FUNCTION = 'article.search-result header.search-result__header div.search-result__job-function span'
    TIME_STAMP = 'article.search-result header.search-result__header div.search-result__job-function div.text--right'
    SUMMARY = 'article.search-result div.search-result__body div.search-result__content p'

class ParsedItem:
    """
    A class to take an HTML page and findjobs on a page(s) on Jobberman website.
    """

    def __init__(self, page):
        self.soup = BeautifulSoup(page, 'html.parser')

    @property
    def find_job_name(self):
        locator = ParsedItemLocator.JOB_NAME
        job_link = self.soup.select_one(locator)
        job_name = job_link.attrs['title']
        return(job_name)
    
    @property
    def find_job_link(self):
        locator = ParsedItemLocator.JOB_LINK
        job_link = self.soup.select_one(locator).attrs['href']
        return(job_link)

    @property
    def employer(self): # aLSO RETURNS LINK TO THE EMPLOYERS SITE
        locator = ParsedItemLocator.EMPLOYER
        emp_link = self.soup.select_one(locator).attrs['href']
        emp_name = self.soup.select_one(locator).string.strip()
        return(emp_name, emp_link)

    @property
    def location(self):
        locator = ParsedItemLocator.LOCATION
        location = self.soup.select_one(locator).string.strip()
        return(location)

    @property
    def job_type(self):
        locator = ParsedItemLocator.JOB_TYPE
        type = self.soup.select_one(locator).string.strip()
        return(type)

    @property
    def salary(self):
        locator = ParsedItemLocator.SALARY
        salary = self.soup.select_one(locator).text.strip().split()
        salary = ' '.join(map(str, salary))
        return(salary)

    @property
    def job_function(self): #ALSO RETURNS THE TIME STAMP
        locator = ParsedItemLocator.JOB_FUNCTION
        locator2 = ParsedItemLocator.TIME_STAMP
        function = self.soup.select_one(locator).string.strip()
        time_stamp = self.soup.select_one(locator2).text.strip()
        return(function, time_stamp)

    @property
    def summary(self):
        locator = ParsedItemLocator.SUMMARY
        summ = self.soup.select_one(locator).string.strip()
        return(summ)


# find_job_name()
# find_job_link()
# employer()
# location()
# job_type()
# salary()
# job_function()
# summary()

page = ParsedItem(ITEM_HTML)
print(page.find_job_link)
