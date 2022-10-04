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
first_name = browser.find_element_by_id("first_name")
first_name.send_keys(info['first_name'])

# Last Name
last_name = browser.find_element_by_id("last_name")
last_name.send_keys(info['last_name'])

# Email
email = browser.find_element_by_id("email")
email.send_keys(info['email'])

# Phone
phone = browser.find_element_by_id("phone")
if phone:
    phone.send_keys(info['phone'])

# City
city = browser.find_element_by_id("auto_complete_input")
if city:
    city.send_keys(info['city'])

# School
# school1 = browser.find_element_by_id('s2id_autogen1_search')
# if school1:
#     school1.send_keys(info['school1'])

# Degree 
# degree1 = browser.find_element_by_id('s2id_autogen2')
# degree1.send_keys(info['degree1'])
# degree1.click()

# Discipline
# discipline1 = browser.find_element_by_id('s2id_autogen3')
# discipline1.send_keys(info['discipline1'])
# discipline1.click()

# Start Date 1
start_month1 = browser.find_element_by_xpath('//*[@id="education_section"]/div[1]/fieldset/div[4]/fieldset/input[1]')
if start_month1:
    start_month1.send_keys(info['start_month'])
start_year1 = browser.find_element_by_xpath('//*[@id="education_section"]/div[1]/fieldset/div[4]/fieldset/input[2]')
if start_year1:
    start_year1.send_keys(info['start_year1'])

# End Date 1
end_month1 = browser.find_element_by_xpath('//*[@id="education_section"]/div[1]/fieldset/div[5]/fieldset/input[1]')
if end_month1:
    end_month1.send_keys(info['end_month'])
end_year1 = browser.find_element_by_xpath('//*[@id="education_section"]/div[1]/fieldset/div[5]/fieldset/input[2]')
if end_year1:
    end_year1.send_keys(info['end_year1'])

# Add another education
another_ed = browser.find_element_by_id('add_education')
another_ed.click()

# Start Date 2
start_month2 = browser.find_element_by_xpath('//*[@id="education_section"]/div[2]/fieldset/div[4]/fieldset/input[1]')
if start_month2:
    start_month2.send_keys(info['start_month'])
start_year2 = browser.find_element_by_xpath('//*[@id="education_section"]/div[2]/fieldset/div[4]/fieldset/input[2]')
if start_year2:
    start_year2.send_keys(info['start_year2'])

# End Date 2
end_month2 = browser.find_element_by_xpath('//*[@id="education_section"]/div[2]/fieldset/div[5]/fieldset/input[1]')
if end_month2:
    end_month2.send_keys(info['end_month'])
end_year2 = browser.find_element_by_xpath('//*[@id="education_section"]/div[2]/fieldset/div[5]/fieldset/input[2]')
if end_year2:
    end_year2.send_keys(info['end_year2'])



# Confirm all information is true by clicking checkbox
browser.find_element_by_xpath('//*[@id="job_application_answers_attributes_0_answer_selected_options_attributes_0_question_option_id"]').click()

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

# Are you within commutable distance or willing to relocate?
commutable_relocate = Select(browser.find_element_by_id('job_application_answers_attributes_12_boolean_value'))
commutable_relocate.select_by_visible_text(info['commutable_relocate'])

# Active security clearances
security_clearance = browser.find_element_by_id("s2id_autogen4")
security_clearance.send_keys(info['security_clearance'])

# LinkedIn
linkedin = browser.find_element_by_id("job_application_answers_attributes_15_text_value")
if linkedin:
    linkedin.send_keys(info['linkedin'])

# Additional link
additional_link = browser.find_element_by_id("job_application_answers_attributes_16_text_value")
additional_link.send_keys(info['additional_link'])

# How did you hear about this job?
hear_job = Select(browser.find_element_by_id('job_application_answers_attributes_17_answer_selected_options_attributes_17_question_option_id'))
hear_job.select_by_visible_text(info['hear_job'])

# Please specify name for referral
referral_name = browser.find_element_by_id("job_application_answers_attributes_18_text_value")
referral_name.send_keys(info['referral_name'])

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
