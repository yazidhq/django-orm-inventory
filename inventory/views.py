from django.shortcuts import render
from .models import Product, Inventory, StockControl
from django.core.paginator import Paginator

def all_products(request):
    objs = Product.objects.all()
    paginator = Paginator(objs, 8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'grid-output.html', {'page_obj':page_obj})


def view(request, slug):
    single_product = Product.objects.get(slug=slug)
    inventory_product = Inventory.objects.get(product__slug=slug)
    stock_product = StockControl.objects.get(inventory__product__slug=slug)
    data = {
        'product':single_product, 
        'inventory':inventory_product,
        'stock':stock_product,
    }
    return render(request, 'view-single.html', data)


def edit(request, slug):
    return render(request, 'edit-item.html')
