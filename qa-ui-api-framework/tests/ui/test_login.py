from pages.login_page import LoginPage


def test_valid_login(browser_page, config):
    login_page = LoginPage(browser_page)
    login_page.open(config["base_url"])
    login_page.login(config["username"], config["password"])

    assert "inventory" in login_page.get_current_url()


def test_invalid_login(browser_page, config):
    login_page = LoginPage(browser_page)
    login_page.open(config["base_url"])
    login_page.login("standard_user", "wrong_password")

    assert "Epic sadface" in login_page.get_error_message()

def test_locked_out_user_login(browser_page,config):
    login_page = LoginPage(browser_page)
    login_page.open(config["base_url"])
    login_page.login("locked_out_user", "secret_sauce")

    assert "Sorry, this user has been locked out." in login_page.get_error_message()

def test_blank_username_login(browser_page,config):
    login_page = LoginPage(browser_page)
    login_page.open(config["base_url"])
    login_page.login("","secret_sauce")

    assert "Username is required" in login_page.get_error_message()

def test_blank_password_login(browser_page,config):
    login_page = LoginPage(browser_page)
    login_page.open(config["base_url"])
    login_page.login("standard_user","")

    assert "Password is required" in login_page.get_error_message()

def test_blank_fields_login(browser_page,config):
    login_page = LoginPage(browser_page)
    login_page.open(config["base_url"])
    login_page.login("","")


    assert "Username is required" in login_page.get_error_message()

def test_invalid_username_login(browser_page,config):
    login_page = LoginPage(browser_page)
    login_page.open(config["base_url"])
    login_page.login("invalid_user","secret_sauce")

    
    assert "Epic sadface" in login_page.get_error_message()
    assert "inventory" not in login_page.get_current_url()


    



