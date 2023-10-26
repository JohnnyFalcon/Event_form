from django import forms
from django.forms import ModelForm
from .models import EventUser


# Create user data form


class EventForm(ModelForm):
    class Meta:
        model = EventUser
        fields = "__all__"  # Tuple version ("name", "surname", "email", "birth")
        labels = {
            "name": "",
            "surname": "",
            "email": "",
            "birth": "Birth Date",
        }
        widgets = {
            "name": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Name"}
            ),
            "surname": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Surname"}
            ),
            "email": forms.EmailInput(
                attrs={"class": "form-control", "placeholder": "E-mail"}
            ),
            "birth": forms.DateInput(
                attrs={
                    "class": "form-control",
                    "type": "date",
                }
            ),
        }
