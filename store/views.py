from django.shortcuts import render, get_object_or_404
from .models import Product

# Create your views here.


def index(request):
    products = Product.objects.order_by('name')
    context = {'products': products}
    return render(request, 'store/index.html', context)


def detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    context = {'product': product}
    return render(request, 'store/detail.html', context)
