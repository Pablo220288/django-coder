from django.conf.urls import handler404, handler500
from django.contrib.auth.views import LogoutView
from django.urls import include, path

from models.views import *

urlpatterns = [
    path("", index, name="index"),
    path("home/", index, name="home"),
    path("shop/", shop, name="shop"),
    path("about/", about, name="about"),
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
    # Delete
    path("delete/<str:type>/<str:id>/", delete, name="delete"),
    path("service/", Services.as_view(), name="service"),
    path("forms/<str:type>/<str:action>/<str:id>/", forms, name="forms"),
    path("blog/", blog, name="blog"),
    path("contact/", contact, name="contact"),
    path("cart/", cart, name="cart"),
    path("checkout/", checkout, name="checkout"),
]

handler404 = Error404.as_view()
