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

# gpa_undergrad
gpa_undergrad = Select(browser.find_element_by_id('job_application_answers_attributes_1_answer_selected_options_attributes_1_question_option_id'))
gpa_undergrad.select_by_visible_text(info['gpa_undergrad'])

# gpa_grad
gpa_grad = Select(browser.find_element_by_id('job_application_answers_attributes_2_answer_selected_options_attributes_2_question_option_id'))
gpa_grad.select_by_visible_text(info['gpa_grad'])

# gpa_doctorate
gpa_doctorate = Select(browser.find_element_by_id('job_application_answers_attributes_3_answer_selected_options_attributes_3_question_option_id'))
gpa_doctorate.select_by_visible_text(info['gpa_doctorate'])

# sat_score
sat_score = Select(browser.find_element_by_id('job_application_answers_attributes_4_answer_selected_options_attributes_4_question_option_id'))
sat_score.select_by_visible_text(info['sat_score'])

# act_score
act_score = Select(browser.find_element_by_id('job_application_answers_attributes_5_answer_selected_options_attributes_5_question_option_id'))
act_score.select_by_visible_text(info['act_score'])

# gre_score
gre_score = Select(browser.find_element_by_id('job_application_answers_attributes_6_answer_selected_options_attributes_6_question_option_id'))
gre_score.select_by_visible_text(info['gre_score'])

# gmat_score
gmat_score = Select(browser.find_element_by_id('job_application_answers_attributes_7_answer_selected_options_attributes_7_question_option_id'))
gmat_score.select_by_visible_text(info['gmat_score'])

# spacex_history
spacex_history = Select(browser.find_element_by_id('job_application_answers_attributes_8_answer_selected_options_attributes_8_question_option_id'))
spacex_history.select_by_visible_text(info['spacex_history'])