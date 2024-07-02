from django import forms

from .models import About, Product, Testimonial

# Form Products


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = "__all__"
        widgets = {
            "name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "id": "name",
                    "name": "name",
                    "placeholder": "Product Name",
                }
            ),
            "price": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "id": "price",
                    "name": "price",
                    "placeholder": "Product Price",
                }
            ),
            "stock": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "id": "stock",
                    "name": "stock",
                    "placeholder": "Product Stock",
                }
            ),
            "category": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "id": "category",
                    "name": "category",
                    "placeholder": "Product Category",
                }
            ),
            "image_url": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "id": "image_url",
                    "name": "image_url",
                    "placeholder": "Product Image URL",
                }
            ),
        }


class AboutForm(forms.ModelForm):

    class Meta:
        model = About
        fields = "__all__"
        widgets = {
            "first_name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "id": "first_name",
                    "name": "first_name",
                    "placeholder": "About First Name",
                }
            ),
            "last_name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "id": "last_name",
                    "name": "last_name",
                    "placeholder": "About Last Name",
                }
            ),
            "position": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "id": "position",
                    "name": "position",
                    "placeholder": "About Position",
                }
            ),
            "description": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "cols": "30",
                    "rows": "5",
                    "id": "description",
                    "name": "description",
                    "placeholder": "About Description",
                }
            ),
            "image_url": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "id": "image_url",
                    "name": "image_url",
                    "placeholder": "About Image URL",
                }
            ),
        }

class TestimonialForm(forms.ModelForm):

    class Meta:
        model = Testimonial
        fields = "__all__"
        widgets = {
            "first_name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "id": "first_name",
                    "name": "first_name",
                    "placeholder": "First Name",
                }
            ),
            "last_name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "id": "last_name",
                    "name": "last_name",
                    "placeholder": "Last Name",
                }
            ),
            "position": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "id": "position",
                    "name": "position",
                    "placeholder": "Position",
                }
            ),
            "testimonial": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "cols": "30",
                    "rows": "5",
                    "id": "testimonial",
                    "name": "testimonial",
                    "placeholder": "Testimonial",
                }
            ),
            "image_url": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "id": "image_url",
                    "name": "image_url",
                    "placeholder": "About Image URL",
                }
            ),
        }
