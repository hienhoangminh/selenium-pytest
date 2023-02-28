from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class DuckDuckGoSearchPage:
    
    URL = "https://www.duckduckgo.com"
    SEARCH_INPUT = (By.ID, 'search_form_input_homepage')
    
    def __init__(self, browser):
        self._browser = browser
        self._wait = WebDriverWait(self._browser, 30)
    
    def load(self):
        self._browser.get(self.URL)
    
    def search(self, phrase):
        self._wait.until(EC.presence_of_element_located(self.SEARCH_INPUT))
        search_input = self._browser.find_element(*self.SEARCH_INPUT)
        search_input.send_keys(phrase + Keys.RETURN)
            