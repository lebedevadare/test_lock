from .BasePage import BasePage
from locators import Home, MasterDetail


class HomePage(BasePage):
    def find_element_tel(self):
        # browser.find_element(by=By.CSS_SELECTOR, value=Home.home_address)
        self._get_element(Home.home.home_address, index=0)

    def compare_link_home(self):
        # browser.find_element(by=By.CSS_SELECTOR, value=Home.home_address)
        telephone_home = self._get_element(Home.home.home_address, index=0)
        # telephone_home = browser.find_element(by=By.CSS_SELECTOR, value=Home.phone_home)
        telephone_text_home = self._get_element_text(Home.home.home_address, index=0)
        telephone_href_text_home = telephone_home.get_attribute("href")
        print(telephone_href_text_home)
        telephone_text_home = f'tel:{telephone_text_home}'
        assert telephone_text_home == telephone_href_text_home, f'Значение в аттрибуте href отличается от  номера, значение href -- {telephone_href_text_home}, значение в html --  {telephone_text_home}'

    def find_element_map(self):
        self._get_element(Home.map.map_home, index=0)
        self._get_element(Home.map.marker_icon_at_map, index=0)

