import pytest
from playwright.sync_api import sync_playwright
from utils.config_reader import load_config
from utils.api_client import APIClient

@pytest.fixture(scope="session")
def config():
    return load_config()


@pytest.fixture(scope="session")
def api_client(config):
    return APIClient(config["api_base_url"])

@pytest.fixture(scope="function")
def browser_page(config):
    with sync_playwright() as p:
        browser_type = getattr(p, config["browser"])
        browser = browser_type.launch(headless=config["headless"])
        page = browser.new_page()
        yield page
        browser.close()