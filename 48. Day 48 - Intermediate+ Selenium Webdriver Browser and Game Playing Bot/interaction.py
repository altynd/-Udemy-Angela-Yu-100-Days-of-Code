from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys

website="https://ru.wikipedia.org/wiki/%D0%97%D0%B0%D0%B3%D0%BB%D0%B0%D0%B2%D0%BD%D0%B0%D1%8F_%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0"
driver = webdriver.Chrome()
driver.get(website)

#number of articles
number_articles = driver.find_element(By.CSS_SELECTOR,".main-top-right p b")
# number_articles.click()

all_portals = driver.find_element(By.LINK_TEXT, "Порталы")
# all_portals.click()

search = driver.find_element(By.NAME, "search")
search.send_keys("Python")
search.send_keys(Keys.ENTER)

# search_button = driver.find_element(By.ID, "searchButton")
# search_button.click()

input()
