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
driver.get('https://steamcommunity.com/openid/loginform/?goto=%2Fopenid%2Flogin%3Fopenid.mode%3Dcheckid_setup%26openid.ns%3Dhttp%253A%252F%252Fspecs.openid.net%252Fauth%252F2.0%26openid.identity%3Dhttp%253A%252F%252Fspecs.openid.net%252Fauth%252F2.0%252Fidentifier_select%26openid.claimed_id%3Dhttp%253A%252F%252Fspecs.openid.net%252Fauth%252F2.0%252Fidentifier_select%26openid.return_to%3Dhttps%253A%252F%252Fapi.hypedrop.com%252Fauth%252Fsteam%252Freturn%26openid.realm%3Dhttps%253A%252F%252Fapi.hypedrop.com%3Fopenid.mode%3Dcheckid_setup%26openid.ns%3Dhttp%253A%252F%252Fspecs.openid.net%252Fauth%252F2.0%26openid.identity%3Dhttp%253A%252F%252Fspecs.openid.net%252Fauth%252F2.0%252Fidentifier_select%26openid.claimed_id%3Dhttp%253A%252F%252Fspecs.openid.net%252Fauth%252F2.0%252Fidentifier_select%26openid.return_to%3Dhttps%253A%252F%252Fapi.hypedrop.com%252Fauth%252Fsteam%252Freturn%26openid.realm%3Dhttps%253A%252F%252Fapi.hypedrop.com')


def login_steam():
    
    username_field = driver.find_element(By.XPATH, '//*[@id="responsive_page_template_content"]/div[1]/div[1]/div/div/div/div[2]/div/form/div[1]/input')
    username_field.click()
    username_field.send_keys(str(username))
    print('inputed username')

    time.sleep(1)
    password_field = driver.find_element(By.XPATH, '//*[@id="responsive_page_template_content"]/div[1]/div[1]/div/div/div/div[2]/div/form/div[2]/input')
    password_field.click()
    password_field.send_keys(str(password))
    print('inputed password')

    time.sleep(1)
    sign_in = driver.find_element(By.XPATH, '//*[@id="responsive_page_template_content"]/div[1]/div[1]/div/div/div/div[2]/div/form/div[4]')
    sign_in.click()
    
    # figure out how to wait for 2 factor auth page to load
    time.sleep(20)

    sign_in_button = driver.find_element(By.XPATH, '//*[@id="imageLogin"]')
    sign_in_button.click()

time.sleep(3)
login_steam()
time.sleep(300)



driver.close()
driver.quit()