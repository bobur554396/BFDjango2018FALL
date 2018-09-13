from django.shortcuts import render


def index(request):
    name = "test name"
    is_weekend = False
    products = [{'id': i, 'name': 'Product #{}'.format(i)} for i in range(10)]
    context = {
        'name': name,
        'is_weekend': is_weekend,
        'product': {
            'id': 123,
            'name': 'Product name',
        },
        'products': products
    }
    return render(request, 'index.html', context)


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')
