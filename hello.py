from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# Specify the path to the WebDriver
driver_path = "C:/WebDriver/chromedriver.exe"  # Make sure to include the .exe extension

# Set up the ChromeDriver service
service = Service(driver_path)

# Initialize the WebDriver
driver = webdriver.Chrome(service=service)

# Open a webpage
driver.get("https://www.example.com")

# Example action: print the page title

if driver.title == 'Example Domain':
    print('passed')
else:
    print('failed')

# Close the browser
driver.quit()