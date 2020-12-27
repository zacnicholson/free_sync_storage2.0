from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from time import sleep
import random
import csv

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument('window-size=1920x1080')



with open('output.txt') as f:
    reader = csv.reader(f)
    row1 = next(f)
    row2 = next(f)

email_name = row1
referral_code = row2

while True:
    with open("numbers.csv") as f:
        lines = f.readlines()
        numbers = random.choice(lines)


    class SyncBot:

        def __init__(self):
            self.driver = webdriver.Chrome('/Users/zacnicholson/PycharmProjects/free_sync_storage/chromedriver', options=chrome_options)

        def new_account(self):
            self.driver.get(f'https://www.sync.com/get-started?_sync_refer={referral_code}')
            email = self.driver.find_element_by_xpath(
                '/html/body/div[1]/section/div/div[2]/div[2]/div/div/form/div[1]/input')
            email.send_keys(f'{email_name}+{numbers}@gmail.com')

            sleep(1)

            password = self.driver.find_element_by_xpath(
                '/html/body/div[1]/section/div/div[2]/div[2]/div/div/form/div[2]/input')
            password.send_keys('Password!!')
            sleep(2)
            confirm_password = self.driver.find_element_by_xpath(
                '/html/body/div[1]/section/div/div[2]/div[2]/div/div/form/div[3]/input')
            confirm_password.send_keys("Password!!")

            sleep(1)

            terms = self.driver.find_element_by_xpath(
                '/html/body/div[1]/section/div/div[2]/div[2]/div/div/form/div[4]/label[3]/table/tbody/tr/td[1]/input')
            terms.click()

            complete = self.driver.find_element_by_xpath(
                '/html/body/div[1]/section/div/div[2]/div[2]/div/div/form/div[5]')

            sleep(1)

            complete.click()
            sleep(10)
            self.driver.close()

        sleep(2)


    bot = SyncBot()
    bot.new_account()
