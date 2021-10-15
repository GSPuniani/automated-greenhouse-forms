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

# Undergraduate GPA
gpa_undergrad = Select(browser.find_element_by_id('job_application_answers_attributes_1_answer_selected_options_attributes_1_question_option_id'))
gpa_undergrad.select_by_visible_text(info['gpa_undergrad'])

# Graduate GPA
gpa_grad = Select(browser.find_element_by_id('job_application_answers_attributes_2_answer_selected_options_attributes_2_question_option_id'))
gpa_grad.select_by_visible_text(info['gpa_grad'])

# Doctorate GPA
gpa_doctorate = Select(browser.find_element_by_id('job_application_answers_attributes_3_answer_selected_options_attributes_3_question_option_id'))
gpa_doctorate.select_by_visible_text(info['gpa_doctorate'])

# SAT Score
sat_score = Select(browser.find_element_by_id('job_application_answers_attributes_4_answer_selected_options_attributes_4_question_option_id'))
sat_score.select_by_visible_text(info['sat_score'])

# ACT Score
act_score = Select(browser.find_element_by_id('job_application_answers_attributes_5_answer_selected_options_attributes_5_question_option_id'))
act_score.select_by_visible_text(info['act_score'])

# GRE Score
gre_score = Select(browser.find_element_by_id('job_application_answers_attributes_6_answer_selected_options_attributes_6_question_option_id'))
gre_score.select_by_visible_text(info['gre_score'])

# GMAT Score
gmat_score = Select(browser.find_element_by_id('job_application_answers_attributes_7_answer_selected_options_attributes_7_question_option_id'))
gmat_score.select_by_visible_text(info['gmat_score'])

# SpaceX Employment History
spacex_history = Select(browser.find_element_by_id('job_application_answers_attributes_8_answer_selected_options_attributes_8_question_option_id'))
spacex_history.select_by_visible_text(info['spacex_history'])

# Years of Professional Work Experience
work_exp = Select(browser.find_element_by_id('job_application_answers_attributes_10_answer_selected_options_attributes_10_question_option_id'))
work_exp.select_by_visible_text(info['work_exp'])

# Basic Qualifications Satisfied
basic_qualifications = Select(browser.find_element_by_id('job_application_answers_attributes_11_boolean_value'))
basic_qualifications.select_by_visible_text(info['basic_qualifications'])

# How did you hear about this job?
hear_job = Select(browser.find_element_by_id('job_application_answers_attributes_17_answer_selected_options_attributes_17_question_option_id'))
hear_job.select_by_visible_text(info['hear_job'])

# Legal authorization
legal_auth = Select(browser.find_element_by_id('job_application_answers_attributes_19_answer_selected_options_attributes_19_question_option_id'))
legal_auth.select_by_visible_text(info['legal_auth'])

# Citizenship Status
citizen_status = Select(browser.find_element_by_id('job_application_answers_attributes_20_answer_selected_options_attributes_20_question_option_id'))
citizen_status.select_by_visible_text(info['citizen_status'])

# Gender
gender = Select(browser.find_element_by_id('job_application_gender'))
gender.select_by_visible_text(info['gender'])


# Hispanic/Latino
hispanic_lat = Select(browser.find_element_by_id('job_application_hispanic_ethnicity'))
hispanic_lat.select_by_visible_text(info['hispanic_lat'])


# Veteran Status
veteran = Select(browser.find_element_by_id('job_application_veteran_status'))
veteran.select_by_visible_text(info['veteran'])


# Disability Status
disability = Select(browser.find_element_by_id('job_application_disability_status'))
disability.select_by_visible_text(info['disability'])
