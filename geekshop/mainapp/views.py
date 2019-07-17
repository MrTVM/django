from django.shortcuts import render
from .models import Product, ProductCategory


def main(request):
    return render(request, 'mainapp/index.html')


def products(request):
    title = 'Interior product'
    categories = ProductCategory.objects.all()
    products = Product.objects.all()
    content = {
        'title': title,
        'categories': categories,
        'products': products,
    }
    return render(request, 'mainapp/products.html', context=content)


def contacts(request):
    return render(request, 'mainapp/contact.html')