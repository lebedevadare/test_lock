from locators import Home, MasterDetail
from .BasePage import BasePage


class MainPage(BasePage):

    def click_at_master_link(self):
        # master_LINK = self.browser.find_element(by=By.CSS_SELECTOR, value=Home.link_master)
        self._get_element(Home.link.link_master, index=0)
        self._click(Home.home.card_names, index=2)
        # names = self.browser.find_elements(by=By.CSS_SELECTOR, value=Home.card_names)
        # names[2].click()

    def find_element_after_click(self):
        # self.browser.find_element(by=By.CSS_SELECTOR, value=MasterDetail.name_detail)
        self._get_element(MasterDetail.master.name_detail, index=0)
        self._get_element(MasterDetail.master.address_master, index=0)
        # self.browser.find_element(by=By.CSS_SELECTOR, value=MasterDetail.address_master)

    def compare_link(self):
        # telephone = self.browser.find_element(by=By.CSS_SELECTOR, value=MasterDetail.telephone_detail)
        telephone = self._get_element(MasterDetail.master.telephone_detail, index=0)
        # telephone_text = self.browser.find_element(by=By.CSS_SELECTOR, value=MasterDetail.telephone_detail).text
        telephone_text = self._get_element_text(MasterDetail.master.telephone_detail, index=0)
        telephone_href_text = telephone.get_attribute("href")
        telephone_text = f'tel:{telephone_text}'
        assert telephone_text == telephone_href_text, f'Значение в аттрибуте href отличается от  номера, значение href -- {telephone_href_text}, значение в html --  {telephone_text}'

    def find_element_master_detail(self):
        self._get_element(MasterDetail.master.name_detail, index=0)
        self._get_element(MasterDetail.master.address_master, index=0)
