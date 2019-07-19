from django.shortcuts import render, get_object_or_404
from .models import Product, ProductCategory


def main(request):
    return render(request, 'mainapp/index.html')


def products(request, pk=None):
    title = 'Interior product'
    categories = ProductCategory.objects.all()
    products = Product.objects.all()

    if pk:
        category = get_object_or_404(ProductCategory, pk=pk)
        products = products.filter(category=category)

    content = {
        'title': title,
        'categories': categories,
        'products': products,
    }
    return render(request, 'mainapp/products.html', context=content)


def contacts(request):
    return render(request, 'mainapp/contact.html')