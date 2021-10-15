# Web form automation
from selenium import webdriver 
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.support.ui import Select
# Accessing environment variables
import os
import yaml


# Chromedriver
chromedriver_location = f"/Users/{os.environ['USER']}/Downloads/chromedriver"

# browser = webdriver.Safari()
browser = webdriver.Chrome(chromedriver_location)
# binary = FirefoxBinary('path/to/installed firefox binary')
# browser = webdriver.Firefox(firefox_binary=binary)


# Retrieve info from YAML file
with open('config.yml', 'r') as file:
    info = yaml.safe_load(file)

# Job Application URL
browser.get(info['url'])

# First Name
first_name = browser.find_element_by_xpath('//*[@id="first_name"]')
first_name.send_keys(info['first_name'])

# Last Name
last_name = browser.find_element_by_xpath('//*[@id="last_name"]')
last_name.send_keys(info['last_name'])

# Email
email = browser.find_element_by_xpath('//*[@id="email"]')
email.send_keys(info['email'])

# Phone
phone = browser.find_element_by_xpath('//*[@id="phone"]')
if phone:
    phone.send_keys(info['phone'])

# City
city = browser.find_element_by_xpath('//*[@id="job_application_location"]')
if city:
    city.send_keys(info['city'])

# LinkedIn
linkedin = browser.find_element_by_xpath('//*[@id="job_application_answers_attributes_15_text_value"]')
if linkedin:
    linkedin.send_keys(info['linkedin'])

# School
school = browser.find_element_by_xpath('//*[@id="s2id_autogen1"]')
if school:
    school.send_keys(info['school'])

# Degree 
degree = Select(browser.find_element_by_id('education_degree_0'))
degree.select_by_visible_text(info['degree'])

# Discipline
discipline = Select(browser.find_element_by_id('education_discipline_0'))
discipline.select_by_visible_text(info['discipline'])

# Start Date
start_month = browser.find_element_by_xpath('//*[@id="education_section"]/div[1]/fieldset/div[4]/fieldset/input[1]')
if start_month:
    start_month.send_keys(info['start_month'])
start_year = browser.find_element_by_xpath('//*[@id="education_section"]/div[1]/fieldset/div[4]/fieldset/input[2]')
if start_year:
    start_year.send_keys(info['start_year'])

# End Date
end_month = browser.find_element_by_xpath('//*[@id="education_section"]/div[1]/fieldset/div[5]/fieldset/input[1]')
if end_month:
    end_month.send_keys(info['end_month'])
end_year = browser.find_element_by_xpath('//*[@id="education_section"]/div[1]/fieldset/div[5]/fieldset/input[2]')
if end_year:
    end_year.send_keys(info['end_year'])

