from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Path to chromedriver executable
# chromedriver_path = r'C:\chromedriver-win32\chromedriver.e yourxe'  # Replace with your chromedriver executable path

web = 'https://www.whoscored.com/LiveScores'
path = Service(executable_path=r"C:\Users\Downloads\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=path)
driver.get(web)

driver.maximize_window()

#Pagination
prev_page = driver.find_element(By.XPATH, '//button[@id="dayChangeBtn-prev"]')

last_page = -30

current_page = 1

while current_page >= last_page:
    
        
    time.sleep(5)
    prev_page_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[@id="dayChangeBtn-prev"]'))               )
    prev_page_button.click()
    
    current_page = current_page - 1


driver.quit()
