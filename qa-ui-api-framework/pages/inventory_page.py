class InventoryPage:
    def __init__(self,page):
        self.page = page
        self.page_title = page.locator(".title")
        self.inventory_items = page.locator(".inventory_item")
        self.inventory_item_names = page.locator(".inventory_item_name")
        self.inventory_item_prices = page.locator(".inventory_item_price")
        self.add_to_cart_buttons = page.locator(".button.btn_inventory")


    def get_current_url(self):
        return self.page.url
    
    def get_page_title_text(self):
        return self.page_title.text_content()
    
    def get_inventory_count(self):
        self.inventory_items.first.wait_for(state="visible")
        return self.inventory_items.count()

    def is_page_title_visible(self):
        self.page_title.wait_for(state="visible")
        return self.page_title.is_visible()