import selenium
from selenium import webdriver
import os
from webdriver_manager.chrome import ChromeDriverManager
import time
from creds import username, password

#Selinium setup
driver = webdriver.Chrome(ChromeDriverManager().install())

#retrieve the webpage
driver.get('https://www.hypedrop.com/en/pvp')























time.sleep(30)

driver.close()
driver.quit()