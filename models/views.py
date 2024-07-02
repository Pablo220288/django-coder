from django.contrib import messages
from django.shortcuts import render

from .forms import AboutForm, ProductForm, TestimonialForm
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
    if request.method == "POST" and request.POST.get("type") == "Product":
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
    elif request.method == "POST" and request.POST.get("type") == "About":
        form = AboutForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data.get("first_name")
            last_name = form.cleaned_data.get("last_name")
            position = form.cleaned_data.get("position")
            description = form.cleaned_data.get("description")
            image = form.cleaned_data.get("image_url")

            newAbout = About(
                first_name=first_name,
                last_name=last_name,
                position=position,
                description=description,
                image_url=image,
            )
            newAbout.save()
            messages.add_message(
                request=request,
                level=messages.SUCCESS,
                message="Personal added successfully",
            )
            team = About.objects.all()
            testimonial = Testimonial.objects.all()
            context = {"teams": team, "testimonials": testimonial}
            return render(request, "about.html", context)
    elif request.method == "POST" and request.POST.get("type") == "Testimonial":
        form = TestimonialForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data.get("first_name")
            last_name = form.cleaned_data.get("last_name")
            position = form.cleaned_data.get("position")
            testimonial = form.cleaned_data.get("testimonial")
            image = form.cleaned_data.get("image_url")

            newTestimonial = Testimonial(
                first_name=first_name,
                last_name=last_name,
                position=position,
                testimonial=testimonial,
                image_url=image,
            )
            newTestimonial.save()
            messages.add_message(
                request=request,
                level=messages.SUCCESS,
                message="Testimonial added successfully",
            )
            team = About.objects.all()
            testimonial = Testimonial.objects.all()
            context = {"teams": team, "testimonials": testimonial}
            return render(request, "about.html", context)
    else:
        formProduct = ProductForm()
        formAbout = AboutForm()
        formTestimonial = TestimonialForm()

    return render(
        request,
        "services.html",
        {
            "formProduct": formProduct,
            "formAbout": formAbout,
            "formTestimonial": formTestimonial,
        },
    )


def blog(request):
    return render(request, "blog.html")


def contact(request):
    return render(request, "contact.html")


def cart(request):
    return render(request, "cart.html")


def checkout(request):
    return render(request, "checkout.html")
