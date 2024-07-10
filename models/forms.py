from django import forms
from django.contrib.auth.forms import (
    PasswordChangeForm,
    UserChangeForm,
    UserCreationForm,
)
from django.contrib.auth.models import User

from .models import About, Avatar, Product, Service, Testimonial

# Forms


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


class ServiceForm(forms.ModelForm):

    class Meta:
        model = Service
        fields = "__all__"
        widgets = {
            "title": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "id": "title",
                    "name": "title",
                    "placeholder": "Service Title",
                }
            ),
            "description": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "id": "description",
                    "name": "description",
                    "placeholder": "Service Description",
                }
            ),
            "icon_url": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "id": "icon_url",
                    "name": "icon_url",
                    "placeholder": "Service Icon",
                }
            ),
        }


class RegisterForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "id": "email",
                "name": "email",
                "placeholder": "Enter email",
            }
        ),
    )
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "id": "password1",
                "name": "password1",
                "placeholder": "Enter Password",
            }
        ),
    )
    password2 = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "id": "password2",
                "name": "password2",
                "placeholder": "Enter Password Again",
            }
        ),
    )

    class Meta:
        model = User
        fields = (
            "username",
            "email",
            "first_name",
            "last_name",
            "password1",
            "password2",
        )
        widgets = {
            "username": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "id": "username",
                    "name": "username",
                    "placeholder": "Username",
                }
            ),
            "first_name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "id": "username",
                    "name": "username",
                    "placeholder": "Enter First Name",
                }
            ),
            "last_name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "id": "username",
                    "name": "username",
                    "placeholder": "Enter Last Name",
                }
            ),
        }


class ProfileForm(UserChangeForm):
    email = forms.EmailField(
        required=True,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "id": "email",
                "name": "email",
                "placeholder": "Enter email",
            }
        ),
    )
    first_name = forms.CharField(
        label="Nombre",
        max_length=50,
        required=True,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "id": "first_name",
                "name": "first_name",
                "placeholder": "Enter first name",
            }
        ),
    )
    last_name = forms.CharField(
        label="Apellido",
        max_length=50,
        required=True,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "id": "last_name",
                "name": "last_name",
                "placeholder": "Enter last name",
            }
        ),
    )

    class Meta:
        model = User
        fields = ["email", "first_name", "last_name"]


class MyPasswordChangeForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["old_password"].widget = forms.PasswordInput(
            attrs={
                "class": "form-control",
                "id": "old_password",
                "name": "old_password",
                "placeholder": "Enter old password",
            }
        )
        self.fields["new_password1"].widget = forms.PasswordInput(
            attrs={
                "class": "form-control",
                "id": "new_password1",
                "name": "new_password1",
                "placeholder": "Enter new password",
            }
        )
        self.fields["new_password2"].widget = forms.PasswordInput(
            attrs={
                "class": "form-control",
                "id": "new_password2",
                "name": "new_password2",
                "placeholder": "Enter new password again",
            }
        )


class AvatarForm(forms.ModelForm):

    image = forms.ImageField(
        required=True,
    )

    class Meta:
        model = Avatar
        fields = ["image"]
