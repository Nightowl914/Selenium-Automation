from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

# Function that navigate to desired url
def navigate_to_url(driver, url):
    driver.get(url)

# Function that autofill login and card billing details 
def autofill_form(driver, submit_button=None, *fields):
    # Use for loop to loop through each tuple and append relevant data to the corresponding fields
    for field in fields:
        field_name, field_value = field[0], field[1]
        field_name.send_keys(field_value)

    # Click on the submit button if provided
    if submit_button:
        submit_button.click()

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
def search_product(driver, search_input, user_input, submit_input):
    # Take in user input and append it on the search bar
    search_input.send_keys(user_input)
    
    # Click on the search button
    submit_input.click()

def view_product(driver, product_link):
    # Click to view product
    product_link.click()

def add_to_cart(driver, qty_field, quantity, add_btn):
    # Clear the quantity field before appending user input
    qty_field.clear()
    
    # Take in user input and append it on the quantity field
    qty_field.send_keys(quantity)

    # Click on the button
    add_btn.click()

def view_cart(driver, view_cart_link):
    # Click on the link
    view_cart_link.click()

def checkout(driver, checkout_btn):
    # Click on the checkout button
    checkout_btn.click()

def place_order(driver, placeOrder_btn):
    # Click on the place order button
    placeOrder_btn.click()



