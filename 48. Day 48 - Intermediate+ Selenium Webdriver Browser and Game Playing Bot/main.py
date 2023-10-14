from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()

driver.get("https://www.python.org/")
# search_bar = driver.find_element(By.NAME, value="q")
# search_bar.get_attribute("class"))

# documentation_link = driver.find_element(By.CSS_SELECTOR, ".documentation-widget a")
# print(documentation_link.text)
# print(documentation_link.get_attribute("href"))

# xpath = "/html/body/div/footer/div[2]/div/ul/li[3]/a"
# bug_link = driver.find_element(By.XPATH, xpath)
# print(bug_link.get_attribute("href"))

# events_block = driver.find_element(By.CLASS_NAME, "event-widget")

event_times = driver.find_elements(By.CSS_SELECTOR, ".event-widget time")

event_names = driver.find_elements(By.CSS_SELECTOR, ".event-widget ul li a")

event_dict={}
for i in range(len(event_times)):
    event_dict[i] = {
            "time":event_times[i].text,
            "name":event_names[i].text
        }
print(event_dict)

