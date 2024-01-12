from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Function that initialize the driver
def initialize_driver():
    service = Service(executable_path="chromedriver.exe")
    return webdriver.Chrome(service=service)

# Function that take in user input and search for the product
def search_product(driver, user_input):
    driver.get("https://www.automationexercise.com/products")
    
    # Target the search box by id
    search_input = driver.find_element(By.ID, "search_product")
    # Take in user input and append it on the search bar
    search_input.send_keys(user_input)
    
    # Target the search button by id
    submit_input = driver.find_element(By.ID, "submit_search")
    # Click on the search button
    submit_input.click()

    # Wait for the result to load
    wait_res = WebDriverWait(driver, 10)
    wait_res.until(EC.presence_of_element_located((By.ID, "search_product")))
    time.sleep(5)

def main():
    # Request input from user
    user_input = input("Enter a search term: ")

    try:
        driver = initialize_driver()
        # Execute the code through the search_product function
        search_product(driver, user_input)
    finally:
        driver.quit()

if __name__ == "__main__":
    main()
