from django.shortcuts import render

# Create your views here.


def main(request):
    return render(request, 'mainapp/index.html')


def products(request):
    links_menu = [
        {'href': 'products', 'name': 'all'},
        {'href': 'products', 'name': 'home'},
        {'href': 'products', 'name': 'office'},
        {'href': 'products', 'name': 'furniture'},
        {'href': 'products', 'name': 'modern'},
        {'href': 'products', 'name': 'classic'},
    ]
    return render(request, 'mainapp/products.html', context={'links_arr': links_menu})


def contacts(request):
    return render(request, 'mainapp/contact.html')