import time

class ShopifyManager:
    def __init__(self, api_key, store_url):
        self.api_key = api_key
        self.store_url = store_url
        self.connected = False
        
    def connect(self):
        if self.api_key and self.store_url:
            self.connected = True
            print(f"Connected to Shopify Store: {self.store_url}")
        else:
            print("Missing credentials for Shopify.")

    def list_product(self, title, description, price, images):
        if not self.connected:
            self.connect()
            
        print(f"Listing new product '{title}' for ${price}...")
        time.sleep(1)
        # Call shopify REST API here
        return {"status": "success", "product_id": "123456789"}
        
    def adjust_price(self, product_id, new_price):
        print(f"Adjusting price for Product {product_id} to ${new_price}")
        time.sleep(0.5)
        return True
