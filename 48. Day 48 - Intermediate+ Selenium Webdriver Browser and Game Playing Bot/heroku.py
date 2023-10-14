from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys

website = "https://secure-retreat-92358.herokuapp.com/"
driver = webdriver.Chrome()
driver.get(website)

name = driver.find_element(By.NAME, "fName")
name.send_keys("Dmitriy")

lname = driver.find_element(By.NAME, "lName")
lname.send_keys("Altyn")

email = driver.find_element(By.NAME, "email")
email.send_keys("altynd@mail.ru")

# submit = driver.find_element(By.XPATH, "/html/body/form/button")
submit = driver.find_element(By.CSS_SELECTOR, "form button")
submit.click()

input()
