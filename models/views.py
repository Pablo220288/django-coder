from django.shortcuts import render

from .models import Product

# Create your views here.


def index(request):
    context = {"products": Product.objects.all()}
    return render(request, "index.html", context)


def shop(request):
    return render(request, "shop.html")


def about(request):
    return render(request, "about.html")


def service(request):
    return render(request, "services.html")


def blog(request):
    return render(request, "blog.html")


def contact(request):
    return render(request, "contact.html")


def cart(request):
    return render(request, "cart.html")


def checkout(request):
    return render(request, "checkout.html")
