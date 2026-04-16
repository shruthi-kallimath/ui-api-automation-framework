from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


def test_inventory_page_loads_after_login(browser_page, config):
    login_page = LoginPage(browser_page)
    inventory_page = InventoryPage(browser_page)

    login_page.open(config["base_url"])
    login_page.login(config["username"], config["password"])

    assert "inventory" in inventory_page.get_current_url()
    assert inventory_page.is_page_title_visible()
    assert inventory_page.get_page_title_text()== "Products"


def test_products_are_displayed_on_inventory_page(browser_page, config):
    login_page = LoginPage(browser_page)
    inventory_page = InventoryPage(browser_page)

    login_page.open(config["base_url"])
    login_page.login(config["username"], config["password"])

    assert inventory_page.get_inventory_count() > 0