# Web form automation
from selenium import webdriver 
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
# Accessing environment variables
import os


# Chromedriver
chromedriver_location = f"/Users/{os.environ['USER']}/Downloads/chromedriver"

# browser = webdriver.Safari()
browser = webdriver.Chrome(chromedriver_location)
# binary = FirefoxBinary('path/to/installed firefox binary')
# browser = webdriver.Firefox(firefox_binary=binary)

# print(str(os.getenv('URL')))
# browser.get(str(os.getenv('URL')))
browser.get("https://boards.greenhouse.io/spacex/jobs/5479547002?gh_jid=5479547002&gh_src=e7cc0b212us#app")

first_name = browser.find_element_by_xpath('//*[@id="first_name"]')
first_name.send_keys(os.getenv('FIRST_NAME'))