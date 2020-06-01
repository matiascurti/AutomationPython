from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

#import unittext 
import time


#Base
driver = webdriver.Chrome('chromedriver.exe')
driver.implicitly_wait(10) # seconds
basepage = 'https://www.youtube.com/'

#webelements
search_box = '//input[@id="search"]'
search_box_bottom = '//*[@id="search-icon-legacy"]'

driver.get(basepage)
driver.maximize_window()

driver.find_element_by_xpath(search_box).send_keys ('Stephen Ridley')
driver.find_element_by_xpath (search_box_bottom).click()

time.sleep(5)


driver.close()
driver.quit()