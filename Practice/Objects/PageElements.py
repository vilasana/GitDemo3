import pytest
from selenium import webdriver
from selenium.webdriver.common import action_chains
from selenium.webdriver.support import wait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.alert import Alert
from utilities.BaseClass import BaseClass

class Elements(BaseClass):

    def __init__(self,driver):
        self.driver = driver

    radiobtn = (By.XPATH, "//input[@value='radio3']")
    country = (By.XPATH, "//input[@id='autocomplete']")
    countries = (By.XPATH, "//div[@class='ui-menu-item-wrapper']")
    dd = (By.CSS_SELECTOR, "select[id*='dropdown-class-example']")
    cb = (By.XPATH, "//input[@type='checkbox']")
    new_window_btn = (By.CSS_SELECTOR, "button[id*='openwindow']")
    new_tab = (By.LINK_TEXT, "Open Tab")
    name = (By.ID, "name")
    alertbox = (By.ID, "alertbtn")
    confirmbox = (By.ID, "confirmbtn")
    tbl = (By.XPATH, "//table[@id='product']/tbody/tr/td[4]")

    def getElements(self):
        #radiobutton
        self.driver.find_element(*Elements.radiobtn).click()

        #dropdown list
        self.driver.find_element(*Elements.country).send_keys("Un")
        self.driver.implicitly_wait(6)
        countries = self.driver.find_elements(*Elements.countries)
        #print(countries[2].text)
        #print("List is not getting printed!")
        for c in countries:
            if "united states" in c.text.casefold():
                c.click()
        #dropdown select
        dropdown = Select(self.driver.find_element(*Elements.dd))
        dropdown.select_by_value("option2")

        #checkbox
        checkbox = self.driver.find_elements(*Elements.cb)
        for c in checkbox:
            cval = c.find_element(By.XPATH,"parent::label")
            print(cval.text)
            if cval.text == "Option1":
                c.click()

        #switching to another window
        self.driver.find_element(*Elements.new_window_btn).click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        print(self.driver.title)
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])

        #switching to another tab
        self.driver.find_element(*Elements.new_tab).click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        print(self.driver.title)
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])

        #alert
        self.driver.find_element(*Elements.name).send_keys("Vilasana")
        self.driver.find_element(*Elements.alertbox).click()
        self.driver.switch_to.alert.accept()

        #confirm
        self.driver.find_element(*Elements.name).send_keys("Vilasana")
        self.driver.find_element(*Elements.confirmbox).click()
        self.driver.switch_to.alert.dismiss()

        #table
        total = 0
        amt = self.driver.find_elements(*Elements.tbl)
        for val in amt:
             total = total + int(val.text)
        assert total == 296

        #mousehover
        self. driver.execute_script("window.scrollTo(0, 1000);")
        acobj = action_chains.ActionChains(self.driver)
        btn = self.driver.find_element(By.ID, "mousehover")
        acobj.move_to_element(btn).perform()
        acobj.click(self.driver.find_element(By.LINK_TEXT, "Top")).perform()
        self. driver.execute_script("window.scrollTo(0, 1000);")

        #iframe
        frame = self.driver.find_element(By.ID, "courses-iframe")
        self.driver.switch_to.frame(frame)
        print(self.driver.find_element(By.TAG_NAME, "h2").text)
        self.driver.switch_to.default_content()
        print("This is to confirm that we have switched to default page," + self.driver.find_element(By.TAG_NAME, "h1").text)
