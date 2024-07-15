from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementClickInterceptedException
import time
import os

user = os.environ["USER"]
username = os.environ["USERNAME"]
password = os.environ["PASSWORD"]


class InstaFollower:
    def __init__(self):
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=self.chrome_options)

    def login(self):
        self.driver.get(url="https://www.instagram.com/accounts/login/")
        try:
            time.sleep(3)
            user_name = self.driver.find_element(by=By.XPATH, value='//*[@id="loginForm"]/div/div[1]/div/label/input')
            user_name.send_keys(username)
            time.sleep(1)
            pass_word = self.driver.find_element(by=By.XPATH, value='//*[@id="loginForm"]/div/div[2]/div/label/input')
            pass_word.send_keys(password)
            time.sleep(1)
            login = self.driver.find_element(by=By.XPATH, value='//*[@id="loginForm"]/div/div[3]/button')
            login.click()
            time.sleep(5)
            login_info = self.driver.find_element(by=By.XPATH, value="//div[contains(text(), 'Not now')]")
            if login_info:
                login_info.click()
            time.sleep(3)
            turn_on = self.driver.find_element(by=By.XPATH, value="//button[contains(text(), 'Not Now')]")
            if turn_on:
                turn_on.click()
            time.sleep(3)
        except NoSuchElementException:
            self.driver.quit()
            self.login()

    def find_followers(self):
        time.sleep(3)
        self.driver.get(url=f"https://www.instagram.com/{user}/followers/")
        try:
            time.sleep(6)
            followers_page = self.driver.find_element(by=By.XPATH,
                                                      value='/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[2]/div/div[2]/section/main/div/header/section[3]/ul/li[2]/div/a')
            followers_page.click()
            time.sleep(2)
            modal = self.driver.find_element(by=By.XPATH,
                                             value='/html/body/div[6]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div[2]')
            for i in range(5):
                self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
                time.sleep(2)

        except NoSuchElementException:
            # self.driver.quit()
            # self.find_followers()
            pass

    def follow(self):
        time.sleep(2)
        p = self.driver.find_element(by=By.XPATH, value='/html/body/div[6]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div[2]')
        follows = p.find_elements(by=By.TAG_NAME, value="button")
        for button in follows:
            try:
                button.click()
                time.sleep(2)
            except ElementClickInterceptedException:
                cancel = self.driver.find_element(by=By.XPATH, value="//button[contains(text(), 'Cancel')]")
                cancel.click()
                time.sleep(1.5)


obj = InstaFollower()
obj.login()
obj.find_followers()
obj.follow()
