# Progress and Summary

#### Product Management



**Add Products:**

Checks if the product to be added already exists or not

Adds in temporary dict

calls update\_products from db manager to save it



**Delete Products:**

Checks if the product to be deleted exists or not

deletes in temporary dict

calls update\_products from db manager to save it



**Update Quantity:**

Performs addition in old and new quantity

Updates in temporary dict

calls update\_products from db manager to save it

**Future: Check if addition makes sense(cant be below 0)**





#### Transaction Management



**Add Transaction**

Checks if product exists or not

Generates dictionary id

Adds transaction data to dictionary

Calls Update Quantity from product management

Calls update\_products from db manager to save it





#### Database Management



**Constructor:**

Checks and creates products.json and transactions.json if not exists

Loads data into a dict



**Fetch Product Data, Fetch Transaction Data:**

returns their respective data



**Update Products, Update Transaction Data**

Takes data dict as parameter and write to their respective files=4)



