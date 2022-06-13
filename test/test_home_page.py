import allure

from variables import URL
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from locators import Home, MasterDetail, HomePost
from page_object import MainPage, HomePage,PostPage


def test_find_element_for_page_home(browser):
    MainPage(browser).click_at_master_link()
    MainPage(browser).find_element_master_detail()
    MainPage(browser).compare_link()

@allure.story('Story telephone at home page')
def test_home_page_telephone(browser):
    HomePage(browser).compare_link_home()

def test_map_with_marker(browser):
    HomePage(browser).find_element_map()



def test_home_page_blog(browser):
    PostPage(browser).find_element_post_home(2)

