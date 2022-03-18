from django import forms
from .models import Garden, Plant

class GardenForm(forms.ModelForm):
    class Meta:
        model=Garden
        fields='__all__'

class PlantForm(forms.ModelForm):
    class Meta:
        model=Plant
        fields='__all__'