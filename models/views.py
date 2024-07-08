from django.contrib import messages

# Login
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import redirect, render

# Create Base View
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    ListView,
    TemplateView,
    UpdateView,
)

from .forms import AboutForm, ProductForm, RegisterForm, TestimonialForm
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
    products = Product.objects.all()
    about = About.objects.all()
    testimonial = Testimonial.objects.all()

    return render(
        request,
        "services.html",
        {
            "products": products,
            "abouts": about,
            "testimonials": testimonial,
        },
    )


def forms(request, type, action, id):
    if request.method == "POST" and request.POST.get("type") == "Product":
        if request.POST.get("action") == "update":
            product = Product.objects.get(id=id)
            form = ProductForm(request.POST)
            if form.is_valid():
                product.name = form.cleaned_data.get("name")
                product.price = form.cleaned_data.get("price")
                product.stock = form.cleaned_data.get("stock")
                product.category = form.cleaned_data.get("category")
                product.image_url = form.cleaned_data.get("image_url")
                product.save()
                messages.add_message(
                    request=request,
                    level=messages.SUCCESS,
                    message="Product updated successfully",
                )
                context = {"products": Product.objects.all()}
                return render(request, "shop.html", context)
        else:
            form = ProductForm(request.POST)
            if form.is_valid():
                name = form.cleaned_data.get("name")
                price = form.cleaned_data.get("price")
                stock = form.cleaned_data.get("stock")
                category = form.cleaned_data.get("category")
                image = form.cleaned_data.get("image_url")

                newProduct = Product(
                    name=name,
                    price=price,
                    stock=stock,
                    category=category,
                    image_url=image,
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
        if request.POST.get("action") == "update":
            about = About.objects.get(id=id)
            form = AboutForm(request.POST)
            if form.is_valid():
                about.first_name = form.cleaned_data.get("first_name")
                about.last_name = form.cleaned_data.get("last_name")
                about.position = form.cleaned_data.get("position")
                about.description = form.cleaned_data.get("description")
                about.image_url = form.cleaned_data.get("image_url")

                about.save()
                messages.add_message(
                    request=request,
                    level=messages.SUCCESS,
                    message="Personal update successfully",
                )
                team = About.objects.all()
                testimonial = Testimonial.objects.all()
                context = {"teams": team, "testimonials": testimonial}
                return render(request, "about.html", context)
        else:
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
        if request.POST.get("action") == "update":
            testimonial = Testimonial.objects.get(id=id)
            form = TestimonialForm(request.POST)
            if form.is_valid():
                testimonial.first_name = form.cleaned_data.get("first_name")
                testimonial.last_name = form.cleaned_data.get("last_name")
                testimonial.position = form.cleaned_data.get("position")
                testimonial.testimonial = form.cleaned_data.get("testimonial")
                testimonial.image_url = form.cleaned_data.get("image_url")

                testimonial.save()
                messages.add_message(
                    request=request,
                    level=messages.SUCCESS,
                    message="Testimonial update successfully",
                )
                team = About.objects.all()
                testimonial = Testimonial.objects.all()
                context = {"teams": team, "testimonials": testimonial}
                return render(request, "about.html", context)
        else:
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
        context = {}
        if type == "product":
            if action == "update":
                product = Product.objects.get(id=id)
                context = {
                    "formProduct": ProductForm(
                        initial={
                            "name": product.name,
                            "price": product.price,
                            "stock": product.stock,
                            "category": product.category,
                            "image_url": product.image_url,
                        }
                    ),
                    "action": "update",
                }
            else:
                context = {"formProduct": ProductForm()}

        if type == "about":
            if action == "update":
                about = About.objects.get(id=id)
                context = {
                    "formAbout": AboutForm(
                        initial={
                            "first_name": about.first_name,
                            "last_name": about.last_name,
                            "position": about.position,
                            "description": about.description,
                            "image_url": about.image_url,
                        }
                    ),
                    "action": "update",
                }
                print(context)
            else:
                context = {"formAbout": AboutForm()}

        if type == "testimonial":
            if action == "update":
                testimonial = Testimonial.objects.get(id=id)
                context = {
                    "formTestimonial": TestimonialForm(
                        initial={
                            "first_name": testimonial.first_name,
                            "last_name": testimonial.last_name,
                            "position": testimonial.position,
                            "testimonial": testimonial.testimonial,
                            "image_url": testimonial.image_url,
                        }
                    ),
                    "action": "update",
                }
            else:
                context = {"formTestimonial": TestimonialForm()}

        return render(
            request,
            "forms.html",
            context,
        )


@login_required
def delete(request, type, id):

    if request.method == "POST" and type == "product":
        product = Product.objects.get(id=id)
        product.delete()

        messages.add_message(
            request=request,
            level=messages.SUCCESS,
            message="Product delete successfully",
        )

        products = Product.objects.all()
        about = About.objects.all()
        testimonial = Testimonial.objects.all()

        return render(
            request,
            "services.html",
            {
                "products": products,
                "abouts": about,
                "testimonials": testimonial,
            },
        )

    elif request.method == "POST" and type == "about":
        about = About.objects.get(id=id)
        about.delete()

        messages.add_message(
            request=request,
            level=messages.SUCCESS,
            message="About delete successfully",
        )

        products = Product.objects.all()
        about = About.objects.all()
        testimonial = Testimonial.objects.all()

        return render(
            request,
            "services.html",
            {
                "products": products,
                "abouts": about,
                "testimonials": testimonial,
            },
        )

    elif request.method == "POST" and type == "testimonial":
        testimonial = Testimonial.objects.get(id=id)
        testimonial.delete()

        messages.add_message(
            request=request,
            level=messages.SUCCESS,
            message="Testimonial delete successfully",
        )

        products = Product.objects.all()
        about = About.objects.all()
        testimonial = Testimonial.objects.all()

        return render(
            request,
            "services.html",
            {
                "products": products,
                "abouts": about,
                "testimonials": testimonial,
            },
        )
    else:
        if type == "product":
            product = Product.objects.get(id=id)
            return render(
                request,
                "delete.html",
                {"data": product, "product": type},
            )
        if type == "about":
            about = About.objects.get(id=id)
            return render(
                request,
                "delete.html",
                {"data": about, "about": type},
            )
        if type == "testimonial":
            testimonial = Testimonial.objects.get(id=id)
            return render(
                request,
                "delete.html",
                {"data": testimonial, "testimonial": type},
            )


class Services(TemplateView):
    template_name = "services.html"

    def get_context_data(self, **kwargs):
        context = super(Services, self).get_context_data(**kwargs)
        context["products"] = Product.objects.all()
        context["abouts"] = About.objects.all()
        context["testimonials"] = Testimonial.objects.all()
        return context


# PRODUCTS

class CustomLoginRequiredMixin(LoginRequiredMixin):
    def dispatch(self, request, *args, **kwargs):
        user = request.user
        if not user.is_authenticated:
                messages.warning(request, 'You must be logged in to view this page')
                return self.handle_no_permission()
        return super(CustomLoginRequiredMixin, self).dispatch(
            request, *args, **kwargs
        )


class Products(CustomLoginRequiredMixin, ListView):
    model = Product
    template_name = "products.html"
    permission_denied_message = 'You are not authorized to view this page'



class ProductCreate(CustomLoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = "forms.html"
    success_url = reverse_lazy("products")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["product"] = "create"
        return context

    def form_valid(self, form):
        messages.success(self.request, "Product created successfully")
        return super().form_valid(form)


class ProductUpdate(CustomLoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = "forms.html"
    success_url = reverse_lazy("products")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["product"] = "update"
        return context

    def form_valid(self, form):
        messages.success(self.request, "Product updated successfully")
        return super().form_valid(form)


class ProductDelete(CustomLoginRequiredMixin, DeleteView):
    model = Product
    template_name = "delete.html"
    success_url = reverse_lazy("products")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["product"] = "delete"
        return context

    def form_valid(self, form):
        messages.success(self.request, "Product deleted successfully")
        return super().form_valid(form)


# ABOUT


class Abouts(CustomLoginRequiredMixin, ListView):
    model = About
    template_name = "abouts.html"


class AboutCreate(CustomLoginRequiredMixin, CreateView):
    model = About
    form_class = AboutForm
    template_name = "forms.html"
    success_url = reverse_lazy("abouts")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["about"] = "create"
        return context

    def form_valid(self, form):
        messages.success(self.request, "About created successfully")
        return super().form_valid(form)


class AboutUpdate(CustomLoginRequiredMixin, UpdateView):
    model = About
    form_class = AboutForm
    template_name = "forms.html"
    success_url = reverse_lazy("abouts")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["about"] = "update"
        return context

    def form_valid(self, form):
        messages.success(self.request, "About updated successfully")
        return super().form_valid(form)


class AboutDelete(CustomLoginRequiredMixin, DeleteView):
    model = About
    template_name = "delete.html"
    success_url = reverse_lazy("abouts")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["about"] = "delete"
        return context

    def form_valid(self, form):
        messages.success(self.request, "About deleted successfully")
        return super().form_valid(form)


# TESTIMONIAL


class Testimonials(CustomLoginRequiredMixin, ListView):
    model = Testimonial
    template_name = "testimonials.html"


class TestimonialCreate(CustomLoginRequiredMixin, CreateView):
    model = Testimonial
    form_class = TestimonialForm
    template_name = "forms.html"
    success_url = reverse_lazy("testimonials")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["testimonial"] = "create"
        return context

    def form_valid(self, form):
        messages.success(self.request, "Testimonial created successfully")
        return super().form_valid(form)


class TestimonialUpdate(CustomLoginRequiredMixin, UpdateView):
    model = Testimonial
    form_class = TestimonialForm
    template_name = "forms.html"
    success_url = reverse_lazy("testimonials")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["testimonial"] = "update"
        return context

    def form_valid(self, form):
        messages.success(self.request, "Testimonial updated successfully")
        return super().form_valid(form)


class TestimonialDelete(CustomLoginRequiredMixin, DeleteView):
    model = Testimonial
    template_name = "delete.html"
    success_url = reverse_lazy("testimonials")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["testimonial"] = "delete"
        return context

    def form_valid(self, form):
        messages.success(self.request, "Testimonial deleted successfully")
        return super().form_valid(form)


# LOGIN AND LOGOUT


def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request, "index.html")
        else:
            messages.warning(request, "Invalid Credentials")
            return redirect(reverse_lazy("login"))
    else:
        form = AuthenticationForm()
        form.fields["username"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Enter username"}
        )
        form.fields["password"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Enter password"}
        )
    return render(request, "login.html", {"form": form})


def logout_view(request):
    logout(request)
    return redirect(reverse_lazy("login"))


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if request.POST.get("username") in User.objects.values_list(
            "username", flat=True
        ):
            messages.warning(request, "Username already exists")
            return redirect(reverse_lazy("register"))
        if request.POST.get("password1") != request.POST.get("password2"):
            print("aqui")
            messages.warning(request, "Passwords do not match")
            return redirect(reverse_lazy("register"))
        if form.is_valid():
            user = form.cleaned_data.get("username")
            form.save()
            messages.success(request, f"Account created for {user}")
            return redirect(reverse_lazy("login"))
    else:
        form = RegisterForm()
    return render(request, "register.html", {"form": form})


# ERORR PAGES

class Error404(TemplateView):
    template_name = "404.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Page Not Found"
        return context

def blog(request):
    return render(request, "blog.html")


def contact(request):
    return render(request, "contact.html")


@login_required
def cart(request):
    return render(request, "cart.html")


@login_required
def checkout(request):
    return render(request, "checkout.html")
