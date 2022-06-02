from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By


class BasePage:
    def __init__(self, browser):
        self.browser = browser

    def __element(self, selector: dict, index: int, link_text: str = None):
        by = None
        if link_text:
            by = By.LINK_TEXT
        elif 'css' in selector.keys():
            by = By.CSS_SELECTOR
            selector = selector['css']
        return self.browser.find_elements(by, selector)[index]

    def _click(self, selector, index=0):
        ActionChains(self.browser).move_to_element(self.__element(selector, index)).click().perform()

    def _get_element(self, selector, index):
        return self.__element(selector, index)

    def _get_element_text(self, selector, index):
        return self.__element(selector, index).text