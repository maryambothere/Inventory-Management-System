from Backend.ProductManagement import ProductManagement
from Database.DatabaseManagement import DatabaseManagement
import streamlit as st

product_manager = ProductManagement()

db_manager = DatabaseManagement()
all_products = db_manager.fetch_data()


st.title("Inventory Management System")
st.write("")

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("Dashboard", width=170):
        st.session_state.dashboard = True
        st.session_state.excel_sheet = False

with col2:
    if st.button("Products Management", width=170):
        st.session_state.dashboard = False
        st.session_state.excel_sheet = True
        st.session_state.search = ""

with col3:
    if st.button("Stock History", width=170):
        st.session_state.dashboard = False
        st.session_state.excel_sheet = False


# Dashboard Panel
if st.session_state.get("dashboard", False):
    st.write('I am dashboard')


# Products Panel
if st.session_state.get("excel_sheet", False):
    search = st.text_input("Search products", placeholder="Enter product name...")

    # Filter products based on search
    filtered_products = {
        name: details
        for name, details in all_products.items()
        if search.lower() in name.lower()
    }

    # Table Header
    header = st.columns([3, 2, 2, 1])
    header[0].write("**Product**")
    header[1].write("**Price**")
    header[2].write("**Quantity**")
    header[3].write("**Action**")

    # Product rows (filtered by search)
    for product_name, details in filtered_products.items():
        col = st.columns([3, 2, 2, 1])

        col[0].write(product_name)
        col[1].write(details["price"])
        col[2].write(details["Quantity"])

        if col[3].button("Delete", key=f"delete_{product_name}"):
            product_manager.deleteProduct(product_name)
            st.rerun()


# # OLD CODE
# col1, col2, col3 = st.columns(3)

# with col1:
#     if st.button("Add Item", width=130):
#         st.session_state.show_add_form = True
#         st.session_state.show_del_form = False
#         st.session_state.view_all = False

# with col2:
#     if st.button("View Items", width=130):
#         st.session_state.show_add_form = False
#         st.session_state.show_del_form = False
#         st.session_state.view_all = True
    

# with col3:
#     if st.button("Delete Item", width=130):
#         st.session_state.show_del_form = True
#         st.session_state.show_add_form = False
#         st.session_state.view_all = False


# if st.session_state.get("show_add_form", False):
#     st.subheader("Add New Product")

#     product_name = st.text_input("Product Name")
#     price = st.number_input("Price", min_value=0.0)
#     quantity = st.number_input("Quantity", min_value=0, step=1)

#     if st.button("Save Product"):
#         all_pr = product_manager.addProducts(product_name, price, quantity)
#         st.write(all_pr)

# if st.session_state.get("show_del_form", False):
#     st.subheader("Remove Product")
#     product_name = st.text_input("Product Name")

#     if st.button("Save Changes"):
#         all_pr = product_manager.deleteProducts(product_name)
#         st.write(all_pr)

# if st.session_state.get("view_all", False):
#     st.subheader("Your Products")

#     all_pr = product_manager.viewProducts()
#     st.write(all_pr)
