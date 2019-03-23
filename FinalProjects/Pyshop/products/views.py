from django.http import HttpResponse
from django.shortcuts import render
from .models import Product

# /product --> index
# (URL) uniform resource locator (Address)


def index(request):
    products = Product.objects.all()
    return render(request,'index.html',{'products':products})
    #return HttpResponse('Hello World')


def newproduct(requests):
    return HttpResponse('New Products')







