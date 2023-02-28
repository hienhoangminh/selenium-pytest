import pytest
import json
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

@pytest.fixture
def config(scope='session'): # Run the config fixture only one time.
    with open('config.json') as config_file:
        config = json.load(config_file)
    
    assert config['browser'] in ['Firefox', 'Chrome', 'headless']
    assert isinstance(config['implicit_wait'], int)
    assert config['implicit_wait'] > 0
    
    return config    

@pytest.fixture
def browser(config):
    
    if config['browser'] == 'Chrome':
        opts = webdriver.ChromeOptions()
        if config['headless']:
            opts.add_argument('headless')
        b = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=opts)
    elif config['browser'] == 'Firefox':
        opts = webdriver.FirefoxOptions()
        if config['headless']:
            opts.headless = True
        b = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=opts)
    else:
        raise Exception(f'Browser "{config["browser"]}" is not supported')
    
    b.implicitly_wait(config['implicit_wait'])

    # Return the WebDriver instance for the setup
    yield b

    # Quit the WebDriver instance for the teardown
    b.quit()