# SeleniumEShopAutomation - E-commerce Website Automation


## Introduction
This repository contains Python code designed to automate interactions with a simulated e-commerce website (https://www.automationexercise.com/) using Selenium. The automation script simulates a user's journey through the website, including logging in, searching for a product, adding it to the cart, and placing an order. The script uses the Selenium WebDriver to interact with the website's elements and perform various actions.

## Prerequisites
Before running the script, ensure you have the following components installed:


- ##### Python 3.x

- ##### ChromeDriver (compatible with your Chrome browser version)

- ##### Selenium WebDriver

- ##### Chrome browser

- ##### uBlock Origin extension (or any ad-blocking extension of your choice)

## Installation
1. #### Clone the repository to your local machine:
```
git clone https://github.com/Nightowl914/SeleniumEShopAutomation.git
```

2. #### Install the required Python packages:
```
pip install selenium
```

3. #### Download ChromeDriver:
   ##### Download the appropriate ChromeDriver version from (https://googlechromelabs.github.io/chrome-for-testing/#stable) and place the executable in the project directory.

4. #### Install an Ad-Blocking Extension:
   ##### Install an ad-blocking extension such as uBlock Origin from the Chrome Web Store or your preferred source.

5. #### Locate the Extension ID:
 - #####  After installation, locate the extension using the extension ID.
 - #####  Navigate to C:\Users\[user_name]\AppData\Local\Google\Chrome\User Data\Default\Extensions\[folder_with_id].

6. #### Copy the Extension Folder:
   ##### Access the [folder_with_id] and copy the folder inside (e.g., a folder with the name 5.17.1_0) to a location of your choice.

7. #### Compress the Folder:
   ##### Compress the copied folder into a zip file.

8. #### Rename the Zip File:
   ##### Rename the zip file to a name of your choice.

9. #### Change File Type:
   ##### Change the file type of the zip file to .crx.

10. #### Move to SeleniumEShopAutomation's Extensions Folder:
    ##### Drag and drop the .crx file inside the SeleniumEShopAutomation's extensions folder.

## Usage
#### 1. Open the main.py file.
#### 2. Update the following variables with your specific details:
- ##### user_email: Your login email
- ##### user_pwd: Your login password
- ##### card_name: Name on your credit card
- ##### card_number: Credit card number
- ##### cvc_number: CVC number
- ##### expiration_month: Expiration month of the credit card
- ##### expiration_year: Expiration year of the credit card

#### 3. Specify your own download path for invoices:
```
chrome_options.add_experimental_option("prefs", {
    "download.default_directory": "/path/to/your/download/directory"
}) 
```
#### 4. Run the script:
```
python main.py
```
##### The script will launch a Chrome browser with the ad-blocking extension, navigate through the specified URLs, and perform the automated actions.

## Functions
##### The script is organized into functions for better modularity:

- ##### initialize_driver: Initializes the Selenium WebDriver with Chrome options, extensions, and preferences.
- ##### navigate_to_url: Navigates to the specified URL.
- ##### autofill_form: Automates form filling based on provided field values.
- ##### search_product: Searches for a product on the website.
- ##### view_product: Views details of a specific product.
- ##### add_to_cart: Adds a specified quantity of a product to the shopping cart.
- ##### view_cart: Navigates to the shopping cart.
- ##### checkout: Initiates the checkout process.
- ##### place_order: Places an order in the checkout process.
- ##### download_invoice: Downloads the order invoice.

## Error Handling
##### The script includes error handling for 'NoSuchElementException' and 'TimeoutException'. If an unexpected error occurs, it will be displayed with a corresponding message.




## Note
- ##### The script uses Chrome as the default browser. Ensure Chrome is installed on your machine.
- ##### The chromedriver.exe executable must be compatible with your Chrome browser version.
- ##### Feel free to customize the script further based on your specific requirements. Happy automating!
