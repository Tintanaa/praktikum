import pytest
from playwright.sync_api import Page, expect
from pages.loginpage import LoginPage
from pages.inventorypage import InventoryPage
from pages.cartpage import CartPage
from pages.checkoutpage import CheckoutPage

@pytest.fixture(scope="function", autouse=True)
def before_each_after_each(page: Page):
    yield
    page.close()

def test_successful_login(page: Page):
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login("standard_user", "secret_sauce")
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")

def test_failed_login(page: Page):
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login("wrong_user", "wrong_password")
    expect(login_page.error_message).to_be_visible()
    expect(login_page.error_message).to_contain_text("Username and password do not match any user in this service")


def test_add_to_cart(page: Page):
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login("standard_user", "secret_sauce")
    
    inventory_page = InventoryPage(page)
    inventory_page.add_to_cart("sauce-labs-backpack")
    expect(inventory_page.cart_badge).to_have_text("1")

def test_checkout(page: Page):
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login("standard_user", "secret_sauce")
    
    inventory_page = InventoryPage(page)
    inventory_page.add_to_cart("sauce-labs-backpack")
    
    cart_page = CartPage(page)
    cart_page.navigate()
    cart_page.proceed_to_checkout()
    
    checkout_page = CheckoutPage(page)
    checkout_page.fill_information("John", "Doe", "12345")
    checkout_page.complete_order()
    
    expect(checkout_page.thank_you_header).to_have_text("Thank you for your order!")

def test_logout(page: Page):
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login("standard_user", "secret_sauce")
    
    inventory_page = InventoryPage(page)
    inventory_page.logout()
    
    expect(page).to_have_url("https://www.saucedemo.com/")