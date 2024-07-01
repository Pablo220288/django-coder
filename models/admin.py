from django.contrib import admin
from django.utils.html import format_html

# Register your models here.
from .models import *


class ProductAdmin(admin.ModelAdmin):
    list_display = ("image", "name", "category", "price", "stock")

    def image(self, obj):
        return format_html(
            '<img src="/models/static/images/{}" width="30" />', obj.image_url
        )


class AboutAdmin(admin.ModelAdmin):
    list_display = ("image", "name", "position")

    def image(self, obj):
        return format_html(
            '<img src="/models/static/images/{}" width="30" />', obj.image_url
        )

    def name(self, obj):
        return format_html("{} {}", obj.first_name, obj.last_name)


class TestimonialAdmin(admin.ModelAdmin):
    list_display = ("image", "name", "position")

    def image(self, obj):
        return format_html(
            '<img src="/models/static/images/{}" width="30" />', obj.image_url
        )

    def name(self, obj):
        return format_html("{} {}", obj.first_name, obj.last_name)


admin.site.register(Product, ProductAdmin)
admin.site.register(About, AboutAdmin)
admin.site.register(Testimonial, TestimonialAdmin)
