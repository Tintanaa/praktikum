from playwright.sync_api import Page, expect

class InventoryPage:
    def __init__(self, page: Page):
        self.page = page
        self.cart_badge = page.locator(".shopping_cart_badge")
        self.burger_menu = page.locator("#react-burger-menu-btn")
        self.logout_link = page.locator("#logout_sidebar_link")

    def add_to_cart(self, item_id: str):
        self.page.click(f"#add-to-cart-{item_id}")

    def get_cart_count(self):
        return self.cart_badge.inner_text()

    def open_burger_menu(self):
        self.burger_menu.click()

    def logout(self):
        self.open_burger_menu()
        self.logout_link.click()
