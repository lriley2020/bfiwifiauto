#!/home/pi/bfwifiauto/env/bin/python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from selenium.webdriver.chrome.options import *
from time import sleep
options = Options()
options.add_argument("headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
driver = webdriver.Chrome(options=options)

driver.get("https://getwifi.no/")
driver.set_window_size(808, 816)
driver.find_element(By.CSS_SELECTOR, ".btn-choose-ltd").click()
driver.find_element(By.ID, "swal2-checkbox").click()
driver.find_element(By.CSS_SELECTOR, ".swal2-confirm").click()
timeout = 5
element_present = WebDriverWait(driver,timeout).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, '.connect')))
element_present.click()
sleep(5)
#driver.find_element(By.CSS_SELECTOR, ".connect").click()
driver.quit()

