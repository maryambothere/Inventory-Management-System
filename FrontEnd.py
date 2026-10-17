from Backend.ProductManagement import ProductManagement
import streamlit as st

product_manager = ProductManagement()

st.title("Inventory Management System")


col1, col2, col3 = st.columns(3)

with col1:
    if st.button("Add Item", width=130):
        st.session_state.show_add_form = True
        st.session_state.show_del_form = False
        st.session_state.view_all = False

with col2:
    if st.button("View Items", width=130):
        st.session_state.show_add_form = False
        st.session_state.show_del_form = False
        st.session_state.view_all = True
    

with col3:
    if st.button("Delete Item", width=130):
        st.session_state.show_del_form = True
        st.session_state.show_add_form = False
        st.session_state.view_all = False


if st.session_state.get("show_add_form", False):
    st.subheader("Add New Product")

    product_name = st.text_input("Product Name")
    price = st.number_input("Price", min_value=0.0)
    quantity = st.number_input("Quantity", min_value=0, step=1)

    if st.button("Save Product"):
        all_pr = product_manager.addProducts(product_name, price, quantity)
        st.write(all_pr)

if st.session_state.get("show_del_form", False):
    st.subheader("Remove Product")
    product_name = st.text_input("Product Name")

    if st.button("Save Changes"):
        all_pr = product_manager.deleteProducts(product_name)
        st.write(all_pr)

if st.session_state.get("view_all", False):
    st.subheader("Your Products")

    all_pr = product_manager.viewProducts()
    st.write(all_pr)
