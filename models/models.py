from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    stock = models.IntegerField()
    category = models.CharField(max_length=100, default="")
    image_url = models.CharField(max_length=2083, default="")

    class Meta:
        verbose_name_plural = "Products"
        verbose_name = "Product"
        ordering = ["name"]

    def __str__(self):
        return self.name


class About(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    description = models.TextField(default="")
    image_url = models.CharField(max_length=2083, default="")

    class Meta:
        verbose_name_plural = "Abouts"
        verbose_name = "About"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Testimonial(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    testimonial = models.TextField(default="")
    image_url = models.CharField(max_length=2083, default="")

    class Meta:
        verbose_name_plural = "Testimonials"
        verbose_name = "Testimonial"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

