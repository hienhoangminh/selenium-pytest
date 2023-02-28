"""
These tests cover DuckDuckGo searches.
"""
import pytest
from pages.search import DuckDuckGoSearchPage
from pages.result import DuckDuckGoResultPage

@pytest.mark.parametrize('phrase', ['panda', 'python', 'polar bear'])
def test_basic_duckduckgo_search(browser, phrase):

    search_page = DuckDuckGoSearchPage(browser)
    result_page = DuckDuckGoResultPage(browser)
    # Given the DuckDuckGo home page is displayed
    search_page.load()
    
    # When the user searches for "panda"
    search_page.search(phrase)

    # And the search result query is "panda"
    assert phrase == result_page.search_input_value()

    # And the search result links pertain to "panda"
    # for title in result_page.result_link_titles():
    #     assert PHRASE.lower() in title.lower()
    
    # Then the search result title contains "panda"
    assert phrase in result_page.title()