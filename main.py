import selenium
from selenium import webdriver
import os
from webdriver_manager.chrome import ChromeDriverManager
import time
from creds import username, password
from selenium.webdriver.common.by import By

#Selinium setup
driver = webdriver.Chrome(ChromeDriverManager().install())

#retrieve the webpage
driver.get('https://www.hypedrop.com/en/pvp')



def login():
    # login button path
    login_button = driver.find_element(By.XPATH, '/html/body/cw-root/cw-header/nav/div[2]/div/cw-auth-buttons/div/button[2]')
    login_button.click()

    time.sleep(3)
    
    # Click on steam
    #steam_button =  driver.find_element(By.NAME, 'Steam')
    #steam_button.click()


time.sleep(3)


driver.close()
driver.quit()