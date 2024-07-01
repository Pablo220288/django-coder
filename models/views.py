from django.contrib import messages
from django.shortcuts import render

from .forms import ProductForm
from .models import About, Product, Testimonial

# Create your views here.


def index(request):
    products = Product.objects.all()[:3]
    testimonial = Testimonial.objects.all()
    context = {"products": products, "testimonials": testimonial}
    return render(request, "index.html", context)


def shop(request):
    search = request.GET.get("search")
    if search:
        context = {"products": Product.objects.filter(name__contains=search)}
    else:
        context = {"products": Product.objects.all()}
    return render(request, "shop.html", context)


def about(request):
    team = About.objects.all()
    testimonial = Testimonial.objects.all()
    context = {"teams": team, "testimonials": testimonial}
    return render(request, "about.html", context)


def service(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get("name")
            price = form.cleaned_data.get("price")
            stock = form.cleaned_data.get("stock")
            category = form.cleaned_data.get("category")
            image = form.cleaned_data.get("image_url")

            newProduct = Product(
                name=name, price=price, stock=stock, category=category, image_url=image
            )
            newProduct.save()
            messages.add_message(
                request=request,
                level=messages.SUCCESS,
                message="Product added successfully",
            )
            context = {"products": Product.objects.all()}
            return render(request, "shop.html", context)
    else:
        form = ProductForm()

    return render(request, "services.html", {"form": form})


def blog(request):
    return render(request, "blog.html")


def contact(request):
    return render(request, "contact.html")


def cart(request):
    return render(request, "cart.html")


def checkout(request):
    return render(request, "checkout.html")
