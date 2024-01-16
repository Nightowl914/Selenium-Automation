from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from module.automation_library import navigate_to_url, initialize_driver, autofill_form, search_product, view_product, add_to_cart, view_cart, checkout, place_order 
import time

def main():
    # Navigation urls
    login_url = "https://www.automationexercise.com/login"
    product_url = "https://www.automationexercise.com/products"
    
    # User_details
    user_email = "testEmail@email.com"
    user_pwd = "test12345"
    card_name = "test"
    card_number = 1234567
    cvc_number = 123
    expiration_month = "05"
    expiration_year = 2028

    # Wait time
    wait = 10

    try:
        # Execute the code through the initialize_driver function
        driver = initialize_driver()


        # Navigate to login page
        navigate_to_url(driver, login_url)
        # Target the email field
        email_field = driver.find_element(By.NAME, "email")
        # Target the password field
        pwd_field = driver.find_element(By.NAME, "password")
        # Target the login button by class
        login_btn = driver.find_element(By.CSS_SELECTOR, "button[data-qa='login-button']")
        # Execute the code through the autofill_form function
        autofill_form(driver, login_btn, (email_field, user_email), (pwd_field, user_pwd))


        # Navigate to product page
        navigate_to_url(driver, product_url)
        # Target the search box by id
        search_input = driver.find_element(By.ID, "search_product")
        # Request search product input from user
        # user_input = input("Enter a search term: ")
        user_input = "Blue Top"
        # Target the search button by id
        submit_input = driver.find_element(By.ID, "submit_search")
        # Wait for the search result to load
        WebDriverWait(driver, wait).until(
            EC.presence_of_element_located((By.CLASS_NAME, "container"))
        )
        # Execute the code through the search_product function
        search_product(driver, search_input, user_input, submit_input)
        

        # Wait for the product link to be located first
        WebDriverWait(driver, wait).until(
            EC.presence_of_element_located((By.XPATH, "//a[contains(@href, '/product_details/') and contains(text(), 'View Product')]"))
        )
        # Target product link 
        product_link = driver.find_element(By.XPATH, "//a[contains(@href, '/product_details/') and contains(text(), 'View Product')]")
        # Execute the code through the view_product function
        view_product(driver, product_link)


        # Target quantity field
        qty_field = driver.find_element(By.ID, "quantity")
        # Ask user for quantity input
        # quantity = input("Enter quantity: ")
        quantity = 10
        # Wait for the 'Add to cart' button to be clickable
        WebDriverWait(driver, wait).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn.btn-default.cart"))
        )
        # Target 'Add to cart' button
        add_btn = driver.find_element(By.CSS_SELECTOR, ".btn.btn-default.cart")
        # Execute the code through the add_to_cart function
        add_to_cart(driver, qty_field, quantity, add_btn)


        # Wait for the 'View Cart' link to be clickable
        WebDriverWait(driver, wait).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="cartModal"]/div/div/div[2]/p[2]/a'))
        )
        # Target the 'View Cart' link
        view_cart_link = driver.find_element(By.XPATH, '//*[@id="cartModal"]/div/div/div[2]/p[2]/a')
        # Execute the code through the view_cart function
        view_cart(driver, view_cart_link)


        # Target the checkout button by class name
        checkout_btn = driver.find_element(
        By.XPATH, "//a[contains(@class, 'btn') and contains(@class, 'btn-default') and contains(@class, 'check_out') and contains(text(), 'Proceed To Checkout')]"
        )
        # Execute the code through the checkout function
        checkout(driver, checkout_btn)


        # Target the place order button
        placeOrder_btn = driver.find_element(By.XPATH, "//a[contains(@href, '/payment') and contains(text(), 'Place Order')]")
        # Execute the code through the place_order function
        place_order(driver, placeOrder_btn)


        # Target the name on card field
        cardName_field = driver.find_element(By.NAME, "name_on_card")
        # Target the card number field
        cardNumber_field = driver.find_element(By.NAME, "card_number")
        # Target the cvc field
        cvc_field = driver.find_element(By.NAME, "cvc")
        # Target the expiration month field
        expMonth_field = driver.find_element(By.NAME, "expiry_month")
        # Target the expiration year field
        expYear_field = driver.find_element(By.NAME, "expiry_year")
        # Target the pay and confirm button
        pay_btn = driver.find_element(By.ID, "submit")
        # Execute autofill_form function to Loop through each tuple then append the value to the corresponding field and click on the pay button
        autofill_form(
            driver, pay_btn, (cardName_field, card_name), 
            (cardNumber_field, card_number), (cvc_field, cvc_number), 
            (expMonth_field, expiration_month), (expYear_field, expiration_year)
        )
    finally:
        time.sleep(5)
        driver.quit()

if __name__ == "__main__":
    main()

