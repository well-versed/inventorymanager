from django.urls import path
from . import views

urlpatterns = [
    # Home
    path("", views.home, name="home"),

    # Products
    path("products/", views.product_list, name="product_list"),
    path("products/add/", views.add_product, name="add_product"),

    # Customers
    path("customers/", views.customer_list, name="customer_list"),
    path("customers/add/", views.add_customer, name="add_customer"),

    # Suppliers
    path("suppliers/", views.supplier_list, name="supplier_list"),
    path("suppliers/add/", views.add_supplier, name="add_supplier"),

    # Sales
    path("sales/start/", views.start_sale, name="start_sale"),
]
