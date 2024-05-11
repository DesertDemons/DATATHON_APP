from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time


# Specify the URL of the business page on Google Maps
url = 'https://www.google.com/maps/place/Dasman+Diabetes+Institute/@29.3896735,47.9908678,17z/data=!3m1!4b1!4m6!3m5!1s0x3fcf8485b33c3fef:0x344d421abea08071!8m2!3d29.3896735!4d47.9934427!16s%2Fg%2F1tf22kns?entry=ttu'

# Create an instance of the Chrome driver
driver = webdriver.Chrome()

# Navigate to the specified URL
driver.get(url)

# Wait for the reviews to load
wait = WebDriverWait(driver, 20)  # Increased the waiting time

# Scroll down to load more reviews
body = driver.find_element(By.XPATH, "//div[contains(@class, 'm6QErb') and contains(@class, 'DxyBCb') and contains(@class, 'kA9KIf') and contains(@class, 'dS8AEf')]")
num_reviews = len(driver.find_elements(By.CLASS_NAME, 'wiI7pd'))
while True:
    body.send_keys(Keys.END)
    time.sleep(2)  # Adjust the delay based on your internet speed and page loading time
    new_num_reviews = len(driver.find_elements(By.CLASS_NAME, 'wiI7pd'))
    if new_num_reviews == num_reviews:
        # Scroll to the top to ensure all reviews are loaded
        body.send_keys(Keys.HOME)
        time.sleep(2)
        break
    num_reviews = new_num_reviews

# Wait for the reviews to load completely
wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'wiI7pd')))

# Extract the text of each review
review_elements = driver.find_elements(By.CLASS_NAME, 'wiI7pd')
reviews = [element.text for element in review_elements]

# Print the reviews
print(reviews)

# Close the browser
driver.quit()

