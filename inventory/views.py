from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Product, Customer, Supplier, Sale
from .forms import ProductForm, CustomerForm, SupplierForm, SaleForm, SaleItemFormSet

# --- Home ---
def home(request):
    return render(request, "inventory/home.html")

# --- Product Views ---
def product_list(request):
    products = Product.objects.all()
    return render(request, "inventory/product_list.html", {"products": products})

def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'inventory/add_product.html', {'form': form})

# --- Customer Views ---
def customer_list(request):
    customers = Customer.objects.all()
    return render(request, "inventory/customer_list.html", {"customers": customers})

def add_customer(request):
    if request.method == "POST":
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('customer_list')
    else:
        form = CustomerForm()
    return render(request, 'inventory/add_customer.html', {'form': form})

# --- Supplier Views ---
def supplier_list(request):
    suppliers = Supplier.objects.all()
    return render(request, 'inventory/suppliers.html', {'suppliers': suppliers})

def add_supplier(request):
    if request.method == 'POST':
        form = SupplierForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('supplier_list')
    else:
        form = SupplierForm()
    return render(request, 'inventory/add_supplier.html', {'form': form})

# --- Sales Views ---
def start_sale(request):
    sale = None
    total = 0

    if request.method == "POST":
        sale_form = SaleForm(request.POST)
        formset = SaleItemFormSet(request.POST)

        if sale_form.is_valid() and formset.is_valid():
            sale = sale_form.save()
            items = formset.save(commit=False)

            for item in items:
                item.sale = sale
                # reduce stock
                item.product.stock -= item.quantity
                item.product.save()
                item.save()

            total = sale.total_amount()
            return render(request, "inventory/start_sale.html", {
                "sale_form": sale_form,
                "formset": SaleItemFormSet(instance=sale),
                "sale": sale,
                "total": total,
            })
    else:
        sale_form = SaleForm()
        formset = SaleItemFormSet()

    return render(request, "inventory/start_sale.html", {
        "sale_form": sale_form,
        "formset": formset,
        "sale": sale,
        "total": total,
    })
