from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

# Enter a search term
user_input = input("Enter a search term: ")

# Open the webpage 
driver.get("https://www.automationexercise.com/products")

# Target the search box by id
search_input = driver.find_element(By.ID, "search_product")
# Submit the search term by clicking enter
search_input.send_keys(user_input)
submit_input = driver.find_element(By.ID, "submit_search")
submit_input.click()



# Wait for search results to load
wait_res = WebDriverWait(driver, 10)
wait_res.until(EC.presence_of_element_located((By.ID, "search_product")))

time.sleep(5)

driver.quit()




