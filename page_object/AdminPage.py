from selenium.webdriver.common.by import By


class AdminPage:
    def __init__(self, browser):
        self.browser = browser
        self.path = 'admin/'

    def open(self, url):
        self.browser.get(url + self.path)

    def input_username(self, text):
        self.browser.find_element(By.NAME, 'username').clear()
        self.browser.find_element(By.NAME, 'username').send_keys(text)

    def input_password(self, text):
        self.browser.find_element(By.NAME, 'password').clear()
        self.browser.find_element(By.NAME, 'password').send_keys(text)

    def submit_login(self):
        self.browser.find_element(By.CSS_SELECTOR, '[type = "submit"]').click()
