# Web form automation
from selenium import webdriver 
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
# Accessing environment variables
# from dotenv import load_dotenv
# load_dotenv()
# from decouple import config
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

# First Name
first_name = browser.find_element_by_xpath('//*[@id="first_name"]')
# first_name.send_keys(os.environ.get('FIRST_NAME'))
# first_name.send_keys(config('FIRST_NAME'))
first_name.send_keys('Gobind')

# Last Name
last_name = browser.find_element_by_xpath('//*[@id="last_name"]')
last_name.send_keys('Puniani')

# Email
email = browser.find_element_by_xpath('//*[@id="email"]')
email.send_keys('gobindpuniani@gmail.com')

# Phone
phone = browser.find_element_by_xpath('//*[@id="phone"]')
phone.send_keys('(559) 392-2944')

# City
city = browser.find_element_by_xpath('//*[@id="job_application_location"]')
city.send_keys('Clovis')

# LinkedIn
linkedin = browser.find_element_by_xpath('//*[@id="job_application_answers_attributes_15_text_value"]')
linkedin.send_keys('https://www.linkedin.com/in/gobind-puniani/')