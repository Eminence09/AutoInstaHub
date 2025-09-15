from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time



driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.instagram.com/accounts/emailsignup/")

time.sleep(5)

email = "yashbanait05@gmail.com"
full_name = "vivan shah"
username = "vivanshahn123"
password = "YasH@1#3%2BanaIt"


try:
    cookies_button = driver.find_element(By.XPATH, '//button[text()="Only allow essential cookies"]')
    cookies_button.click()

except:
    print('ok')

driver.find_element(By.NAME, 'emailOrPhone').send_keys(email)   
driver.find_element(By.NAME, 'password').send_keys(password)   
driver.find_element(By.NAME, 'fullName').send_keys(full_name)   
driver.find_element(By.NAME, 'username').send_keys(username)  
# driver.find_element(By., 'username')  

# dropdown_element = driver.find_element_by_id("myDropdown")


driver.find_element(By.XPATH, '//button[@type="submit"]').click()

time.sleep(2)

a = driver.find_element(By.XPATH, '//option[@title="2000"]').click()
time.sleep(2)



driver.find_element(By.XPATH, '//button[@type="button" and text()="Next"]').click()


# driver.find_element(By.XPATH, '//button[@type="button" and text()="Next"]').click()
# driver.find_element(By.XPATH, '//button[@type="button"]').click()

# dropdown = driver.find_element(By.CLASS_NAME, "_aau-")

# def select_dropdown_option(dropdown, option_text):
#     for option in dropdown.options:
#         if option.text == option_text:
#             option.click()
#             break

# select_dropdown_option(dropdown, "2000")

# select = Select(dropdown_element)
# select.select_by_visible_text("2000")
# time.sleep(2)


try:
    confirmation_code_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located(By.NAME, 'email_confirmation_code'))
    next_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(By.XPATH, '//button[@role="button" and text()="Next"]'))
    
    expected_code = "12341"
    EC.confirmation_code_input.send_key(expected_code)
    
    entered_code = confirmation_code_input.get_attribute("value")
    
    if entered_code == expected_code:   
        print("Confirmation code matched. clicking next!")
    else:
        print("No match found!")

except TimeoutException:
    print("Timeout!")

finally:
    pass


time.sleep(5000)
print("Account Created Successfully")