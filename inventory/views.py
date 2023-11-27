from django.shortcuts import render, redirect
from .models import Product, Inventory, StockControl, Category
from django.core.paginator import Paginator
from django.contrib import messages
from .forms import FormProduct, FormCategory


# category
def category(request):
    cats = Category.objects.all().order_by('-id')
    return render(request, 'category/categories.html', {'categories':cats})


def add_category(request):
    if request.method == 'POST':
        form = FormCategory(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Category Successfully Added...")
            return redirect('category')
        else:
            messages.error(request, "Category Unsuccessfully Added...")
            return redirect('category')
    else:
        form = FormCategory()
    return render(request, 'category/add-category.html', {'form':form})
# category


# Product
def products(request):
    objs = Product.objects.all().order_by('-id')
    paginator = Paginator(objs, 8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'grid-output.html', {'page_obj':page_obj})


def view(request, slug):
    try:
        data = {
            'product':Product.objects.get(slug=slug), 
            'inventory':Inventory.objects.get(product__slug=slug),
            'stock':StockControl.objects.get(inventory__product__slug=slug),
        }
    except:
        data = {
            'error':'Inventory for this product has not been created yet.'
        }
    return render(request, 'view-single.html', data)


def edit(request, slug):
    current_record = Product.objects.get(slug=slug)
    if request.method == 'POST':
        form = FormProduct(request.POST, instance=current_record)
        if form.is_valid():
            form.save()
            messages.success(request, "Product Successfully Updated...")
            return redirect('products')
        else:
            messages.error(request, "Product Unsuccessfully Updated...")
            return redirect('products')
    else:
        form = FormProduct(instance=current_record)
    data = {
        'form': form,
        'product': current_record,
    }
    return render(request, 'edit-item.html', data)


def delete(request, slug):
    Product.objects.get(slug=slug).delete()
    messages.success(request, "Product Deleted Succesfully..")
    return redirect('products')


def add(request):
    if request.method == 'POST':
        form = FormProduct(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Product Successfully Added...")
            return redirect('products')
        else:
            messages.error(request, "Product Unsuccessfully Addedd...")
            return redirect('products')
    else:
        form = FormProduct()
    data = {
        'form': form,
    }
    return render(request, 'add-item.html', data)
# Product