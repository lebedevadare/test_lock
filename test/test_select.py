import pytest
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


def test_select_header(browser):
    # нахождение элемнта
    select = Select(browser.find_element(By.NAME, 'select-country'))
    print(select)
    # выбор в селекте бразилии
    select.select_by_visible_text('Brazil')
    # нахождение элемента
    browser.find_element(by=By.CSS_SELECTOR, value='a.city-master-link')
    select = Select(browser.find_element(By.NAME, 'select-country'))
    # выбор в селекте росии
    select.select_by_visible_text('Russia')
    # нахождение элемента
    text_header_list_master = browser.find_element(by=By.CSS_SELECTOR, value='a.city-master-link')
    # проверка
    assert text_header_list_master.text == "Мастера в Москва (20)", f"Выдача такая{text_header_list_master.text}"
