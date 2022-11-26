from linkedin_scraper import Company, actions
from selenium import webdriver
import csv
driver = webdriver.Chrome()
try:
    f = open("credentials.txt", "r")
    contents = f.read()
    email = contents.replace("=", ",").split(",")[1]
    password = contents.replace("=", ",").split(",")[3]
except:
    f = open("credentials.txt", "w+")
    email = input('Enter your linkedin username: ')
    password = input('Enter your linkedin password: ')
    f.write("username={}, password={}".format(username, password))
    f.close()
actions.login(driver, email, password) # if email and password isnt given, it'll prompt in terminal
company = Company(linkedin_url= 'https://www.linkedin.com/company/google', driver=driver, get_employees=True, close_on_complete=False)
print (company)

with open("data.csv",'r') as f:
    people = f.read()

with open("person.csv",'w') as f:
    for p in people:
        company = Company(linkedin_url= p, driver=driver, get_employees=True, close_on_complete=False)