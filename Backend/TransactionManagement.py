from Database.DatabaseManagement import DatabaseManagement
from Backend.ProductManagement import ProductManagement

class TransactionManagement:

   def __init__(self):
      self.db_manager = DatabaseManagement()
      self.pr_manager = ProductManagement()


   def add_transaction(self, product_name, quantity, transaction_type, date):
      
      product_data = self.db_manager.fetch_product_data()
      
      if product_name not in product_data:
        return "Product does not exist"

      transaction_data = self.db_manager.fetch_transaction_data()

      if transaction_data:
         new_id = max(int(key) for key in transaction_data.keys()) + 1
      else:
         new_id = 1 

      transaction_data[new_id] = {"product_name": product_name, "quantity": quantity, "transaction_type": transaction_type, "date": date}
      if transaction_type == 'Out':
         self.pr_manager.update_product_quantity(product_name, -quantity)
      else:
         self.pr_manager.update_product_quantity(product_name, quantity)
         
      self.db_manager.update_transactions(transaction_data)
      
      return "Success"
