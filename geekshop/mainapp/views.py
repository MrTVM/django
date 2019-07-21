from django.shortcuts import render, get_object_or_404
from .models import Product, ProductCategory


def main(request):
    title = 'Interior product'
    basket = []
    if request.user:
        basket = request.user.basket.all()

    content = {
        'title': title,
        'basket': basket,
    }
    return render(request, 'mainapp/index.html', context=content)


def products(request, pk=None):
    title = 'Interior product'
    categories = ProductCategory.objects.all()
    products = Product.objects.all()

    basket = []
    if request.user:
        basket = request.user.basket.all()

    if pk:
        category = get_object_or_404(ProductCategory, pk=pk)
        products = products.filter(category=category)

    content = {
        'title': title,
        'categories': categories,
        'products': products,
        'basket': basket,
    }
    return render(request, 'mainapp/products.html', context=content)


def product_detail(request, pk=None):
    title = 'Interior product'
    categories = ProductCategory.objects.all()
    products = Product.objects.all()

    basket = []
    if request.user:
        basket = request.user.basket.all()

    if pk:
        product = get_object_or_404(ProductCategory, pk=pk)
        product = products.filter(pk=product.pk).first()

    content = {
        'title': title,
        'categories': categories,
        'product': product,
        'basket': basket,
    }
    return render(request, 'mainapp/product_detail.html', context=content)


def contacts(request):
    return render(request, 'mainapp/contact.html')