from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

username = "test@name.come"
password = "Test@123"

Service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=Service)

driver.get("https://mahamasthakabhisheka2025.com/login")

time.sleep(10)

driver.quit()

