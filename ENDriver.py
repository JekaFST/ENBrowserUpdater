# -*- coding: utf-8 -*-
from Const import URLS, DOMAIN, GAME_ID
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# REFRESH_PATH = '/html/body/div/div[1]/ul/li[1]/a'
REFRESH_PATH = './/li[contains(@class, "refresh")]/a'


class ENChromeDriver(object):
    def __init__(self, login, password, domain=DOMAIN, game_id=GAME_ID):
        self.driver = webdriver.Chrome('chromedriver.exe')
        self.domain = domain
        self.game_id = game_id
        self.login = login
        self.password = password

    def close_browser(self):
        self.driver.quit()

    def login_to_en(self):
        self.driver.get(self.domain + URLS['login_url_ending'])
        login_elem = self.driver.find_element_by_id('txtLogin')
        # login_elem.clean()
        login_elem.send_keys(self.login)
        password_elem = self.driver.find_element_by_id('txtPassword')
        # password_elem.clean()
        password_elem.send_keys(self.password)
        login_button = self.driver.find_element_by_name('EnButton1')
        login_button.click()

    def open_game(self):
        self.driver.get(self.domain + URLS['game_url_ending'] + self.game_id)

    def refresh_level_page(self):
        refresh_elem = self.driver.find_element_by_xpath(REFRESH_PATH)
        refresh_elem.click()

# if __name__ == '__main__':
#     en_driver = ENChromeDriver()
