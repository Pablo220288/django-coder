from django import forms

from .models import Product

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
