from django import forms
from .models import Country

class CountryForm(forms.ModelForm):
    country = forms.CharField(widget=forms.TextInput({"class": "form-control"}))
    price = forms.IntegerField(widget=forms.TextInput({"class": "form-control", "type": "number"}))
    text = forms.CharField(widget=forms.TextInput({"class": "form-control", "type": "text"}))
    
    class Meta:
        model = Country
        fields = ("country", "airline", "price", "image", "text")
