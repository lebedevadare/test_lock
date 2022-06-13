import allure
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from locators import Pagination

@allure.feature('Пагинация')
def test_pagination(browser):
    # нашли элементы
    el = browser.find_element(by=By.CSS_SELECTOR, value=Pagination.pag.header_post)
    ul = browser.find_elements(by=By.CSS_SELECTOR, value=Pagination.pag.number_ul_pagination)
    # клик по пагинации и переход на др страницу
    ul[2].click()
    # ожидание и проверка селектора
    wait = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div a.post__header")))
    print(wait.text)
