from pathlib import Path
import json

class ProductManagement:

    def __init__(self):
        self.products = {}

        self.file_path = Path("Database/products.json")
        self.file_path.parent.mkdir(parents=True, exist_ok=True)

        if self.file_path.exists():
            with open(self.file_path, "r") as file:
                self.products = json.load(file)
        else:
            with open(self.file_path, "w") as file:
                json.dump(self.products, file, indent=4)


    def addProducts(self, product_name, product_price, product_qtt):
        if product_name in self.products:
            return "Product already exists!"
        
        self.products[product_name] = {"price": product_price, "Quantity": product_qtt}

        with open(self.file_path, "w") as file:
            json.dump(self.products, file, indent=4)

        return "Added"

    def deleteProducts(self, product_name):
        if product_name not in self.products:
            return "Product does'nt exists!"
        
        del self.products[product_name]

        with open(self.file_path, "w") as file:
            json.dump(self.products, file, indent=4)

        return "deleted"
    
    def viewProducts(self):      
        return self.products