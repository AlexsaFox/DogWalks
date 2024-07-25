from django import forms

from main.models import DogAge, DogSize, DogColor


class DogCreateForm(forms.Form):
    name = forms.CharField(max_length=100)
    age = forms.ChoiceField(choices=DogAge.choices)
    breed = forms.CharField(max_length="200")
    size = forms.ChoiceField(choices=DogSize.choices)
    color = forms.ChoiceField(choices=DogColor.choices)
    activity = forms.CharField(max_length="500")
    relations_with_cats = forms.BooleanField()
    relations_with_dogs = forms.BooleanField()
    relations_with_kids = forms.BooleanField()
    relations_with_adults = forms.BooleanField()
    gender = forms.BooleanField(help_text="true - девочка, false - мальчик")
    address = forms.CharField(max_length="100")
    description = forms.CharField(max_length="1000")