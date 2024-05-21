from django import forms

from . import models


class PlaceForm(forms.ModelForm):
    class Meta:
        model = models.Place
        fields = ["name", "description", "longitude", "latitude"]
        # widgets = {
        #     'name': forms.TextInput(attrs={'type': 'text'}),  # Пример виджета для текстового поля
        #     'description': forms.Textarea(attrs={'rows': 4, 'cols': 40}),
        #     # Пример виджета для многострочного текстового поля
        #     'longitude': forms.NumberInput(attrs={'type': 'number'}),
        #     # Пример виджета для числового поля
        #     'latitude': forms.NumberInput(attrs={'type': 'number'}),
        #     # Пример виджета для числового поля
        # }