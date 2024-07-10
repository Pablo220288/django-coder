from django.conf.urls import handler404, handler500
from django.contrib.auth.views import LogoutView
from django.urls import include, path

from models.views import *

urlpatterns = [
    path("", index, name="index"),
    path("home/", index, name="home"),
    path("shop/", shop, name="shop"),
    path("about/", about, name="about"),
    path("contact/", contact, name="contact"),
    # path Login
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    path("register/", register, name="register"),
    # path Products
    path("products/", Products.as_view(), name="products"),
    path("product/create/", ProductCreate.as_view(), name="productCreate"),
    path("product/update/<int:pk>", ProductUpdate.as_view(), name="productUpdate"),
    path("product/delete/<int:pk>", ProductDelete.as_view(), name="productDelete"),
    # path Abouts
    path("abouts/", Abouts.as_view(), name="abouts"),
    path("about/create/", AboutCreate.as_view(), name="aboutCreate"),
    path("about/update/<int:pk>", AboutUpdate.as_view(), name="aboutUpdate"),
    path("about/delete/<int:pk>", AboutDelete.as_view(), name="aboutDelete"),
    # path Testimonials
    path("testimonials/", Testimonials.as_view(), name="testimonials"),
    path("testimonial/create/", TestimonialCreate.as_view(), name="testimonialCreate"),
    path(
        "testimonial/update/<int:pk>",
        TestimonialUpdate.as_view(),
        name="testimonialUpdate",
    ),
    path(
        "testimonial/delete/<int:pk>",
        TestimonialDelete.as_view(),
        name="testimonialDelete",
    ),
    # path Services
    path("services/", Services.as_view(), name="services"),
    path("service/create/", ServiceCreate.as_view(), name="serviceCreate"),
    path(
        "service/update/<int:pk>",
        ServiceUpdate.as_view(),
        name="serviceUpdate",
    ),
    path(
        "service/delete/<int:pk>",
        ServiceDelete.as_view(),
        name="serviceDelete",
    ),
    # Delete
    path("delete/<str:type>/<str:id>/", delete, name="delete"),
    # Profile
    path("profile/", profile, name="profile"),
    path("change-password/", ChangePasswordView.as_view(), name="changePassword"),
    path("change-avatar/", avatar_change, name="changeAvatar"),
    # Cart
    path("cart/", cart, name="cart"),
    path("checkout/", checkout, name="checkout"),
]

handler404 = Error404.as_view()
