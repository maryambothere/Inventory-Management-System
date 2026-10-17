from Backend.ProductManagement import ProductManagement

product_manager = ProductManagement()

msg = product_manager.deleteProducts("abc")
print(msg)

