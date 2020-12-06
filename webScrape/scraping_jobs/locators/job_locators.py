class JobLocator:
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
