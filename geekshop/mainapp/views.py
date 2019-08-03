from django.shortcuts import render, get_object_or_404
from .models import Product, ProductCategory
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def main(request):
    title = 'Interior product'

    basket = []
    if request.user.is_authenticated:
        basket = request.user.basket.all()

    content = {
        'title': title,
        'basket': basket,
    }
    return render(request, 'mainapp/index.html', context=content)


def products(request, pk=None, page=1):
    title = 'Interior product'
    categories = ProductCategory.objects.all()
    products = Product.objects.all()

    basket = []
    if request.user.is_authenticated:
       basket = request.user.basket.all()

    if pk or pk == 0:
        if pk !=0:
            category = get_object_or_404(ProductCategory, pk=pk)
            products = products.filter(category=category)

        paginator = Paginator(products, 2)
        try:
            products_paginator = paginator.page(page)
        except PageNotAnInteger:
            products_paginator = paginator.page(1)
        except EmptyPage:
            products_paginator = paginator.page(paginator.num_pages)

        content = {
            'title': title,
            'categories': categories,
            'products': products_paginator,
            'basket': basket,
        }
        return render(request, 'mainapp/products.html', context=content)
    else:
        hot_products = products.filter(is_hot=True)

        paginator = Paginator(hot_products, 2)
        try:
            products_paginator = paginator.page(page)
        except PageNotAnInteger:
            products_paginator = paginator.page(1)
        except EmptyPage:
            products_paginator = paginator.page(paginator.num_pages)

        content = {
            'title': title,
            'hot_products': products_paginator,
            'categories': categories,
            'basket': basket,
        }
        return render(request, 'mainapp/hot_products.html', content)


def product_detail(request, pk=None):
    title = 'Interior product'
    categories = ProductCategory.objects.all()
    products = Product.objects.all()

    basket = []
    if request.user.is_authenticated:
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