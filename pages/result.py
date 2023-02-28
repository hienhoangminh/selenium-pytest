
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class DuckDuckGoResultPage:
    
    RESULT_LINKS = (By.CSS_SELECTOR, 'a.result__a')
    SEARCH_INPUT = (By.ID, 'search_form_input')
    
    def __init__(self, browser):
        self._browser = browser
        self._wait = WebDriverWait(self._browser, 30)

    def result_link_titles(self):
        links = self._browser.find_elements(*self.RESULT_LINKS)
        titles = [link.text for link in links]
        return titles
    
    def search_input_value(self):
        search_input = self._browser.find_element(*self.SEARCH_INPUT)
        value = search_input.get_attribute('value')
        return value

    
    def title(self):
        return self._browser.title
            