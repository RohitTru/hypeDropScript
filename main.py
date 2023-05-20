import selenium
from selenium import webdriver
import os
from webdriver_manager.chrome import ChromeDriverManager
import time
from creds import username, password
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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
    
def two_factor_auth_approval():
    required_url = 'https://steamcommunity.com/openid/login?openid.mode=checkid_setup&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.return_to=https%3A%2F%2Fapi.hypedrop.com%2Fauth%2Fsteam%2Freturn&openid.realm=https%3A%2F%2Fapi.hypedrop.com?openid.mode=checkid_setup&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.return_to=https%3A%2F%2Fapi.hypedrop.com%2Fauth%2Fsteam%2Freturn&openid.realm=https%3A%2F%2Fapi.hypedrop.com'

    while True:
        current_url = driver.current_url
    
        if str(current_url) == str(required_url):
            sign_in_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="imageLogin"]')))
            sign_in_button.click()
            print('logging in...')
            break
        if str(current_url) != str(required_url):
            time.sleep(1)

def navigation():
    free_drop_button = driver.find_element(By.XPATH, '/html/body/cw-root/cw-header/nav/div[1]/li[5]/a')
    free_drop_button.click()
    print("opening free gifts page")

def open_cases():
    fifth_drop = driver.find_element(By.XPATH, '/html/body/cw-root/mat-sidenav-container/mat-sidenav-content/div/cw-daily-rewards/div/div[2]/cw-reward-tile[5]/cw-flip-card/div/div[1]/div')
    fifth_drop.click()


def main():
    time.sleep(3)
    login_steam()
    
    time.sleep(1)
    two_factor_auth_approval()
   
    time.sleep(1)
    navigation()

    time.sleep(1)
    driver.refresh()

    time.sleep(1)
    open_cases()
   
    time.sleep(300)

    driver.close()
    driver.quit()


if __name__ == "__main__":
    main()



