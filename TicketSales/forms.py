from dataclasses import fields
from django import forms
from .models import Concert


class SearchForm(forms.Form):
    query = forms.CharField(label="نام کنسرت", max_length=254, required=False)


class ConcertForm(forms.ModelForm):
    class Meta:
        model = Concert
        fields = '__all__'
