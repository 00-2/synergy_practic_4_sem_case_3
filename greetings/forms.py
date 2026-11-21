from django import forms

from .models import Greeting


class GreetingForm(forms.ModelForm):
    class Meta:
        model = Greeting
        fields = ["name"]
        labels = {"name": "Имя"}
        widgets = {"name": forms.TextInput(attrs={"autocomplete": "given-name"})}
        error_messages = {"name": {"required": "Введите имя."}}
