from django.urls import include, path

from models.views import *

urlpatterns = [
    path("", index, name="index"),
    path("home/", index, name="home"),
    path("shop/", shop, name="shop"),
    path("about/", about, name="about"),
    path("service/", service, name="service"),
    path("blog/", blog, name="blog"),
    path("contact/", contact, name="contact"),
    path("cart/", cart, name="cart"),
    path("checkout/", checkout, name="checkout"),
]
