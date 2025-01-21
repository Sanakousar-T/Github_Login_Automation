
from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By 
from selenium.webdriver.chrome.service import Service 
from webdriver_manager.chrome import ChromeDriverManager 
import time

# Initialize the Chrome WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Open GitHub login page
driver.get("https://github.com/login")

# Wait for the page to load
time.sleep(2)

# Find the username/email input field
username_field = driver.find_element(By.ID, "login_field")
username_field.send_keys("sanakousar.tallihal@gmail.com")  # Replace with your GitHub username

# Find the password input field
password_field = driver.find_element(By.ID, "password")
password_field.send_keys("github_password")  # Replace with your GitHub password

# Press Enter to submit the login form
password_field.send_keys(Keys.RETURN)

# Wait for some time to allow the login to complete
time.sleep(5)

# Check if login was successful by checking if the profile icon exists
try:
    profile_icon = driver.find_element(By.CSS_SELECTOR, "img[alt='@sanakousar.tallihal@gmail.com']")  # Replace with your GitHub username
    print("Login successful")
except Exception as e:
    print("Login failed")

# Close the browser
driver.quit()
