import selenium
## from bs4 import BeautifulSoup
from selenium import webdriver
## url = 'https://www.regulations.gov/search/comment?filter=renewable%20fuel%20standard'
url2 = 'https://www.regulations.gov/docket/EPA-HQ-OAR-2014-0537/comments'

PATH = '/usr/local/bin/chromedriver'
driver = webdriver.Chrome(PATH)

driver.get(url2)


