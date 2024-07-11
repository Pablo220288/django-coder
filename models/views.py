from django.contrib import messages

# Login
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import PasswordChangeView
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

from .forms import (
    AboutForm,
    AvatarForm,
    MyPasswordChangeForm,
    ProductForm,
    ProfileForm,
    RegisterForm,
    ServiceForm,
    TestimonialForm,
)
from .models import About, Avatar, Product, Service, Testimonial

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


# CUSTOM MIDDLEWARE


class CustomLoginRequiredMixin(LoginRequiredMixin):
    def dispatch(self, request, *args, **kwargs):
        user = request.user
        if not user.is_authenticated:
            messages.warning(request, "You must be logged in to view this page")
            return self.handle_no_permission()
        return super(CustomLoginRequiredMixin, self).dispatch(request, *args, **kwargs)


# PRODUCTS


class Products(CustomLoginRequiredMixin, ListView):
    model = Product
    template_name = "products.html"
    permission_denied_message = "You are not authorized to view this page"


class ProductCreate(CustomLoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = "forms.html"
    success_url = reverse_lazy("products")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["product"] = "Add"
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
        context["product"] = "Update"
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
        context["product"] = "Delete"
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
        context["about"] = "Add"
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
        context["about"] = "Update"
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
        context["about"] = "Delete"
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
        context["testimonial"] = "Add"
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
        context["testimonial"] = "Update"
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
        context["testimonial"] = "Delete"
        return context

    def form_valid(self, form):
        messages.success(self.request, "Testimonial deleted successfully")
        return super().form_valid(form)


# SERVICES


class Services(CustomLoginRequiredMixin, ListView):
    model = Service
    template_name = "services.html"


class ServiceCreate(CustomLoginRequiredMixin, CreateView):
    model = Service
    form_class = ServiceForm
    template_name = "forms.html"
    success_url = reverse_lazy("services")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["service"] = "Add"
        return context

    def form_valid(self, form):
        messages.success(self.request, "Service created successfully")
        return super().form_valid(form)


class ServiceUpdate(CustomLoginRequiredMixin, UpdateView):
    model = Service
    form_class = ServiceForm
    template_name = "forms.html"
    success_url = reverse_lazy("services")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["service"] = "Update"
        return context

    def form_valid(self, form):
        messages.success(self.request, "Service updated successfully")
        return super().form_valid(form)


class ServiceDelete(CustomLoginRequiredMixin, DeleteView):
    model = Service
    template_name = "delete.html"
    success_url = reverse_lazy("services")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["service"] = "Delete"
        return context

    def form_valid(self, form):
        messages.success(self.request, "Service deleted successfully")
        return super().form_valid(form)


# LOGIN AND LOGOUT


def login_view(request):
    if "next" in request.GET:
        messages.warning(request, "You must be logged in to access this page")
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)

            try:
                avatar = Avatar.objects.get(user=request.user.id).image.url
            except:
                avatar = "/media/avatars/default.png"
            finally:
                request.session["avatar"] = avatar

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


# EDIT PROFILE


@login_required
def profile(request):
    is_user = request.user
    if request.method == "POST":
        form = ProfileForm(request.POST)
        if form.is_valid():
            user = User.objects.get(username=is_user)
            user.email = form.cleaned_data.get("email")
            user.first_name = form.cleaned_data.get("first_name")
            user.last_name = form.cleaned_data.get("last_name")
            user.save()
            messages.success(request, "Profile updated successfully")
            return redirect(reverse_lazy("profile"))
    else:
        form = ProfileForm(instance=is_user)
        username = is_user.username
    return render(request, "profile.html", {"form": form, "username": username})


class ChangePasswordView(CustomLoginRequiredMixin, PasswordChangeView):
    template_name = "change_password.html"
    success_url = reverse_lazy("profile")
    form_class = MyPasswordChangeForm

    def form_valid(self, form):
        messages.success(self.request, "Change password successfully")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.warning(self.request, "Change password failed")
        return super().form_invalid(form)


@login_required
def avatar_change(request):
    is_user = request.user
    if request.method == "POST":
        form = AvatarForm(request.POST, request.FILES)
        if form.is_valid():
            user = User.objects.get(username=is_user)
            avatar_old = Avatar.objects.filter(user=is_user)
            if len(avatar_old) > 0:
                for i in range(len(avatar_old)):
                    avatar_old[i].delete()

            avatar = Avatar(user=user, image=form.cleaned_data.get("image"))
            avatar.save()

            image = Avatar.objects.get(user=is_user).image.url
            request.session["avatar"] = image

            messages.success(request, "Avatar updated successfully")
            return redirect(reverse_lazy("profile"))
    else:
        form = AvatarForm()
    return render(request, "avatar.html", {"form": form})


# CONTACT


def contact(request):
    return render(request, "contact.html")


# CART


@login_required
def cart(request):
    return render(request, "cart.html")


# CHECKOUT


@login_required
def checkout(request):
    return render(request, "checkout.html")


# ABOUT ME


def about_me(request):
    return render(request, "about_me.html")
