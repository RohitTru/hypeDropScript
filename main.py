import selenium
from selenium import webdriver
import os
from webdriver_manager.chrome import ChromeDriverManager
import time
driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get('https://www.youtube.com/@MusicbyChoice')

time.sleep(30)

driver.close()
driver.quit()