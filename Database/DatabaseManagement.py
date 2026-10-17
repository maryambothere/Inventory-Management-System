import json
from pathlib import Path

class DatabaseManagement:

    def __init__(self):
        self.product_data = {}
        self.transactions_data = {}
    
        self.product_file_path = Path("Database/products.json")
        self.transactions_file_path = Path("Database/transactions.json")
        self.product_file_path.parent.mkdir(parents=True, exist_ok=True)
    
        if self.product_file_path.exists():
            with open(self.product_file_path, "r") as file:
                self.product_data = json.load(file)
        else:
            with open(self.product_file_path, "w") as file:
                json.dump(self.product_data, file, indent=4) 

        
        if self.transactions_file_path.exists():
            with open(self.transactions_file_path, "r") as file:
                self.transactions_data = json.load(file)
        else:
            with open(self.transactions_file_path, "w") as file:
                json.dump(self.transactions_data, file, indent=4)


    def fetch_product_data(self):
        return self.product_data

    def fetch_transaction_data(self):
        return self.transactions_data

    def update_products(self, data):
        with open(self.product_file_path, "w") as file:
            json.dump(data, file, indent=4)

    def update_transactions(self, data):
        with open(self.transactions_file_path, "w") as file:
            json.dump(data, file, indent=4)