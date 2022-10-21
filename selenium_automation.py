from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec

service_path = Service(executable_path='D:\chromdriver\chromedriver.exe')
viewers_url = 'https://docs.google.com/forms/d/e/1FAIpQLScRyi9dC_B31D7kTP3lqADxnmvf-r6iMWyfXc9sXSIFzYtxQQ/viewform'

class AutoFill:
    def __init__(self):
        self.browser = webdriver.Chrome(service=service_path)
        self.browser.get(url=viewers_url)

    def wait_load(self, locator):
        WebDriverWait(self.browser, 10).until(ec.element_to_be_clickable(locator))

    def input_address(self, address):
        self.wait_load((By.XPATH, '/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input'))
        self.browser.find_element(By.XPATH, '/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(address)

    def input_price(self, price):
        self.wait_load((By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input'))
        self.browser.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(price)

    def input_link(self, link):
        self.wait_load(
            (By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input'))
        self.browser.find_element(By.XPATH,
                                  '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(
            link)

    def input_coor(self, coor):
        self.wait_load(
            (By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[1]/input'))
        self.browser.find_element(By.XPATH,
                                  '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(
            coor)
    def submit_button(self):
        self.wait_load((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div'))
        self.browser.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div').click()

    def resubmit_button(self):
        self.wait_load((By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[4]/a[2]'))
        self.browser.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[4]/a[2]').click()



