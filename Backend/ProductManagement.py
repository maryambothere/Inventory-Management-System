from Database.DatabaseManagement import DatabaseManagement

class ProductManagement:

    def __init__(self):
        self.db_manager = DatabaseManagement()
        self.products = self.db_manager.fetch_product_data()
              


    def addProducts(self, product_name, product_price, product_brand):
        if product_name in self.products:
            return "Product already exists!"
        
        self.products[product_name] = {"price": product_price, "brand": product_brand, "Quantity": 0}
        self.db_manager.update_products(self.products)
        return "Added"
    

    def deleteProduct(self, product_name):
        if product_name not in self.products:
            return "Product does'nt exists!"
        
        del self.products[product_name]
        self.db_manager.update_products(self.products)
        return "deleted"

    def update_product_quantity(self, product_name, new_amount):
        old_amount = self.products[product_name]["Quantity"]
        new_amount = old_amount + new_amount
        self.products[product_name]["Quantity"] = new_amount
        self.db_manager.update_products(self.products)
        return
    
