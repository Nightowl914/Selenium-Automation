from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time

# Function that initialize the driver
def initialize_driver():
    service = Service(executable_path="chromedriver.exe")

    # add in extension path for adblock
    extension_path = './extensions/uBlockOrigin.crx'

    # Create Chrome options
    chrome_options = Options()
    
    # Add the extension to Chrome options
    chrome_options.add_extension(extension_path)

    return webdriver.Chrome(service=service, options=chrome_options)

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
    wait_res.until(EC.presence_of_element_located((By.XPATH, "//a[contains(@href, '/product_details/') and contains(text(), 'View Product')]")))


def view_product(driver):
    # target product link 
    product_link = driver.find_element(By.XPATH, "//a[contains(@href, '/product_details/') and contains(text(), 'View Product')]")
    # Click to view product
    product_link.click()

def add_to_cart(driver, quantity):
    # Target quantity field
    qty_field = driver.find_element(By.ID, "quantity")
    # Clear the quantity field before appending user input
    qty_field.clear()
    # Take in user input and append it on the quantity field
    qty_field.send_keys(quantity)
    # Target 'Add to cart' button
    add_btn = driver.find_element(By.CSS_SELECTOR, ".btn.btn-default.cart")
    time.sleep(2)
    # Click on the button
    add_btn.click()

def view_cart(driver):
    # Target view cart link and wait for the 'View Cart' link to be clickable
    view_cart_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="cartModal"]/div/div/div[2]/p[2]/a'))
    )
    time.sleep(2)
    # Click on the link
    view_cart_link.click()

def main():
    # Request input from user
    user_input = input("Enter a search term: ")

    try:
        driver = initialize_driver()
        # Execute the code through the search_product function
        search_product(driver, user_input)
        # Execute the code through the view_product function
        view_product(driver)
        # Ask user for quantity input
        quantity = input("Enter quantity: ")
        # Execute the code through the add_to_cart function
        add_to_cart(driver, quantity)
        # Execute the code through the view_cart function
        view_cart(driver)
    finally:
        time.sleep(5)
        driver.quit()

if __name__ == "__main__":
    main()

