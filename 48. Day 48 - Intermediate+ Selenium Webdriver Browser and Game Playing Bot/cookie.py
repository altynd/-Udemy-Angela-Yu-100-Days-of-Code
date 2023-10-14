from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
import time

website = "https://orteil.dashnet.org/cookieclicker/"
driver = webdriver.Chrome()
driver.get(website)
driver.implicitly_wait(0.5)
time.sleep(2)

lang = driver.find_element(By.CSS_SELECTOR,"div .langSelectButton")
lang.click()

time.sleep(2)
button = driver.find_element(By.ID, "bigCookie")
n=0
while n<10000:
    button.click()
    # time.sleep(0.001)
    n+=1

input()