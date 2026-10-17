from Backend.ProductManagement import ProductManagement
from Backend.TransactionManagement import TransactionManagement

product_manager = ProductManagement()
tr_manager = TransactionManagement()

msg = tr_manager.add_transaction("Herbal Shampoo", 2, 'In', "19-10-2026")
# msg = product_manager.addProducts("Herbal Shampoo", 700, "Loreal")

print(msg)

