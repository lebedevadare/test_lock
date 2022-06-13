import allure
import pytest
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from locators import Home, ToolsShop

@allure.feature('Shop-tools')
def test_link_for_tool(browser):
    # нахождение элемента
    tools_link = browser.find_element(by=By.CSS_SELECTOR, value=Home.home.tools_link_at_home)
    # клик на ссылку
    tools_link.click()
    # нахождение списка элементов
    shop_tool_headers = browser.find_elements(by=By.CSS_SELECTOR, value=ToolsShop.product.name_product)
    assert len(shop_tool_headers) == 12, f"В выдаче {len(shop_tool_headers)}, а не 12"
