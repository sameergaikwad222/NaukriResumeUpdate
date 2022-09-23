from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from cred import username, password, cvfullpath,chromeDriverPath
import os


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("excludeSwitches", ['enable-logging'])
driver = webdriver.Chrome(
    options=chrome_options, executable_path=chromeDriverPath)
wait = WebDriverWait(driver, timeout=25, poll_frequency=1)
action = ActionChains(driver)

# Navigate to url
driver.get("https://www.naukri.com/nlogin/login")
driver.maximize_window()
uname = driver.find_element_by_id('usernameField')
uname.send_keys(username)
pass1 = driver.find_element_by_id('passwordField')
pass1.send_keys(password)
submitButton = driver.find_element_by_xpath(
    '/html/body/div[2]/div/div/div/div/div/div/div[2]/div/form/div[3]/div[3]/div/button[1]')
submitButton.click()

driver.implicitly_wait(15)

try:
    skip = driver.find_element_by_xpath(
        '/html/body/div[2]/div/div/span/div/div/div/div/div/section/div[2]/div[2]/div/div[1]/form/button')
    skip.click()
except:
    pass


profileLink = driver.get('https://www.naukri.com/mnjuser/profile?id=&altresid')
driver.implicitly_wait(5)

loadcv = driver.find_element_by_id('attachCV')
loadcv.send_keys(cvfullpath)
driver.implicitly_wait(5)
parentPriew = driver.find_element_by_class_name('cvPreview')
validationDiv = parentPriew.find_element_by_class_name('left')
validationtag = validationDiv.find_element_by_tag_name('b')
print(validationtag.get_attribute("value"))
logoutEle = driver.find_element_by_css_selector(
    'a[href="https://www.naukri.com/nlogin/logout"]')
logoutEle.click()
driver.quit()
