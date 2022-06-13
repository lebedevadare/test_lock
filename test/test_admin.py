import allure

from variables import PASSWORD, USERNAME, URL
import pytest
import selenium
from selenium import webdriver
from page_object import AdminPage
from selenium.webdriver.common.by import By
from locators import LocatorAdmin

@allure.feature("Aвторизация в админке")
def test_login(browser):
    admin_page = AdminPage(browser)
    admin_page.open(URL)
    admin_page.input_username(USERNAME)
    admin_page.input_password(PASSWORD)
    admin_page.submit_login()
    user_tools = browser.find_element(By.ID, LocatorAdmin.id_user_tools)

