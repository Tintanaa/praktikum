from playwright.sync_api import Page, expect

class CartPage:
    def __init__(self, page: Page):
        self.page = page
        self.checkout_button = page.locator("#checkout")

    def navigate(self):
        self.page.click(".shopping_cart_link")

    def proceed_to_checkout(self):
        self.checkout_button.click()