from django.shortcuts import render, redirect
from .models import Product, Inventory, StockControl
from django.core.paginator import Paginator
from django.contrib import messages
from .forms import EditProduct

def all_products(request):
    objs = Product.objects.all()
    paginator = Paginator(objs, 8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'grid-output.html', {'page_obj':page_obj})


def view(request, slug):
    data = {
        'product':Product.objects.get(slug=slug), 
        'inventory':Inventory.objects.get(product__slug=slug),
        'stock':StockControl.objects.get(inventory__product__slug=slug),
    }
    return render(request, 'view-single.html', data)


def edit(request, slug):
    current_record = Product.objects.get(slug=slug)
    if request.method == 'POST':
        form = EditProduct(request.POST, instance=current_record)
        if form.is_valid():
            form.save()
            messages.success(request, "Product Successfully Updated...")
            return redirect('all_products')
        else:
            messages.error(request, "Product Unsuccessfully Updated...")
            return redirect('all_products')
    else:
        form = EditProduct(instance=current_record)
    data = {
        'form': form,
        'product': current_record,
    }
    return render(request, 'edit-item.html', data)